The Product Team are choosing to write our Shape Up cycle goals in the form of OKRs:

**Who does what by how much?**

- **Who** is the user (or users) we are targeting with this next release?
- **What** do we want them to do more or less in the immediate future?
- And, by **how much** do we want to see their behaviour change?

Although as a business we may not be able to quantify and then track the metrics part effectively right now, it’s good practice to write these down with the aim of solving for them at a later date.

## **Example**

A well written OKR statement should clearly answer all of those questions.

For example, *we want our existing customers* ***[who]*** *to reduce online store visits for recurring product orders* ***[does what]*** *by 50%* ***[by how much]*** *while maintaining* ***[by how much]*** *their average monthly spend* ***[does what]*** *with us*. 

## **Notes**

### We will not manage to build solutions for all these Goals. So, we need to agree **which** goals are the most important for Product to focus on.

### This list **does not** include tech features

### New customer deals **will** disrupt what we can achieve in Nov/Dec 

### We are possibly missing something

### This is **not** a plan

Let’s discuss...

## **IHQ Longterm Goal Hierarchy**

**Reduce time to revenue by...**

Enable customers to onboard quickly by reducing bespoke work. Working towards the product being *rinse and repeat*

  - Predictive Topics leveraging the new VAE model (DS)

Give customers a coherent end to end experience by bringing together the existing components together

  - Edge-Lift integration

Enable customers to discover and buy new products by themselves

Enable customers to easily discover the true value of the product

Increase the conversion rate of Edge pilots

iOS Insights  
CMS Funnel

**Open new revenue streams by...**

Building new IP that is highly valuable to customers

  - Pre-trained brands model (DS)
  - Intent Graph (MLE)

**Retain existing revenue by...**

Deliver audiences that meet customer needs

Saving costs

Increasing the quality of insights

  - Identify noise in weblog data (ADS)

Reducing the time and cost of delivering recurring insights

  - Reduce Brands Refresh Opex (MLE)
  - Reduce AWS cost (MLE)
  - Faster Lookalike Audiences (DS)
  - Generating the right audience seeds (DS)



## Customer ROI Enhancements (Team A)

*Currently covered mostly by team B aka AI Products*

### Identify and remove noise in weblog data (time box)

[Already started in Sep/Oct] We want **data analysts and campaign managers** (currently at VZ) that use our brands in Insights Explorer to **access all approved brands**, including certain FMCG and fast food ones that have been hidden to **reduce the impact of ad-tech noise**, and be able to **explore top winners without losing confidence** in our behavioural insights.

- Metrics: 
  - Brands filtered for in IE, both qualitative (what brands are used, are people looking at FMCG ones?) and quantitative (number of brands used in IE)
  -  Campaign results where the audience was defined by brands - clicks?

## Enrich Customer Profiles (Team B)

### ~~Faster Lookalike Audiences (Won’t)~~

[Already started in Sep/Oct] We want **Audience Maker users** (currently Verizon campaign managers) to **access lookalike audiences**  **faster on-prem** (ideally withing 24 hours of request), while maintaining or increasing the current performance of the audiences and **reducing the amount of OPEX required to deliver them.**

- Metrics: 
  - Time to model audience, time to evaluate audience, e2e time between the customer request and the audience being available for them in Insights Explorer.

### ~~Generating the right audience seeds (Won’t)~~

We want to **identify the ideal behavioural profile that matches the customer campaign objective** without requiring **Audience Maker users** to select the right filters to match their objective. Currently x% of seeds match the objective and we should increase that to y.

- Metrics:
  - % of approved audiences out of requests
  - % of seeds that match the objective
  - campaign results.

### Predictive Topics leveraging the new VAE model (MH)

We want to enable **new customers** **accessing modelled topic insights** **within a couple of weeks** of onboarding without requiring a fully new & manual implementation, by updating our current topic modelling methodology to one that uses our latest technology (e.g. deep learning, embeddings) and streamlined modelling architecture (e.g. inference engine).

- Metrics
  - Time to onboard a new customer for topic predictions.

## Build the LBM (Team C)

*Currently covered by team B aka AI Products*

### Pre-trained brands model (SH)

We want to **infer brand insights** for **new customers**, given some behavioural interest info, **in the first week of onboarding** without requiring very rich behavioural data from the customer or wait for us to train a model on their 1st party data if they have it.

- Metrics:
  - Time to onboard a new customer for brand predictions.
  - Number of behavioural data sets that Intent can use to deploy value to all and any customer.

