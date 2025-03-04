# Overview

### Brainstorming

[Miro Board](https://miro.com/app/board/uXjVKmUXUms=/?moveToWidget=3458764600115103094&cot=14) - Brainstorming only and extended with all other topics for Team D  
[Jira Ideas link](https://intenthq.atlassian.net/browse/IDEA-78)



# Problem and Goal

## Problems Overview

Our current sales cycles extend from 4 to 6 months, largely due to legal and technical challenges. We’ve detected three main problems:

- Many large potential clients don’t want to **share their sensitive data** with us and the CMO has to spend lots of political capital with IT, security, legal, privacy...
- Our current Lift offering lacks standardization and documentation for **data integration**. For each client, we are implementing custom, manual solutions, which adds time and requires extensive back-and-forth communication.
- Our current Lift offering lacks standardization and documentation for **deployment and implementation**, making the process of deploying it ad-hoc and difficult unless it’s in Intent HQ’s premises.

This lack of standardized guidance leads to numerous additional meetings to define technical details, increasing the effort on client side and slowing down the process significantly. It also erodes client trust, as we are unable to provide a consistent, well-documented implementation approach, further extending the sales cycle.

## Goals / Value - WIP

The primary goal is to reduce the "time to money" by decreasing the time and the legal and technical friction faced during the sales negotiations of **Lift**.

### Value

This will help shorten the sales cycle by reducing the legal and technical hurdles, increase client trust, and ultimately improve the rate of conversion from prospects to closed deals.

### Potential Metrics

- Shortened sales cycle with any upcoming clients in the upcoming months resulting from
  - Clear data integration requirements
  - Clear instructions to deploy on-prem



# Appetite

6 weeks



# Solution

To achieve the outlined goals, the following solution will be implemented:

## Insights Catalog

We’ll create a standard insights catalog that lists all possible insights available within Insights Explorer. Clients can refer to this catalog to understand what insights they can select and the data they need to provide to enable them.

The catalog will consist of the following:

1. **Standard Configuration**

Thanks to it, neither clients or client services will need to create specific configuration for their Insights Explorer. It will just a matter of selecting from a default set of insights. That also means, we’ll offer a way for clients to select what insights (from this a predefined list) they want to enable.

1. **Insights Documentation**

This documentation will guide them through:

  - what each insight is and means,
  - what data is necessary to display it,
  - what schema and format is needed, and
  - how to provide and QA a new data set

### Out of scope

- UI for selecting the insights. For now, it will be just a file in the client-config repo
- If we need to provide example files with the selected insights, then we'll for now still manually create the files (or use a gpt?)

## On-Premises Deployment

In order to reduce the friction to have access to the data, we are proposing an architecture that enables Insights Explorer in the client’s environment:

- Draft architectural diagram here that will need to be “productionised”



- We will consider clients that already have Databricks. We see this not as a requirement, but as as an enabler, because it can give trust about data sharing...

This deployment architecture will come with some detailed documentation that outlines how to deploy Insights Explorer within a client’s environment, focusing on:

  - Step-by-step instructions for spinning up the tool
  - During this process, we’ll also detect any possible areas of improvement to speed up the integration and make it easier. Anything that can be automated, defaulted, etc. should be listed for future iterations.

### Out of scope

- Simplifying deployment packages (e.g., Docker images) to make documentation and implementation easier
- Simplify data provisioning before writing documentation about how to get data into our platform



Done reading? Click here. → Aaron Schick

Aaron Schick I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |