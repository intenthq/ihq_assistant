### Drafting solution

# Overview

The Intent Graph is a knowledge-base storing the relationships between data (currently domains, but could extend to other interaction or transaction data types in the future) and our brands and topics insights. 

This knowledge-base has been collected over time as needed in an effort to deliver these insights to our customers, but it has typically been a one-off exercise with seldom updates where it was deemed necessary for optimising the quality of our insights.

Therefore, this knowledge-base is static and we need to go through bespoke and manual effort to update this, especially when onboarding new customers. 

### Current state

From our initial analysis of the domain coverage we currently have for Nigerian domains - see analysis here

- We have brand knowledge for 31.79% of the top used 9K domains in Nigeria as provided by Semrush. 
- Of the brand-matched domains, 23% have an associated topic, resulting in an overall topic coverage of 8.7%.

A real, more robust data set is likely to contain many more local domains that don’t make the cut for Semrush’s top 9K most used (Approximately 5% of the 9,000 domains are Nigerian-specific) and - given our current hierarchy was compiled from US, UK and Spanish data sets - the overall coverage is likely to be significantly lower than what we saw above.

This could provide sufficient value for an initial PoC delivery, especially for customers that have never leveraged their weblogs before, but would need to be increased significantly over time to demonstrate richness of insights and ensure we meet customer expectations.

# Problem

### Problem overview

Our knowledge of the data indicative of interest in brands and topics is static and its current version is insufficient to provide rich and granular enough behavioural profiles for new customers.

The existing Intent Graph knowledge-base does not have the ability to capture the latest market trends.

Considering we use this to evaluate our models (we measure precision and recall for our predictions against future interactions), we are missing a lot of behavioural interaction data which could help us gain a more complete picture of our models’ performance.

### Target Audience

- Intent data professionals using the Intent Graph for downstream modelling.
- New Lift customers that bought our brands and topic insights.

# Appetite

### Goals & Success

1. Given a new domain that doesn’t exist in the Intent Graph, we need to find the Brand it represents if applicable. Additionally, we should also store other website metadata for future use
   1. This creates a requirement for the Intent Graph as well - that it’s able to ‘tell’ the learner if a domain is already mapped in the Graph or not. The Learner should only run, if the domain isn’t already mapped?
2. Given a new domain that doesn’t exist in the Intent Graph and its metadata (website description), we need to find the Topic that it fits in with best from our available Intent Topics.
   1. This also creates another Intent Graph requirement on top of the above - to store topic definitions and provide input information for the learner to be able to correctly categorise the domain based on our rules.
   2. Consider semantic embeddings for a richer representation of the meaning of the domain.
3. We have seen some domains to be too general for them to give a good indication of an interest (e.g. [apple.com](apple.com)); the solution here should ensure that we don’t map everything into topics, but only when they indicate towards a specific interest in a topic. See more [here](https://coda.io/d/_dK5h4iVEEUo/Maintaining-the-graph_su5Dc2dP#_luP2PC0u).
   1. Furthermore, it’s likely that some domains have a stronger correlation with a topic compared to others - we should be able to provide some indication of the strength of the relationship between the domain and the topic.
   2. This also results in a requirement for the Intent Graph to store this information, not just the link between the domains and other entities.
   3. The graph should also store this information - that a domain shouldn’t be mapped - so that the next time it comes up it doesn’t go forward to the mapping process.
4. Some domains are sensitive in nature and we shouldn’t use in our insight creation at all (religion, race, ethnicity, gender, sexual orientation, porn, disability). The solution should also ensure that such domains are detected and not used downstream.
   1. We should however, store these domains in the Graph in some sort of blocklist to ensure that the next time it comes up it doesn’t go forward to the mapping process. 
   2. Maybe the learner just map to the sensitive topic, but it’s the Graph’s responsibility to not use these downstream. What about domains that map to a usable topic but they’re sensitive in nature?
      1. Graph requirement for another metadata stored about the domain to flag it’s sensitive/blocklisted. Might be stored with a different tag in the same place as for no. 3 above. 
      2. Given these have really sensitive ethical debates around them, we should design a mechanism for humans to review domains that are labelled into sensitive topics.
      3. This would rather be a second iteration.
3. For both 3&4, we need a mechanism of manual verification for *high risk* mappings where someone gets a request to approve such mappings before they make it into the base graph.
4. Learner(s) should be deployable artifacts. Likely part of productising which will be a subsequent iteration.

To turn this into a requirements doc for the Graph development

### Non-goals

1. Adding other types of behavioural data into the Graph - though the solution should be designed in a data agnostic way so that it can be further leveraged and enhanced for a non-domain implementation.

### Risks & Rabbit holes

Accuracy - what is our appetite for error here?

Manual curation process - perhaps some things we define as high risk and we send to a manual curator to check? Who? When? How do we define high-risk?

# Solution

[Solution Miro](https://miro.com/app/board/uXjVLZem8l8=/?moveToWidget=3458764602990508839&cot=14) - to be summarised here [Sebastian Martins](mailto:sebastian.martins@intenthq.com) 

Topics [here](https://docs.google.com/spreadsheets/d/1xezqoUHgNI2yqNvd4o_N1vyC-a7pVlE3rxDjLf8LOJU/edit?gid=1535489501#gid=1535489501) + [loom](https://www.loom.com/share/94a0d181b7004c9d8c17ef1fc21ce050) explainer of the spreadsheet

How do we measure accuracy?

- We could use wiki data labels for validation;
- We could use our existing labels as ground truth for validation;
- Multiple people & intersection of labels?
- Multiple LLMs & intersection of labels?
- What else...?

What to do:

- Integrate and test existing PoCs
  - [site2brand](https://github.com/intenthq/site2brand/) that maps a given domain to a brand or topic - P1
    - Get Nigerian sample domains - we already have a sample of a day of browsing from them aggregated at hourly level. [Georgia Harrison](mailto:georgia.harrison@intenthq.com) to take PoC from [Igor Perchersky](mailto:igor.pechersky@intenthq.com) and upgrade :)  
    - To think if it’s the same tool that covers both brands and topic mapping;
    - Evaluation for both brands and topic mapping;
    - Notably we’ll need API keys for Serper and OpenAI.
  - Integration here means integrating with learners, not productization.
    - Specifically compatibility with certain tooling we use.
  - [WebHostHarvester](https://github.com/intenthq/WebHostHarvester) that finds domains for a given location and focus topic - P2
    - Perhaps focus to priority topics (We have a subset of ~200 - [Daria Barbalata](mailto:daria.barbalata@intenthq.com) to share spreadsheet)
      - an example output - [794 hostnames for “Nigeria:Sport”](https://docs.google.com/spreadsheets/d/1qIjQ1xJOFJyycGGx4eyJJpH7nHeyhC8q03VVN-6moR4/edit?gid=1586105205#gid=1586105205)



Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Answer | Answerer | Vote | Notes |
| --- | --- | --- | --- | --- | --- | --- |