# Tracking

[https://intenthq.atlassian.net/browse/EP-2](https://intenthq.atlassian.net/browse/EP-2)

#   
Background

The Intent Edge iOS SDK heavily relies on a push notification service (PNS), sending silent pushes every hour for processing time. The effectiveness of the SDK is closely tied to this integration. However, managing the PNS is sensitive, as it enables Intent HQ to send push notifications to all end users. To enhance its effectiveness and sensitivity, the PNS management system needs full productization, covering authentication, authorization, audit, transparency over current configuration, and robust error management.

Customers can make all their users experience a crash every hour due to a lack of sufficient testing and integration efforts.

### Note

Even after a successful integration, the customer’s developers can add an additional library which would cause the same crashes. They would feel more confident knowing they can immediately stop the process.

## Current State

Intent has an operational PNS. The management of the entire process goes through a clunky process of sending the push certificate to a customer success manager who has to provide it to a developer and so on.

# Problem

The problem is two-fold:

1. The customer has no direct control. If they want to switch certificates, or stop sending push messages altogether, they have to contact their customer success manager and ask them, which adds an unnecessary delay which might be critical in certain cases.
2. The process can feel amateurish and half-baked to the customer. Following our “Enterprise Ready” initiative, the customer onboarding process should be quick, painless, and create a good (or at least better) impression.

# Appetite

Migrating the management of the iOS push services to the Edge Console (which will soon support full SSO integration and role management) will reasonably take up to six weeks.

# Solution

The Edge Console already have an application management functionality.



The solution will be to change the view, for example to a tabbed one, which will provide all the required capabilities to manage the PNS. It will look something along those lines:









In the backend, the suggested architecture (to be approved by R&D) will keep the existing PNS service as is. Since the Edge Console already communicates with the API service, it makes sense that the API service will also manage the authorization.





Done reading? Click here. → Elad Ben-Tzedeff, Dmytro Hnatovskyi

Elad Ben-Tzedeff I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |