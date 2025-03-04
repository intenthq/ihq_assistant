# Problem

There is a huge amount of clutter in the Edge Console that needs to be removed. At best, it’s a distraction. At worst, it’s additional clicks that can be avoided and missing features that need to be explained.

## User Benefit

The main goal is to prevent hickups during sales calls and prevent customer success questions.

## User Stories

- **As a marketer,** I want the Edge Console only to offer existing capabilities, so I won’t have unanswered questions.
- **As a marketer,** I want to achieve my goals without being prompted to input useless information that serves no purpose, so I could save time.



# Appetite

- Development: 2 weeks
- Testing: 3 days



# Solution

## Remove Unimplemented Pages

- Persona Builder
- Settings
  - Localization
  - User management
  - Billing (We might keep it - pending discussion with the CS team)

## Remove Extra Steps

1. Remove the **Goal** step of the campaign creation.
   1. Remove the “goal” of the campaign from the campaign’s summary
   2. Use a default string (”Engagement”) so the Discover apps won’t break.
2. Rename the **Apps** step to **Setup**.
   1. The header should say: “Set a name and select the apps for the campaign”
3. Add to the **Setup** page name settings (same as it is in the current **Goal** page). Both name and app selection should be required for proceeding.
4. In the **Scope** page, automatically set the start day for today and the end date for a year after the start date (minus one day, so if it starts on May 25th it will end on May 24th).
5. In the **Scope** page, remove the warning dialog if the user didn’t select a country and region.

## Impact

- **Improved User Experience:** Create campaigns without extra steps.

# Rabbit Holes

???

# No-Go's

?



Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false | Is there a reference data list of installed apps and their group? | Lewis Longman-Jones |  |  |
| false | What would be the timeframe for these changes? We are going to be setting up training sessions for both Fishka and ABG in the next 4-8 weeks- if these changes will happen relatively quickly then we will need new documentation and training materials | Ben Marnan |  |  |