### Delivered insights package for internal use (goal 1) and decided to have the EIS integration goal as part of a separate initiative with its own priority - see [here](https://coda.io/d/_d5hIdONEiOD/_suPKm). See more about the functionality enabled in the sprint review recording [here](https://intenthq.zoom.us/rec/play/GkPFHNlopSwh4mGK5PpjUCgQU3XvvtqGyQrjEnu3J3GXO1EXceqkhxdmzmBssczLbhpwPjg49U2bE-5u.zUIeMvmo9239ZMKb?canPlayFromShare=true&from=my_recording&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fintenthq.zoom.us%2Frec%2Fshare%2F7GPyoLL7ceOfH5CucI22gO_yIizfO_W1Px3hc6gHka7NCkDZ6YSJTMbP_5zBEIHC.OtbMlkuBMLklBZAB).

# Background

Client data scientists have leveraged behavioural insights (e.g. churn features), we have provided, for downstream modelling and analytics. These insights have been proven to improve their models performance and as such generate additional ROI.

## Current State

The way we currently provide client data scientists and analysts access to these insights is through a regular transfer of our modelled outputs from IHQ cloud, back to client’s  infrastructure (As of today this is a bespoke implementation for Verizon). After the data lands in the location (hive table in the case of Verizon), it is then picked up by client’s data processing pipelines to move it into Enterprise Data Warehouse (EDW), where they get used by client’s data scientists.



# Problem

There are challenges and bottlenecks with the current approach

1. The interface through which we currently provide access to these insights is not data science or analyst-friendly. This leads to internal client teams building pipelines and shipping the data from the location where we land the insights to a location where they can access it from and in a format that is desirable to them. This adds latency to the process affecting how quickly the client can get value from the insights we provide, and the value of those insights as they become out of date. 
2. As a data scientist or analyst, I currently have no means of accessing up to date information about the modelling approaches used to produce these insights. Providing such information will build trust and encourage the wider use of the insights we deliver. It can also help data scientists and analysts discover more insights that may be useful for their use case.

The above two problems lead to a poor user experience for data scientists using the insights we produce.

# Appetite

We create incredibly powerful behavioural insights at Intent HQ, however our inability to easily surface the value of our behavioural insights to new and existing customers is limiting the reach of these products. 

The proposal is to work in 2 phases of deliverables, which would take 6 weeks in total.

