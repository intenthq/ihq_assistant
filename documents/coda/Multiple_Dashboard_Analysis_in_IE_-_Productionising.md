***Effortless Dashboard Switching Made Simple.***

# Background

User research has identified there are at least 2 core use-cases where users need to work on multiple dashboards. To enable the user to best achieve their goals, they would greatly benefit from being able to work and edit these dashboards within the same session.

- **Comparisons:** 
  - **Decision making:** I’m choosing the best going in-market audience for a campaign in terms of size and profiles. To do that, I’m comparing a couple of different audience segments in each dashboard.
  - **Cross analysing:** I’m cross analysing a few different types of audience segments in each dashboard in order to understand their traits. I’m looking to share how our customer base looks like to stakeholders to help their strategies.
- **Efficient audience building workflows:** 
  - **Creating similar audiences:** I’m creating multiple similar in-market audience segments for a campaign (message codes in VZ). To do that, I’m working on a few audience segments in each dashboard.

**Knowing this, we’ve developed the means of allowing the given scenarios - multiple dashboards to be worked on at the same time. This has been tested by client and internal users within the production environments. The feature is currently behind a feature flag.**





# Target Audience

IE users





# Problem

To be able to fully release this functionality as production quality, we want to tackle 3 usability risks we found during initial testing :

- **Users are unsure which dashboard they have open.**
  - The dashboard name is displayed on the browser tabs but it’s not clear enough, especially with an increase in the number of tabs open, the tab size reduces. 
  - This impacts the risk of accidental errors.
- **Enable a way for users to have a ‘playground’ for exploring**
  - Users often want to carry out some exploration which can conflict with the ‘auto-save’ feature
- **Users need a way to create a new dashboard**
  - Currently all new dashboards are saved instances of a previously worked on dashboard
  - We need a way for users to easily create new dashboard views, that work with the user expectations of auto-save.





# Justification

**We have a evidence captured from users that this will add value and increase user adoption.**

**Why?**

- Both internal users (Intent HQ CS team) and VZ power users found that having this functionality greatly increases their task efficiency and reduces the risk of errors.
- The approach used in testing is greatly favoured by users as the dashboards being worked on are auto-saved (like the ‘working dashboard’ in IE). Unlike the existing functionality where users need to save a new version of any saved dashboard they work on, which is unintuitive and creates lots of friction and frustration with the workflow and managing their saved dashboards.  

**Why now?**

- Users are actively choosing to use the testing version despite the friction (behind the feature flag) in their daily tasks.
- This will not only remove the current friction for using the feature flag, but also remove a lot of the support and training needs caused by intuitive workflows and the current restriction of a single dashboard view.

**What would happen if we didn’t do this?**

- Increased user frustration by users who are actively using the feature flag, and have been doing do for 6 months





# Goal & Success

- Increase user adoption by removing a critical pain point.
- Remove a lot of the support and training needs caused by intuitive workflows.





# User Outcomes & Benefits

Users will be able to perform multiple segments analysis easier 





# Appetite

Small batch (1 designer, 1-2 devs, 1-2 weeks)





# Solution

**User flow changes:**

- The starting point of the user journey will change from users landing on ‘the working dashboard’ view to a landing page.
  - The landing page will consist of:
    - List of dashboards (separated by ‘my dashboards’ and ‘shared dashboards’, accessed by Tabs at the of the lists)
    - A button to ‘create new dashboard’

**Opening saved dashboards:**

- When the user opens a dashboard, it opens in a new browser tabs. 
- The user is able to work across multiple dashboards across different browser tabs.
- When the user make changes to any dashboard, it ‘auto-saves’ them and this removes the needs of saving the changes explicitly.
  - The auto-save approach has been tested and proven to be expected and preferred to uses
  - This also reduces the risk of unsaved audiences that could be potentially timely to recreate causing greater frustration than taking a ‘save as’ approach
    - NOTE: whilst the existing ‘save as’ approach is used for saving dashboards, the users actions are always ‘auto-saved’ in the ‘working dashboard’
- Opening shared dashboards:

**Creating new dashboards:**

- To make a much simpler experience and prevent users from accidentally saving over existing dashboards, users will be able to create new dashboards
  - The button will be located at the top of the page as a clear CTA
  - Upon clicking:
    - The user will see a dialog box and prompted to name their dashboard
    - The user will not be able to proceed until a name is entered. The ‘confirm’ button will be disabled until a name is entered.
    - Once the user ‘confirms’, a new dashboard will be creating using the configuration from the ‘default dashboard’ config with no filters.
      - The new dashboard will appear at the top of the users ‘my dashboards’ list
    - The user will be able to cancel the function

**Duplicating dashboards:**

- A ‘duplicate’ dashboard will be added beside the ‘open’ dashboard button within the Dashboard list item
  - When a user clicks ‘duplicate’, they will see a dialog box and prompted to name their dashboard.
    - The default will be ‘Copy of <dashboard name>’
  - The user will be able to proceed with the default name, or they can rename. The ‘confirm’ button will be active at all times.



