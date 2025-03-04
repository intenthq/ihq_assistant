import os
import time
import json
import requests

# Replace these with your actual values
API_KEY = os.environ.get("CODA_API_KEY")

DOC_ID = "5hIdONEiOD"

# Create a folder to store the exported pages
output_folder = f"documents/coda"
os.makedirs(output_folder, exist_ok=True)

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Step 1: Fetch all pages in the document
API_URL = f"https://coda.io/apis/v1/docs/{DOC_ID}/pages"
response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    pages = response.json()["items"]
    print(f"✅ Found {len(pages)} pages in the document.")

    # Step 2: Loop through each page and export it
    for page in pages:
        PAGE_ID = page["id"]
        PAGE_NAME = page["name"].replace(" ", "_")  # Clean name for file
        print(f"⏳ Exporting page: {PAGE_NAME} (ID: {PAGE_ID})")

        # Step 3: Request export for the page
        export_url = f"https://coda.io/apis/v1/docs/{DOC_ID}/pages/{PAGE_ID}/export"
        payload = {"outputFormat": "markdown"}

        export_response = requests.post(export_url, headers=headers, json=payload)
        if export_response.status_code != 202:
            print(f"❌ Error exporting {PAGE_NAME}: {export_response.text}")
            continue
        
        export_id = export_response.json()["id"]
        status_url = f"{export_url}/{export_id}"

        # Step 4: Poll until export is ready
        while True:
            status_response = requests.get(status_url, headers=headers)
            if status_response.status_code == 200:
                status_data = status_response.json()
                if status_data["status"] == "complete":
                    download_link = status_data["downloadLink"]
                    print(f"✅ Export complete for {PAGE_NAME}, downloading content...")
                    break
                else:
                    print(f"⏳ Waiting for {PAGE_NAME} to finish exporting...")
            else:
                print(f"❌ Error checking status: {status_response.text}")
                break
            time.sleep(5)  # Wait before checking again

        # Step 5: Download the exported content
        download_response = requests.get(download_link)
        if download_response.status_code == 200:
            content = download_response.content.strip()

            if content:  # Check if content is non-empty
                file_path = os.path.join(output_folder, f"{PAGE_NAME.replace('/', '')}.md")
                with open(file_path, "wb") as file:
                    file.write(content)
                print(f"✅ Saved {PAGE_NAME} as {file_path}")
            else:
                print(f"⚠️ Skipped {PAGE_NAME}, no content found.")
        else:
            print(f"❌ Error downloading {PAGE_NAME}: {download_response.text}")
else:
    print(f"❌ Error fetching pages: {response.status_code} {response.text}")