**Phase 1: 3 Weeks (****[R & D Mode](https://basecamp.com/shapeup/2.3-chapter-09#rd-mode)****)**

In the first phase, we enable internal IHQ data scientists to use the `ihq-datasets` package to self-serve insights for their workloads. 

This phase focuses on enhancing the accessibility of the insights we generate. It achieves this by providing our internal data scientists with a streamlined interface through our Python package, allowing them to easily access insights.

~~**Phase 2: 3 Weeks**~~

~~In the second phase, we integrate our insights into Enterprise Insights Store so that our data scientists can do the following:~~

1. ~~Step 1: Discover what insights are available~~ 
2. ~~Step 2: Find information about insights to help them decide if they may be appropriate for their use case~~  
3. ~~Step 3: Get clear and easy instructions on how to use these insights~~

Phase 2 has been deprioritised - subject to prioritisation in the Insights Store team.

# Solution

We do the following:

1. **Generate insights (which have already been implemented)** 
   1. Insights like predictive brands and behaviour embeddings through the inference engine.
   2. Other insights like the Inferred Age, Inferred Gender, Brands, Interests and Churn through our BAU process.
2. ~~**Register the Insights with Insights Store**~~~~, so that we can keep the insights up to date in terms of documentation.~~
3. ~~**Provide an interface**~~ ~~to these insights in the form of a python package~~ `~~ihq-insights~~` ~~or~~ `~~ihq-datasets~~`~~, so that internal data scientists can start using our ML platform to access insights available.~~



The `ihq_insights` library will provide the following interfaces:

- API to fetch insights and make them available as a (spark) dataframe
- API to display metadata information about the dataset
- Instance profile / service account based authentication and authorisation of requests

What will not be supported by the library

- API to register insights new or update old insights
- API to list all available insights
- Role based Access Control (RBAC) for these datasets

### Integration with Enterprise Insights Store

Enterprise insights store is built in such a way that it is interoperable with Git and can render Markdowns in a repository. The proposal for integration is to use Github as the source of truth for all documentation of the insights we produce and Enterprise Insights Store could render markdown’s from this repository.

This method of integration will allow internal and external data scientists in the future to produce documentation about the insights they produce which sit along side the code they write. This enables them to keep documentation up to date with every release as documentation is treated as code.

For internal Insights, which we would like to make available as part of this development effort, we would like to do the following

- Create a Github repository with each folder in the repository having a [README.md](README.md) file which holds the documentation for the insights we produce. 
- Each insight would have been documented using the following template







- Register the insights with enterprise insights store by making an API call or have a form which can be filled out by anyone willing to share the insight



## Scope for 6 weeks iteration:

1. Generate insights for the month of March (Part of the BAU process)

  - Modelled Brands
  - Behavioural Embeddings
  - Inferred Age
  - Inferred Gender
  - Brands
  - Interests
  - Churn

1. Update documentation for each of these insights and associated models, so that data scientists can make informed decision about, whether they could use these insights for their use cases.
2. Register these insights with Enterprise Insights Store backend (this ties in with the work which would in parallel [here](https://coda.io/d/_d5hIdONEiOD/_suPKm)). This should help understand what insights are available and what value each of those insights offers.
3. Release a package `ihq-insights` or `ihq-datasets` so that data scientists can start using these insights for their use cases. This package will allow querying of insights which are already inferred (It does not on-demand query the model running in the inference engine)
4. We socialise this with our DS colleagues internally so that they can start using the insights produced through the interface we designed

Towards the end of this iteration, we will collect feedback from internal data scientists so that we can improve their experience prior to making this available for external data scientists.

## Good to have: (Stretch Goal):

Display a sample of the insights dataset and its metadata so that data scientists and data analysts get a feel of how the data looks.

## Rabbit Holes

We acknowledge that we have to support clients who will be willing to run our products on other clouds like GCP or Azure. Making the python package cloud agnostic is outside the scope for this iteration. However, we will keep in mind of these requirements in the choices we make.

## De-Scoped

Though we can enable a data scientist to try out the model endpoint live by providing a few examples and retrieving the results back, it's out of the scope of this iteration because of the following rationale:

- Data scientists would like to use insights in a online manner.
- We can provide a feel for this data by displacing the insights as a table, as mentioned in the good-to-have section.
- We do not fully understand if Data Scientists have the appetite to use an online inferencing endpoint, however, there could a few use cases where this could be quite appealing for Marketers and integrations with other marketing systems.

## Expected Outcomes

- We have generated, catalogued, and documented our current insights.
- These insights are made available for internal data scientists to explore and access through the Enterprise Insights Store.
- When a data scientist or analyst wants to make use of the insights, they have clear instructions on how to use those insights for their use cases.
- We have this available for the sales and product team to showcase the potential to our clients.

## Benefits of providing access to insights through a python package

1) Data scientists and analysts can access the insights using Python which is the defacto industry standard for data science and analysis. 

2) Access is self serve meaning that we are dispensing with the pipelines for delivering insights  that are currently serviced by internal and client teams. 

3) Access is immediate with users able to discover, access and then leverage insights within a matter of minutes. 

# Anticipated Future Work

- This could lead to the first version of the Enterprise Insights store for Verizon, where we can deploy it on GCP for their data scientists to start consuming the insights we produce today for their use cases.
- This would lead to the initial version of the Enterprise Agent, which could enable insight-sharing through one of the insight-sharing patterns.



Done reading? Click here. → Mark Bunn, Daria Barbalata, Jonathan Lakin

Mark Bunn, Daria Barbalata, Jonathan Lakin I’m aligned with the problems & goals.

 I’m not aligned

 I’m aligned with the problem but not the solution.



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false | Though I understand and agree with the problem and solution, I have a concern that Verizon wouldn’t allow a migration from Omega for accessing insights and that there’s a considerable risk that:<br/><br/>We would have to maintain both indefinitely<br/>Lack of use of EIS<br/><br/>Anything we can do (or that has already been done) to mitigate this risk? | Daria Barbalata |  |  |
| false | I have the feeling we are trying to solve two different problems and I think we may want to split them in different shape docs.<br/><br/>The first one is about documenting the current insights and offering them through the EIS for better discoverability.<br/>The second one is about offering a library for easy access to those insights. | Albert Pastrana |  |  |