**Nice to haves:**

- (Nice to have) Display dashboard names within the dashboard view to make it clear while using multiple dashboards at the same time.
  - Currently the feature flag function shows the dashboard name in the browser tab
  - This is to resolve the issue of users not having clarity about which dashboard is being worked on, and help towards accidental errors caused by this lack of clarity
- (Nice to have) Editing dashboard name on the fly.

 

## User flows:

All user flows are shown below and available as a clickable prototype in figma using the links below.

**Flow: Create new dashboard /** **[Figma](https://www.figma.com/proto/mKaAcYATDsnLfPhjSMt3Wd/Workflow-Tools-v1-(31%2F5%2F2024)?page-id=7%3A2&node-id=280-31825&viewport=-3500%2C-946%2C0.35&t=GT8bYGf2xjElOmn1-9&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=280%3A31825&show-proto-sidebar=1)**



**Flow: Open dashboard /** **[Figma](https://www.figma.com/proto/mKaAcYATDsnLfPhjSMt3Wd/Workflow-Tools-v1-(31%2F5%2F2024)?page-id=7%3A2&node-id=286-17724&viewport=-3500%2C-946%2C0.35&t=GT8bYGf2xjElOmn1-9&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=286%3A17724&show-proto-sidebar=1)**



**Flow: Duplicate from list /** **[Figma](https://www.figma.com/proto/mKaAcYATDsnLfPhjSMt3Wd/Workflow-Tools-v1-(31%2F5%2F2024)?page-id=7%3A2&node-id=329-22655&viewport=-3500%2C-946%2C0.35&t=hVIis3eQj2awXA0r-9&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=329%3A22655&show-proto-sidebar=1)**



**Flow: Duplicate from within the dashboard /** **[Figma](https://www.figma.com/proto/mKaAcYATDsnLfPhjSMt3Wd/Workflow-Tools-v1-(31%2F5%2F2024)?page-id=7%3A2&node-id=362-24805&viewport=-3500%2C-946%2C0.35&t=hVIis3eQj2awXA0r-9&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=362%3A24805&show-proto-sidebar=1)**







https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FmKaAcYATDsnLfPhjSMt3Wd%2FWorkflow-Tools-v1-(31%252F5%252F2024)%3Fpage-id%3D7%253A2%26node-id%3D280-31825%26viewport%3D-2620%252C195%252C0.29%26t%3DVOu8DFCxZEcjZ2xJ-1%26scaling%3Dmin-zoom%26content-scaling%3Dfixed%26starting-point-node-id%3D280%253A31825%26show-proto-sidebar%3D1

















Done reading? Click here. → Albert Pastrana, Javier Pedreira, Mark Bunn, Ismael Perez, Arfa Mahmood, Meri Cortada, Daria Barbalata, Jonathan Lakin

Mark Bunn, Javier Pedreira, Ismael Perez, Albert Pastrana, Daria Barbalata, Arfa Mahmood, Jonathan Lakin I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes | Response | By |
| --- | --- | --- | --- | --- | --- | --- |
| false | What happens if a user opens the same dashboard twice? The way we thought about it (and the way it’s currently implemented in the open in new window) is by only allowing the user to have the same dashboard open once (by directing them to the same tab). But that’s not how most tools do it as they allow you to open the same one in different tabs. | Albert Pastrana |  |  | Since we don’t find the needs of opening same dashboards in multiple tabs, I think we can keep the current behaviour. | Jaekyoung Lee |
| false | **MXP Point of View**<br/><br/>Having the ability to have more dashboards open at one time will likely help avoiding confusion for future MXP users as well. They will have two separate dashboards for now to analyse the transactional and behavioural data and in case they had both open and refreshed and the page changed, the product would feel buggy. What is more important is the clarity on which dashboard the user has currently open.  <br/><br/><br/><br/>**Concern about Autosave**<br/><br/>I don’t think autosaving is a good idea for the dashboards. The best use case in my opinion is to prompt the user if they wanted to save their changes. <br/><br/>This would make it obvious for the user that they can use the dashboards as playgrounds and if they decide to save the changes, they don’t need to create a new dashboard. Also, by having to create new dashboards as playgrounds, we increase the number of steps for the user to get to this point as well as encourage the creation of more dashboards, increasing the potential ‘clutter’ for users. <br/><br/><br/><br/>For the MXP in the IE, we will have two default dashboards that we will set up for each new client in the beginning - one for Orange and one for Fintonic - to make sure that they have the right data in the right dashboard. They will likely use the dashboards as a playground and save their own views if necessary from that starting point. If we introduce Autosave, I have a very strong feeling that we will end up with a lot of confused users who would try to refresh their browsers or re-open the dashboards with no success after just playing around and wanting to see the original setup. <br/><br/>If we have to go with an Autosave feature no matter what, I think we should consider at least Redo / Reset option or a History of changes.  | Luca Szabó |  |  |  |  |
| false |  |  |  |  |  |  |