## Explore and Activate Insights (Team D) 

### Lift Light (SaaS) Customer Demo

We want to **increase the success rate** of product demos by empowering potential clients to **enhance their ROI** through optimised audience targeting, leveraging **Causal AI models** that analyse run on CRM data.

- Metrics: 
  - Demo Feedback / Follow-up / trial request
  - New sales attributed to Lift Light

### Easy Integration

We want to **shorten the sales cycle** by offering **seamless integration** workflows and high-quality **documentation**, allowing potential clients to **easily implement** our solution **without** needing to **move their data** from their existing environment.

- Metrics
  - Technical negotiation feedback / Follow-up 
  - Reduced length of sales cycle
  - New sales attributed to easy integration

### Conversational Interaction (formerly NLP)

We want our **potential clients** and **non-technical users** to increase demo-to-pilot / demo-to-sale **conversion rates** while reducing **time-to-value** for new users through the **introduction of Natural Language Processing capabilities** in out platform.

- Metrics: 
  - Demo Feedback / Follow-up / trial request
  - Increased user adoption / retention (CBL?)
  - New sales attributed to NLP

## Rapid and Low Friction Activation (Team E)

**(Long term Goal: Increase the conversion rate of pilots)**

### Private Edge (MH - Sales)

We want our **customers** (specifically legal, compliance, and IT) to be able to **install all Edge supporting components on a private cloud**, so we can have an alternative to SaaS and avoid legal, compliance and privacy complications. 

**Metrics:**

1. Prospects adopting Edge on-premises.
2. Edge sales cycle duration.

### iOS Edge Pro

We want our **customers** to be able to **integrate with Edge Pro on iOS** to avoid the complications of consuming management services from Intent as SaaS so we can have another alternative to SaaS and avoid legal, compliance and privacy complications.

**Metrics:**

1. Prospects using iOS Edge Pro.
2. Edge Pro sales cycle duration.

### iOS Insights (MH)

We want our **customers** to be have a **rich iOS micro-segments offering** so they will gain more value from using the iOS Edge SDK.

**Metrics:**

1. Number of new insights on iOS

### Remote Notifications

We want our **customers** to be able to **engage** with their audience using **remote notifications** so they will be able to engage with them **immediately** and potentially **activate dormant users**.

###  Edge Data into Lift (MH)

We want our **customers** (specifically marketing) to be able to **digest Edge generated data** into their Lift installations so they will be able to generate audiences based on richer attribute sets, and specifically on behavioral and demographic data.

**Metrics:**

1. Customers with Lift adopting Edge.
2. Time to “first audience”
3. Upsells from Lift to Edge and vice versa.

### Lift Campaigns into Edge (SH)

We want our customers (specifically marketing) to be able to export cohorts from Lift into the Edge system so they could take advantage of the engagement capabilities of the Edge system such as best moment to engage, conversion value management, engaging with un-onboarded customers, etc.

**Metrics:**

1. Conversion rates.
2. Upsells from Lift to Edge and vice versa.

### *Note*

There’s no “how much” I could honestly expect right now. We know the sales team have asked for these in various flavours and we’ve seen customers expressing their wishes first-hand.

## Data and Ml Platform (Team F)

*Currently covered mostly by team B aka AI Products*

### Build the Intent Graph (MH)

[Started Sep/Oct] [Acquisition - MTN focus for MVP] We want **new customers** to be able to **access descriptive (not modelled) brand and topic insights** through the Intent Graph **within [2 weeks] of onboarding**.

- Metrics:
  - Time to map new customer data to brands and topics usable downstream (for Insights Explorer ingestion).

### Reduce Brands Refresh Opex

[Already started in Sep/Oct] We want reduce the time **Intent data scientists** spend **delivering refreshed brands** for customers (currently VZ) **from ~5 working days per month today to a couple of hours** setting things up for the pipeline to run and monitor it.

- Metrics:
  - Time spent per refresh
  - Date of refresh delivery MoM (aiming for consistency here)

### Reduce AWS cost (MH)

[Already started in Sep/Oct] We want **Verizon** to **pay less on their AWS bill** and in turn they will **pay us back a fraction of every $ saved**. By decommissioning Scylla, we will be able to go down **from $190K pm (today) to $160K pm**.

- Metrics:
  - Monthly Verizon AWS bill
  - $$ paid by Verizon to Intent for AWS cost reduction