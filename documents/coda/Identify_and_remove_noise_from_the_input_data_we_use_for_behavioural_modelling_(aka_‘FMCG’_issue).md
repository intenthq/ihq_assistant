### Pipelines are done and tested. Getting ready to actually decommission Scylla.

# Background

OPEX of running our platform has been exceeding $220,000 as of Dec 2023. In Q1 we were able to bring this cost down to $190,000 due to significant storage optimisations on the data lake. However to bring the cost down to desired levels (i.e under $160,000) by the end of June, we would need to optimise other areas of the infrastructure like the compute we use and the licenses we pay which brings our focus on to Scylla and the way we compute profiles

[#0306 Reduce Verizon AWS costs v2: Databricks / Next Gen ](https://intenthq.atlassian.net/browse/IHPI-39)

**More detailed info here:**

[https://coda.io/d/VZ-Program-tracker_dW5sVG1DlPv/AWS-Costs_su8Zg#Cost-Initiatives_tuiUJ/r5](https://coda.io/d/VZ-Program-tracker_dW5sVG1DlPv/AWS-Costs_su8Zg#Cost-Initiatives_tuiUJ/r5)

## Current State



We make use of Scylla as the source of data for pipelines which produce profiles, that can then be ingested into Insight’s Explorer’s persistence (OpenSearch). The current profile creating process makes use of a distributed profile processing pipeline which makes use of Kafka and a custom DSL to achieve this.

# Problem

Scylla costs roughly ~$23k/Month (after Tech-Ops migrating it to Kubernetes. It was ~37k/Month prior to the migration) on an average to operate for Verizon. Along with this operational cost we spend an additional $150k in license every year which is due to expire in March 2025.

# Appetite

- 6 Weeks
- Blend360 2x engineers coordinated by Eddie (30% capacity)

# Solution



Here the `Data Elements` pipeline refers to the new build which will replace the existing pipeline which uses our Data Lake as the source to produce profiles



Technical stack includes Spark and Databricks and removing dependency on Scylla

### A Strategic way of composing pipelines



We would like to build these pipelines in such as way that we can compose new pipelines in the future easily and swiftly. At a high level, this means, we would like to build a bag of transforms which when put together become a Job, Jobs when put together become a pipeline and pipelines put together end up as Data Products.

## Rabbit Holes

- The goal is to migrate only the data elements which are essential to support our data to day operations of testing and interacting with our products, but not to migrate all the 200+ data elements which are currently in insights explorer
  - [https://coda.io/d/_d5hIdONEiOD/_sukDx#_luIO5](https://coda.io/d/_d5hIdONEiOD/_sukDx#_luIO5) 

# Outcomes

- Replace the existing pipeline while respecting the contract exposed by Insights Explorer
- By achieving the above, we would have reduced the overall cost of operating the pipeline which comes from decommissioning Scylla database and avoiding license renewal in March 2025. This would save us roughly ~$23k/Month in cloud OPEX, ~$150k license fee every year and ~$25k/Year in operations cost (~$100k in 2024,  ~$450k in 2025)
- Our platform's architecture would be simplified and would improve maintainability of the system
- Potential for repeatability for new clients



Done reading? Click here. → Daria Barbalata

Daria Barbalata I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Answer | Vote | Notes |
| --- | --- | --- | --- | --- | --- |
| false |  | Kumutha Swampillai |  |  |  |
| false | Concerned of dependencies and making sure we get all teams involved as and when needed - anything we can already foresee? | Daria Barbalata |  |  |  |
| false | Furthermore - looking at the appetite and the fact we haven’t started this yet vs. the cost reduction deadline for Verizon, how confident are we that we can reach that deadline? | Daria Barbalata |  |  |  |
| false | Should the engineering PoC for IE without config be considered here? [https://intent.slack.com/archives/C064KUGTDMH/p1711448702188109](https://intent.slack.com/archives/C064KUGTDMH/p1711448702188109) | Daria Barbalata |  |  |  |