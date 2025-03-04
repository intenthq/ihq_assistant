# Problem

Data science team has the necessity to access top winners scores of insights-explorer data for assessing the output of modelled brands and check the behavioral data the are generating.

There is no current endpoint in IE that allows to access that data for a given field further than defining a dashboard.

Also only way for using those dashboard endpoint need a user session with the session cookies that is not suitable for a non-browser client.



# Appetite

1 week



# Solution

We propose to create an insight-explorer endpoint that can be used with a given api-key (no session cookie is mandatory) that given the set of 4 possible filters (audience, audience-exclusions, baseline and baseline-exclusions) and the card that want to be accessed, return the card data for those filters and card including the needed top-winners.

We want to reuse as much as possible current fetch dashboard code for this new endpoint.



Done reading? Click here. → Daria Barbalata

Daria Barbalata, Maciej Pfutzner I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |