# Background

As part of the BAU Pipelines which run on a monthly basis to cleanse, aggregate and generate insights we have been using AWS’s Elastic Map Reduce (EMR) service to execute our Spark jobs. We have faced multiple issues with EMR’s ability to run our jobs reliably and at the performance levels we expect to operate it in. This lead to a spike in Q4 2023, where we used Databricks to execute our jobs, which proved to help with maintainability, operability and reliability of these jobs while reducing the overall OPEX of the BAU process.

Jira: [https://intenthq.atlassian.net/browse/IHPI-39](https://intenthq.atlassian.net/browse/IHPI-39)

## Current State

Our Data processing Environment:

- Spark as the distributed data processing framework
- Airflow for Orchestration
- EMR as the infrastructure choice for processing data

# Problem

We have been encountering issues with EMR which have been directly impacting the reliability of jobs due to the intermittent failures, these failures lead to a very tedious troubleshooting process because there isn’t an elegant solution in place to search for the root cause thereby leading to longer troubleshooting and maintenance windows. All of this leads to greater OPEX costs, and man hours lost from strategic product development.

# Appetite

6 Weeks

# Solution

We will be able to do the following:

- Migrate Jobs to Databricks Prod
- Orchestrate them using Airflow
- Execute a parallel run with current BAU process and perform QA
- Deprecate the old pipeline
- Execute this new pipeline from the Month of May

## Outcome

- Efficient and Reliable BAU insight generation
  - Faster execution of jobs, leading to pipeline finishing early and hence our customers can get access to the insights sooner
  - Utilises lesser compute and will reduce compute costs
  - Both these points will help us run refreshes more frequently if need be
  - High confidence in meeting our SLAs with our clients
- Easy to operate, hence freeing up capacity for strategic product development
- The above two lead towards, reduced OPEX





Done reading? Click here. → Daria Barbalata, Albert Pastrana

Daria Barbalata, Albert Pastrana I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false | While typically we should stick to the 6 week window, I think this is one that we need to complete - we probably can’t migrate only half the jobs :) That said, are we sure it’s going to fit within 6 weeks or should we manage expectations for longer periods of time? | Daria Barbalata |  |  |