# Problem

Currently, Android campaigns within the Edge Console lack a user-friendly way to target users based on installed application groups defined in the remote configuration. This functionality relies on creating custom micro-segments, which can be cumbersome, requires advanced knowledge for customer success managers (CSMs), and is error prone.

Phase 1 is the “enablement phase”, meaning that we’ll create the pipelines for using this feature within the console. Additional potential “syntactic sugar” features will be added later.

**Note**: We will enrich this feature in the future by using inputs other than application groups, so the title of the feature is “Predictive Micro-Segments.” The text will be taken from the configuration file, so it could be anything from “In Market for Life Insurance” to “About to Switch Cellular Provider”. Label automation is deferred to later versions.

## User Benefit

This dedicated UI empowers customers to leverage application group targeting more effectively during ongoing campaign management and makes the process less error prone. 

## User Stories

- **As a Customer Success Manager,** I want to be able create campaigns for my customers without going into the complex process of defining custom micro-segments, so I could avoid the risk and extra work involved with custom micro-segments.
- **As a marketer,** I want to be able to use predictive features provided by Intent’s customer success team so I could engage better with my audience.



# Appetite

- Development: 4 weeks
- Testing: 1 week



# Solution

## Prerequisites

This solution leans heavily on the app groups defined in the customer’s configuration. The names of the categories will be used directly without any manipulation.

The names of the applications themselves will not be used.

## Audience

A new category called “Predictive Features” will be added to the *Audience* screen in the campaign creation flow. It should only be available for Android applications (for the time being).





Selecting this option will open a standard micro-segment configuration screen, in which the user will be able to select a group from the groups defined in the application’s active remote configuration. The title will be taken directly from the configuration.

The groups are defined under: `Configuration.DeepMS.AppList.<GroupName>.msName` where for each element under AppList there is a msName object there is a group as described [here](https://coda.io/d/_dySAKuGmmhr/Version-2020-02-20-02-20_sudVA#_lu2wY).  
The MS type is a String with Values of “`TRUE`” and “`UNKNOWN`”.  
E.g if the `GroupName` is “`AppsForZara`” and the `Configuration.DeepMS.AppList.AppsForZara.msName` =”`in_the_market_for_zara`”, then the campaign will be if `in_the_market_for_zara = “TRUE”`

The msName should be converted to title case:  in_the_market_for_zara => In the Market for Zara,  
and also for inTheMarketForZara and InTheMarketForZara

Each AppCategory could include a “includeInUI” flag. The category will be displayed only if that flag exists and it’s true.

The default is that it doesn’t exist.

***Note: Uninstalled option is deferred.***

### ***Audience Window Offering both Most Recent and First Indication***





Once the category is selected, the number of days in the status since the last or the first could be used as an additional parameter (similar to onboarding milestones). The data will need to refer to a different MS named <msName>DaysSinceFirst. E.g. if the msName is “`in_the_market_for_zara`” and we select more than 2, then the campaign will say and `in_the_market_for_zaraDaysSinceFirst` `> 2` or `in_the_market_for_zaraDaysSinceLast > 2`



### Summary Box Text

When there’s no limit:

When the limit is set:

“Users predicted as <category>”

“Users predicted as <category> with the <least / most> recent indication <days condition>”

## ~~Context~~

~~idAdditionally, a new category of micro moments will be added. This micro-moment will be triggered at the~~ ~~first time~~ ~~Edge will identify that the user is in that category.~~



~~In the context configuration screen, the only selector is the category.~~



**The Context was deferred in favor of using the audience for recently installed.**

## Impact

- **Improved Customer Experience:** The customers will be able to consume these audience and context features by themselves in a less error prone process.
- **Enhanced Sales Process:** Instead of hand waving, a visual demo using the Edge Console could be used to explain the application based micro-segments to the customers.

# Rabbit Holes

This approach assumes that the configuration of the DeepMS will not change.

# No-Go's

?



Done reading? Click here. → Elad Ben-Tzedeff, Dmytro Hnatovskyi

Elad Ben-Tzedeff I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false | Is there a reference data list of installed apps and their group? | Lewis Longman-Jones |  |  |