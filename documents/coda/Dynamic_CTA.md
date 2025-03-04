# Problem

Our customers would like to personalize the notifications their users get using the Edge Console. We need to provide this capability via the Edge Console in both iOS and Android. This is specifically required for customers who would want to include a custom link that would lead their users to a personalized web page.

**Note**: A customer (Fishka) requested this feature.

## Current state

Within the Call to Action section of the campaign creation flow you can specify a link. Currently this can be a valid URL, and clicking will take the user to the specified location

  


## User Stories

- **As a Marketer,** I want my users to get personalized notification so their engagement will increase.
- **As a Marketer,** I want to use custom links in the same campaign to manage my users’ journey.



# Appetite

- Development: 4 weeks
- Testing: 2 week



# Solution

**Note**: Since the 1st phase will not include any changes in the Edge Console (other than explanation text over the CTA field), the solution already more or less exists in the compiler and the iOS SDK. We will need to verify the solution (maybe fix it), and expand it to the Android SDK.

The solution will include the following:

1. The Edge Console will support inserting templated text. The tooltip will include a reference to a documentation page, e.g. “If you would like to include the value of a micro-segment, please consult the documentation here.”
2. The SDK will insert the value into the template. For example, if the template was “Welcome to ${current_city}!!!” The user will get (if their `current_city` value is “Tel Aviv”) “Welcome to Tel Aviv!!!”
   1. If the value doesn’t exist:  
The **correct** solution is to determine the behavior in the campaign (including setting a default value). To make it as simple as possible, if the value doesn’t exist, the campaign will not display anything, and a campaign error will be reported in the campaign report. 
   2. If the value is null:  
A host application error might result in a null value. This will be treated as if the value doesn’t exist.
   3. If the value is empty:  
An empty string value could be what the host application inserted on purpose, so it will be treated as a valid value.
   4. If the value exceeded max length:  
A string longer than 80 characters should be rejected, the campaign will not display anything, and a campaign error (including the length issue) will be reported in the campaign report.
3. **Bonus points:** As soon as the marketer writes “${” a drop down of the existing micro-segments will allow them to pick one, and picking will set it in the correct format. 

# Rabbit Holes

1. Trying to create a fancy UI. Maybe in the next phase.
2. Trying fancy value display resolutions. ToString() will do nicely (let’s consider dates in the future).

# No-Go's

None

# Potential

Here are some potential additional benefits:

- Loyalty customers like Fishka could base destination pages on the number of redeemable points a customer has (in a range)
- Loans company like ABG could have different destination pages based on the credit score range of the customer
- A company with internal segmentations like Evest could direct Silver, gold, platinum and diamond customers to different landing pages based on the typical behaviours of customers of the different ‘client level’ values

This could provide a means of making the destination page more relevant to the individual  
As a company, it feels as though we are often scared to measure conversion or actions beyond the initial click through. If we have a means of personalising or triaging customers beyond the initial click behaviour, that could really benefit us



Done reading? Click here. → Elad Ben-Tzedeff, Alexander Vlasik

Elad Ben-Tzedeff I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false |  | Tomer Lekach |  |  |