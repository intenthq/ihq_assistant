# Background

We have started development of new topics that use our VAE embeddings - the same underlying model used for modelled brands - more detail about the motivation and value behind that [here](https://coda.io/d/_d5hIdONEiOD/_suY3M). We believe the modelling approach tested above to be quite limited and there is more work to leverage the full power of VAEs in topic modelling.

As the sales pipeline progresses more Lift customers, we are taking this opportunity to future-proof our topic deployment into a new customer (e.g. MTN Nigeria) leveraging the work that has been done to generate behavioural embeddings from user-domain interaction data and the current work to create a knowledge graph that stores our semantic knowledge of domains.

From a previous round of topic modelling experiments:

- In the [first phase](https://coda.io/d/_dK5h4iVEEUo/_sutfh#_lu93o), we demonstrated the **viability of embeddings-based approaches** with a simple mapping-based prototype
- In the [second phase](https://coda.io/d/_dK5h4iVEEUo/_subPz#_lugCU), we built a **tree-based topic model** directly utilising the brand embeddings, **improving on the first prototype** for the existing evaluation criteria
- We identified challenges in topic **evaluation** and prepared a [roadmap for future work](https://coda.io/d/_dK5h4iVEEUo/_sunev#_luMBJ).
- We generated and uploaded **model outputs** for a randomised sample of 100k users to the canary dashboard.

Now considering a new goal more focused on speed of deployment across new and existing customers, we are exploring the above as well as other ideas workshopped (see team ideation subpage) to test and choose the most efficient approach for the future shape of our topic insights.

As a **solutions architect**, when I **plan onboarding** for late-stage prospects, I want to be able to confidently promise **quick delivery of topic insights** derived from **1st party weblog data**.

# Problem

- We don’t have a clearly documented process for how we should deliver topic insights to a new customer;
- We do not have a clear evaluation framework to assess the quality of our topic insights;
- Each topic volume is highly VZ specific and fixed;
  - We expect stability over time with topics and treat all of them equally though we conceptually a different level of affinity over time for topics such as philosophy that may be a strong signature of someone’s personality vs. ones that are more likely to change over time like fitness.
- We have a large number of topics we’re segmenting users into, but some aren’t used while others are duplicated with slightly different and confusing names that are customer specific (e.g. Discounts & allowances vs. bargain hunters). 
  - We also don’t have a clear definition of the meaning of each topics leaving these highly prone to interpretation.
- Topic mapping is very limited (our knowledge of data and/or brands that map into topics). Current solution strongly depends on topic mapping. More detail about this [here](https://coda.io/d/Data-Science-and-ML-Eng_dK5h4iVEEUo/Interests-does-low-coverage-matter_su7Ftr3A#_lufA0sao).
- Current model configuration is only able to capture basic lineal patterns.
  - No knowledge retain across time. Every month the model learns from scratch each user interests.

### Goals & Success

1. Define, standardise and implement a topic evaluation pipeline to be used in the subsequent implementation in production and future research projects.
2. Build experimental tool to automatically label new domains to brands and topics.
3. Choose subset of *Intent Topics* with clear definitions.
4. Choose the modelling and  (sizing) approach, produce topics for UAT using Verizon data and collaborate with stakeholders to approve.
5. Prepare code for initial implementation and productisation into a first customer (e.g. MTN Nigeria).

### Non-goals

- Implementing and orchestrating a new topic insight delivery pipeline. This will have to be addressed once we’ve chosen the most efficient approach;
- Delivering new topic insights to a new or existing customers; 
- Packaging and deploying the new model under customer infrastructure;
- Implementing continuous data labelling - will need to be a subsequent iteration to productise the component within the Intent Graph once we’ve validated an approach.

### Risks & Rabbit holes

- Evaluation can be a never-ending problem especially considering how subjective the ground truth is. But - similar to brands - we will make some decisions that correlate with internal user approval and aim for simplification and standardisation.
- Sizing has been a controversial topic and can cause delays unless we’re able to make a choice on a solution that’s both trustworthy and easy to implement and maintain. We are thinking of using an external validation data source but that has its risks to be thought through and considered vs. other options.

# Solution

1. Define topic evaluation - whatever method we use for generating topic insights, it’s important that we can measure the efficacy of, especially when delivering such insights for the first time with a new customer.
2. Build a tool to automatically label domains (and other interaction data in the future) into brands and topics. We could leverage an LLM for this and need to collaborate with Igor who has done a lot of thinking into a potential solution.
   1. The more ground truth we have, the better we can be at inferring the kind topic users may be interested in and also use for evaluation.
   2. This would also heavily connect this stream with the Intent Graph work which is natural since any downstream process would rely on this semantic layer and any solution built here will need to be integrated into the Intent Graph architecture, ideally for continuous updating as new data comes through.
   3. We should define our core subset of Intent topics that we start from with any new customer. These should link or match Novatiq’s version of the IAB taxonomy in order to ensure seamless integration with them as the need arises to onboard common customers.
3. Experiment with vector searches for clustering users into topics based on user behavioural similarity derived from interaction with brands (VAE model).
   1. This is a research and innovation stream and it should be evaluated (using 1) against traditional BAU methods. 
      1. If successful, we should continue with implementation and productisation. This effort will likely take much longer than simply optimising our current approach, but we believe it will have many other downstream benefits such as:
         1. Reducing our training needs for producing core behavioural insights. This is not also a time-save, but also streamlines and simplifies our pipelines and  ensures better traceability along the e2e refresh process.
         2. Could be re-used as a method for lookalike modelling, seed optimisation and even tested for other models like inferred age and gender.
         3. Would be easier to deploy under customer infrastructures without the need for a confidential AI packaging. These would simply be vector features that we could generate on our side and transfer to the customer infra for IE to query and derive the necessary insight. More useful for future lookalike improvements than specifically topic insight delivery, but worth considering as a secondary benefit of the approach.
      2. If not, however, we should rely on previous work done to unify our existing interest modelling methodology. Here we might need to do a little more code optimisation, but should largely be a smaller piece of work. We believe it’s not worth investing effort here until we’ve invalidated i). Having not signed a new customer yet + the phased sales approach where topics are part of phase 3 (?), we believe we could tackle this - if needed - upon signing and prioritise i) in the meantime.

Along developing the above, we are also considering creating a few artefacts that will be highly valuable for pre-sales and onboarding processes:

- Document the model, data flow and required process for delivery;
- Create data contracts;
- Consider current topic allocation (sizing) challenges & develop in a way in which we have a clear sizing methodology (e.g. same as brand sizing?)

### Appendix

[https://doordash.engineering/2020/08/28/overcome-the-cold-start-problem-in-menu-item-tagging/](https://doordash.engineering/2020/08/28/overcome-the-cold-start-problem-in-menu-item-tagging/)

What is quick enough?

What do we define as topic insight? Does it matter if it’s mapped, descriptive or predictive?

What do we want to **learn**?

- hypothesis
- when to stop - aim to falsify rather than validate

How will we **measure** it?

Then what do we **build**? 

DS objective: capability

- problem that the model is re-trained every month and we cannot track the way people’s interest are changing over time
- We wouln’t be able to iterate for better performance over time if we didn’t address the modelling paradigm first

To do: define subset of focus topics that are useful cross-customer + topic definitions + agreement with stakeholders.

Survey to measure? [https://docs.google.com/presentation/d/1mCOfqpREhyoNbbAfRElEymHbgdur9_PxyB1gq4uXw3Y/edit#slide=id.g93d7020066_3_1227](https://docs.google.com/presentation/d/1mCOfqpREhyoNbbAfRElEymHbgdur9_PxyB1gq4uXw3Y/edit#slide=id.g93d7020066_3_1227)

**Tracking**

- JIRA:  
[https://intenthq.atlassian.net/browse/AIPROD-1322](https://intenthq.atlassian.net/browse/AIPROD-1322)  

- Product Roadmap: [https://coda.io/d/Product-Management_dgMDDph8PXa/2024-Outcome-Based-Roadmap_suomY#Current-period-view-of-roadmap_tu3a0/r16&view=modal](https://coda.io/d/Product-Management_dgMDDph8PXa/2024-Outcome-Based-Roadmap_suomY#Current-period-view-of-roadmap_tu3a0/r16&view=modal)





Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution





# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Answer | Answerer | Vote | Notes |
| --- | --- | --- | --- | --- | --- | --- |