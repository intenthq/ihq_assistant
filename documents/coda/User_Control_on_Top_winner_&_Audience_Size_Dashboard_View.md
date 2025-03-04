***Provide enough information about two different view and give users control to choose.***

# Background

The Insights Explorer offers two different ways of viewing data displayed on the card visualisations: 

- Top Winner view
- Audience Size view 

By default, when users add or remove filters, the dashboard displays the Top Winner view (unless there are no filters ) as this provides the richest understanding of the audience and is one of the Insights Explorers most valuable features. However, there is unexpected behaviour when the user explicitly chooses to view as Audience Size; the tool doesn’t preserve the user's setting.





# Target Audience

All IE users 





# Problem

1) A large amount of users, particularly at Verizon, want to have the Audience Size view as actual counts are more relevant for their needs, particularly with understand sizes when assessing opportunities.

- The default behaviour of switching to Top Winners causes **significant friction** and causes great frustration by having to repeatedly change the selection every time while exploring the data. 
  - **An example scenario looks like** : user adds a filter >  switch to audience size > add another filter > switch to audience size >  add another filter  > switch to audience size > Repeat. 
  - Currently **a user has to switch 10-20 time per one IE session** that last around 30minute to get the job done. The problem is escalating as we aim to increase the number of VZ active users (expected to reach 100+), who will also encounter this issue.
- This makes data exploration **very inefficient and slow to complete tasks.** Because of this, this issue has been reported directly by Verizon end users several times over the last several months as a main pain point.

*Actions on VIP (VZ off-prem) the last 3 month (Feb-Apr 2024):*

*Average action : 170 times per month* 

*Action per user per session: up to 22 times*  


2) Many client **End users do not understand Top winner insight** so they don’t use the insights

- We want to use this problem as an opportunity to both satisfy their need to keep audience size, whilst making the Top Winners feature more visible and allow easy switching between views





# Justification

**We have a evidence captured from users that this will add value and increase user adoption.**

**Why?**

- Significant usability issue
  - More detail captured above in the problem statements.

**Why now?**

- This has been reported numerous times and is repeatedly asked about in the weekly CS > Verizon user checkin
  - We have now reached 130+ active users at Verizon and as user numbers continue to grow will become a greater frustration

**What would happen if we didn’t do this?**

- Increased user frustration
- The CS team will be exposed to the same complaint every week and could cause damage and distrust to a positive relationship that has been developed





# Goal & Success

- Improved user satisfaction by removing frustration that occurs with the majority of users multiple times per session.
- Increase user adoption by removing a critical pain point.
- Give more useful information about Top winner insights.
- Meet product usability standard by following UX principles of honouring user selection and give them control.





# User Outcomes & Benefits

- This will enable the user to complete their tasks smooth and faster.
- This will help users to understand difference between Top winner and Audience Size view





# Appetite

Small batch (1 designer, 1-2 devs, 1-2 weeks)





# Solution

- Make the controls more accessible and visible via a toggle control:
  - This will provide greater control and freedom to all users
  - And make the Top Winners feature more prominent so users who switch to Audience Size are reminded of the feature (which is currently available through a context menu launches with an ellipsis (3 dots ...) button )
- The users selected view will remain:
  - after each interaction
  - after each session when logging back in
  - with each saved dashboard when re-opening
- Changing dashboard level selection will override all card level selections
  - This has been confirmed with users to be the expected and preferred behaviour
- When adding new card, it will use the current dashboard level selection.
- We provide user-friendly explanation about Top Winner view when hovering.
- We keep both dashboard level and card level control as is.



# Future Iterations to consider

- Have the same toggle UI on card level. 





Done reading? Click here. → Rachel Yeomans, Meri Cortada, Jonathan Lakin

Rachel Yeomans, Jonathan Lakin I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes | Response (if needed) | By |
| --- | --- | --- | --- | --- | --- | --- |
| false | For a qualitative piece of feedback (in addition for this feature being the top requested feature across VZ users), during the 5/16 tiger team meeting, Sean Rose asked for a working session to find the best sub-segments for a dynamic variant test. He shared his screen to workshop, and during that 20 minute walk-through, he changed the volumes 10 times. Eduardo Amescua was also on the call and emphasized that he sees slides with screenshots that show the top winners and executives have confused that view with raw volume and if someone isn't there to correct them, the data can be dangerously mis-interpreted.  | Rachel Yeomans |  |  | Thank you for valuable input! |  |
| false | ATM, despite Audience size and Top winners, in the contextual menu there is also Top losers. How this other option will be handled?  | Meri Cortada |  |  | You are right! I omit top loser option from here, but the behaviour will exactly be the same. When user select Top loser, the product will remember the setting until user explicitly change it.  | Jaekyoung Lee |
| false |  | Luca Szabó |  |  |  |  |
| false | Need for Audience Size option saving in MXP<br/><br/>**MXP point of view**:<br/><br/>Having the ability save this preference at least when saving a dashboard will likely be critical for the MXP in IE. Most of the current use cases are based on Audience size and with no CS support, it is VERY likely that users will not understand Top Winners when onboarding. <br/><br/>**Concerns about the toggle**: <br/><br/>Having the global toggle for two options might be confusing that there is also Top Losers and make it less obvious that they can make changes on a card level as well. <br/><br/>Also, not very likely currently, but it could be tedious if the user built a custom dashboard with different options per cards and then used the toggle to play around, but without an ‘undo’ option they would need to re-do their settings all over again.  | Luca Szabó |  |  | **Re: Ability to save preference**<br/><br/>Yes this preference should always be saved <br/><br/>**Re: concerns of the toggle**<br/><br/>The Top Losers is a variant of the Top Winners so the global control is right to have 2 options and the Top Losers only appears on the list cards, so a localised toggle on the card would allow users to control the card and have visibility of the feature which is currently hidden on the card.<br/><br/>**Re: custom set ups**, our research has indicated the product is not used like this, and the only use case so far has been to illustrate the difference between Top Winners and Audience Size which the toggles will assist with this | Mark Bunn |
| false |  | Meri Cortada |  |  |  |  |