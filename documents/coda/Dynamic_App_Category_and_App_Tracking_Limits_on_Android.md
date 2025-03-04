### Iteration closed - progress updates [here](https://intent.slack.com/archives/C06P6PHD5S9/p1717430915578609). Next iteration:

- Strategic IHQ Graph product development being planned [here](https://coda.io/d/_d5hIdONEiOD/_suCJp).
- Using the new domains in VZ pipeline - WIP. More about this [here](https://coda.io/d/_dgMDDph8PXa#Roadmap-CANDIDATES-by-Quarter-FY24-2_tulxb/r77&view=modal).

# Background

The IHQ Graph, also known as the topic hierarchy, is an internal resource used by our topic model to understand which domains are relevant for which interests. For example, a brand - Foot Locker - could be associated with the *retail* topic and the *shoes* topic, and could be further categorised as *sports shoes.* This information is then used to model each topic starting from the users that visited brands associated with that topic in the graph.

The IHQ Graph is, therefore, a pre-requisite of [topic modelling](https://coda.io/d/_d5hIdONEiOD/_suY3M).

## Current State

Only 10% of our brands are linked to topics in the IHQ graph (also known as the topic hierarchy). More concerning is that about 100 topics are associated to 3 or less brands each. 

Considering that brands define the starting seeds for topic modelling with the scope of identifying significant topic signal to model against, there is an accuracy-coverage trade-off we should consider. If a topic is represented by many brands, a few potentially inaccurate ones are less risky because we expect the model to find enough signal in all the accurate ones. But if a topic is represented by very few brands and one of them is wrong, there is a high risk of modelling that topic against the wrong signal and producing flawed outputs. 

# Problem

As a data scientist in charge of topic modelling, I need a good coverage of brands per topic as well as a high accuracy in the brands association to those topics, so I can trust the quality of the topic seeds I use for modelling.

Notably, we need automated ways of achieving this coverage so that we reduce the manual effort involved in making necessary updates at the beginning but also for maintenance over time. 

# Appetite

This work will be focused on increasing the brand coverage of our least represented target topics used by Verizon as defined with CS stakeholders. See the most used topics at VZ [here](https://docs.google.com/spreadsheets/d/1xezqoUHgNI2yqNvd4o_N1vyC-a7pVlE3rxDjLf8LOJU/edit#gid=1725784178) and an analysis showing brand-topic mapping coverage [here](https://coda.io/d/_dK5h4iVEEUo/EDA-Brand-Topic-mappings_suXEw).

We will also aim to build and test automatic tools in order to have a good level of confidence that they can be used to map new brands into the IHQ Graph. However, achieving suitable coverage for new data-sets, especially new languages needs to be a subsequent body of work focused on a particular priority prospect as needed - potentially done during the PoC period. 

Within 6 weeks we aim to achieve [confirming actual target numbers with DS]

- min. coverage of 15 brands per VZ topic
- automatic tools that are able to semantically categorise new domains in english with a minimum of 60% accuracy.

# Solution

To do this we will use a combination of tools:

### Curation Tools and Approaches
| Name | Objective | Requirements | How it works? |
| --- | --- | --- | --- |
| NLP Classifier | Label domains with potential topic labels for easier manual curation | Need either high volume domains from the clients weblog data or a list of high priority domains, to classify.<br/>The curator needs to be from that geography so that they have the localised knowledge necessary to do this task.  | We train a supervised NLP classifier using the labelled domains in the IHQ Graph. The input features are meta data scraped from the domain web pages which contain descriptions of the page. <br/>This classifier achieves about 60% accuracy on the test set. This classifier is then used to predict labels for new domains. The top 5 predictions are presented to the manual curator with each domain to assist them in labelling them. |
| ChatGPT domain finder | Find potential domains for a specific topic for easier manual curation | The curator needs to be from that geography so that they have the localised knowledge necessary to do this task.  | We use the ChatGPT API with the prompt “`comma separated list of 40 '{}' URL websites + country`” for each of the topics we want candidate URLs for. <br/><br/>Curators are presented with potential URLs for topics and they annotate if these are correctly or incorrectly categorised.<br/><br/>Caveat: ChatGPT hallucinates so several URLs aren't real. Also some of the URLs provided don’t appear in our data so aren’t worth classifying as they won’t increase our coverage. |
| Human Curation | Given a topic ask a curator to find popular domain using Google and their general knowledge | The curator needs to be from that geography so that they have the localised knowledge necessary to do this task.  | Curators are presented with topics and the current domains that it contains. Using their own knowledge and Google they find more domains/brands to include in that topic.  |


Notably, the need for human curation should decrease over time as we’ll aim to use the data they curate to optimise the NLP classifier and hopefully require increasingly less manual verification.

## Rabbit holes

URL labelling - the goal is to define what is ‘enough’ per topic (e.g. 15 URLs per topic) and reach that level of coverage, but not try to map the entire brand data.

## **No-goes**

Covering non-english languages

For the english language we already have a set of labelled domains that we can use to train the NLP classifier and measure its performance, but it is not guaranteed that it will maintain that performance for data in other languages and either way - we will need to build up training sets for new languages. Ideally, we’d do this when we’re far enough in the sales process to be able to get a sample of data, but if this isn’t possible and we know the target language, we are likely to find data sets elsewhere (e.g. [https://builtwith.com/datasets/entire-country-datasets/poland/pl-2023-10-18](https://builtwith.com/datasets/entire-country-datasets/poland/pl-2023-10-18)).

Graph architecture

We would like to have a single infrastructure that holds all our knowledge of the semantic relationships between Brands and Topics in various taxonomies and languages (including Edge), but we will need a subsequent piece of work to do this for increased efficiency over time. This really only becomes a real problem once our data sources and customer base increase significantly.

Building a sellable graph product

The IHQ Graph is a component and pre-requisite for us to deliver quality topic predictions into our customers. Building a net new product that we sell out of the box for other companies to assign meaning to their data sets would require significant effort and focus change - not just in our delivery teams, but also in our go-to-market strategy and target sales personas.

Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |