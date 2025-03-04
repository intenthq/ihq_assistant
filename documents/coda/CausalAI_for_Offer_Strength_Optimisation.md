# Background

In the first half of 2024, Intent HQ developed an end-to-end Causal AI pipeline as the first step to scale up the Causal AI capability. This pipeline allows us to efficiently gauge the quality of the raw data, process features for model training, and train, evaluate, and select the best model for downstreaming tasks. The pipeline have been used to build causal models for 10 recent upgrade campaigns of Verizon. Combined with meta-configuration tool, we have proved that the pipeline can successfully run through within one or two working days for all 10 campaigns.   

Despite the usefulness of the current pipeline, it is not capable of handling multiple campaigns at the same time and therefore is limited in optimising campaign-level marketing components. For marketers within Verizon and other prospects such as Estee Lauder, it is often the case that they’d like to provide different offers to users/consumers in order to maximise their responses and ultimately the company’s ROI. As a result, we’ll need to explore a new approach that models several offers together and estimates the potential outcome of each offer given users’ characteristics. 

# Problem

### 

### Problem overview

Being able to predict the optimal offer using Causal AI will be a game-changer in both helping Verizon increase the ROI of their marketing campaigns as well as a broader Marktech space. It is common for marketers to want to target different users with different offers (e.g. various offer strengths, different type of perks, etc.) as users’ lifetime value at risk and tastes are different. For example, if a user of Verizon’s potential lifetime value to be saved is only $500, the maximum discount for an phone upgrade should probably be no more than $500 to generate profit; whereas if that number is $1000, the marketer will probably want to be more generous in their offering. With Causal AI’s offer strength optimisation capability, such decision making will be more streamlined and with higher accuracy.

In addition, building the aforementioned capability also helps when we don’t have a perfectly-constructed treatment&control group in our data. In those situations, instead of comparing users who are targeted to the control group, we can compare users who are targeted by different campaigns to a baseline treatment group. The new capability hence enables us to provide services even to prospects that doesn’t deliver campaign along with a control group.



# Appetite

### Goals & Success

Optimising offer strength comprises two challenging tasks:

1. Model multiple campaigns data within a single model in regardless of the targeting metrics to be optimised. 
2. A comprehensive modelling framework that takes into consideration the campaign’s impact on the profitability as a function of reduced churn rate, customer lifetime value, and cost of offer.

Considering the complexity of the problems, we plan to spread the goals across two three-sprint stages:

Stage 1: Sprint 1-3

1. A thorough analysis of Verizon’s dynamic offers: Focusing on how did offers overlap with each other, and how each users were retargeted offers. 
2. A detailed document surveying the relevant research on multi-campaign modelling, with a special focus on the challenges with Verizon’s data and how we plan to solve it
3. Construct a new model framework according to the data. Train a new Causal model on take as well as a synthetic profitability metrics with the goal of choosing the optimal offer strength. 

Stage 2: Sprint 4-6

1. A review of data readiness for modelling profitability. This includes churn data, cash flow metrics, as well as the cost of offers.
2. A detailed document surveying the relevant research on profitability modelling
3. Test one of the approach identified with the data available

# Solution

### Exploratory data analysis

The result of the data analysis should seek to answer the following questions:

Stage 1:

1. Do different offers have any overlap in their targeted audiences. 
2. Is there a clean sample (i.e. free from any recent retargeting) that we can use

Stage 2: 

1. Can we observe any significant change in churn rate and cash flow after users have taken the data? 

### New modelling framework

Stage 1:

A new modelling framework that models multiple campaigns at the same time

Stage 2:

A new modelling framework that models churn reduction, change in cash flow, as well as the cost of retention at the same time





Done reading? Click here. → Jonathan Lakin

Jonathan Lakin I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false |  | Kumutha Swampillai |  |  |