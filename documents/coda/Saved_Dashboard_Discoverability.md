***Organise. Search. Discover Your Dashboard In a Second with Custom Labels.***

# Background

The usability issue of organisation and discoverability of saved dashboards has been known for many years. This has been deferred as it was not an major issue for small number of internal users. However, we are now looking to have 130+ users in VZ who are frequently using IE and generating a lot of saved content. This means that the impact of this problem is rapidly increasing.





# Problem

- As a campaign manager, I already have 60+ dashboards saved for my campaigns. 
  - I often need to create multiple similar (message codes in VZ) in each dashboard for a campaign. I would like to organise them in an intuitive way so I can easily locate the right one when I come back to revisit those dashboards.
- As a client support person, I struggle to find the dashboard I’m looking for quickly and this makes my job inefficient. This is because I have 100+ saved dashboards and it’s difficult to remember the exact name as well as the location especially for older dashboards.

**User-journey + pain points + ideas mapping:**







# Justification

**Why?**

- This is vital to have the functionality in place before the 130+ VZ users encounter issues that negatively impacts user adoption.
- User research has found that users have expectation to find and organise dashboards in industry standard way.
- This will increase the efficiency of client support team’s work.

**Why now?**

- We know this will be a problem when users have lots of (50+) dashboards by internal users. 
- We want to prevent clients users from experiencing the pain experienced by our internal users.
  - Many high frequency users have already started to experience the pain

**What would happen if we didn’t do this?**

- Using/discovering saved dashboard will be unintuitive and slow. 
- Negatively impact on user adoption.





# Appetite

Small batch (1 designer, 1-2 devs, 1-2 weeks)





# Goal & Success

Increase user adoption.

Meet user expectation by providing standard industry functionality.





# User Outcomes & Benefits

This will help users to find their saved assets easier and quicker.





# Solution

- Allow searching from within the dashboard list 
- Search results will support partially as well as exact search term to accommodate slight different variations of same campaign name (aka fuzzy search)
- Search results will only display matching dashboard names for now
  - Our research hasn’t found a need to match filter or card names from within the Saved Dashboard
- We will allow the adding of custom labels to each dashboards to group/categories them to assist with organisation and identification
- Allow filtering dashboards by labels









# Nice to haves

- Allow multiple labels to a dashboard
- Allow to open multiple dashboard detail sections at the same time
- Make dashboard list view as a user starting point rather then a dashboard view





# Out of Scope

- Dashboards automatically grouped by labels
- Filtering dashboards by other information such as dates created/last edited/last shared/last exported





# Research Questions As We Build

- How best to prioritise search results
- How best to order list of dashboards
- Which information is useful for filtering dashboard





Done reading? Click here. → Shy Alon, Arfa Mahmood, Meri Cortada, Daria Barbalata

Daria Barbalata, Arfa Mahmood, Mark Bunn I’m aligned with the problems & goals

 I’m not aligned

Albert Pastrana I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes | Response | By |
| --- | --- | --- | --- | --- | --- | --- |
| false | I think we should try to do this one in two phases. First we add the search capability that it’s super low effort (2-3 days) and see how people respond to it. If they feel there is still need for labels, then we think of adding support for labels. | Albert Pastrana | Luca Szabó |  | I agree with that 2 iterations. But I think the labelling is where the main value can be delivered for this problem. So should be in scope. Given 3 weeks appetite we could achieve that.  <br/>  <br/>Search is what currently users are using anyway (using browser search). Just replacing the search bar UI within the product won’t solve user pain much. It will be underwhelming.  <br/> | Jaekyoung Lee |
| false | **UPDATE: (9/8/2024)**<br/><br/><br/><br/>We’ve partially built this. <br/><br/>We’ve implemented the search function but have left off the tagging.<br/><br/>With the [Multiple Dashboard Shape Up](https://coda.io/d/_d5hIdONEiOD/_suWy3#_luf4s), we want to learn how those changes impact the users to assess if tagging is the most suitable way. | Mark Bunn |  |  |  |  |