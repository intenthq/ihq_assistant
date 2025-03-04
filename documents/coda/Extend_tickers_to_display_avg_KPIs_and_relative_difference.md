# Overview

This pitch is a part of the [https://coda.io/d/_d5hIdONEiOD/_suST-](https://coda.io/d/_d5hIdONEiOD/_suST-) work, however, as this change will affect overall IE functionalities, we saw it best to open a separate document for clearer documentation and transparency. 

The current logic of Insight Explorer cards cannot display transaction-centric data from Fintonic as it does in Domo, supporting only user-centric data. To address this, IE needs to support distinct count and sum aggregations for transaction-centric data, which are currently unavailable. Adding these aggregations to the cards logic will enable displaying Transactional data, supporting the transition from Domo, enabling MXP demoing in IE and supporting IE cards to cover new use cases.

# Problem

The current logic of Insight Explorer (IE) cards does not allow the display of transaction-centric data from Fintonic as it is shown in Domo. 

Based on what we currently have in the MXP in Domo we need to support the following:

1. Ability to show the number of users for behavioural data (Orange) - ✅ Already supported in IE
2. Ability to show the number of users for transactional data (Fintonic) - eg.: Age, Province, etc. - 🔴 Not yet supported in IE
3. Ability to show the sum of spent for transactional data (Fintonic) - eg.: Brand, Purchasing channel, etc. - 🔴 Not yet supported in IE

Currently, we support 1 but not 2 and 3.

From a technical perspective, this is because IE supports only Count for the cards, but not Distinct Count or Sum aggregations, which are necessary for displaying the number of users or the sum of transactions from Fintonic data. Instead, it shows the number of triplets matching the criteria that is currently uninformative to users. (Triplets are the records/rows of data we get from Fintonic grouped by user, month, and brand)

For example: 



*✏️ Note: The above logic is only related to the cards and it is different for the tickers in the IE for which we already support other types of aggregations (cardinality, sum, avg).*

## **Why Now**

Without this piece of work, we won’t be able to display Transactional data (eg.: expenditure, age, brand, etc.) in the IE and continue with decommissioning Domo for which we need to get the MXP into a marketable state by the end of June latest. 

## Target Audience

- IHQ Sales Team
- External Sales representatives
- Prospective MXP Clients
- Client Success team

## Goals and Success Metrics

### Goal

Enable demoing the Market Explorers in IE with both transaction-centric and user-centric data including all cards mentioned in the scope of the [https://coda.io/d/_d5hIdONEiOD/_suST-](https://coda.io/d/_d5hIdONEiOD/_suST-) 

### Success Metrics

- Demo environment stability - TBD - No more Domo downtimes
- Gain control over reports and features 
- Increased pilot requests - TBD - Ideally get more traction after the demos by delivering more value with the additional IE features



# Appetite

This will be included in the cooldown of the [https://coda.io/d/_d5hIdONEiOD/_suST-](https://coda.io/d/_d5hIdONEiOD/_suST-) which will likely have to be extended into the first week of June

Appetite: 2 weeks



# Solution

We’ve decided to add support for cardinality and sum aggregations for all cards. This will allow data managers to configure any card to show either the count (current behaviour), sum (like the spent for each transaction), or cardinality (that is, a distinct count of users or any other field if needed).  
This is a relatively simple solution (1-2 weeks) that doesn’t require new data or indices or indexing the data differently and it will still support filtering transactions by date.

## Risks & Drawbacks of the solution

The only drawback of this solution is that the [cardinality aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/8.9/search-aggregations-metrics-cardinality-aggregation.html) (i.e. the distinct count) doesn’t show exact results and can be accurate only within a precision threshold. We don’t foresee this being a big problem or a blocker because we are showing the data in aggregated form, and people will be comparing percentages, not specific numbers. In fact, people are seeing just a sample of the data (all users that have Fintonic) so it’s already an approximation.

## Benefit of the solution

- Unblocks the migrating MXP from Domo to IE
- Adds valuable functionality to IE cards for existing and prospective clients 

Besides unblocking the transition of MXP to the IE platform, this piece of work will add a functionality in Insights Explorer that we think may add value to other clients (existing and prospect). As an example, in the Verizon world, we could add now some cards at the account level if we want to, among other possibilities.



# Feedback

Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |