# Background

In 2023, Intent HQ developed a CausalAI pipeline designed to run robust Causal AI models and create optimized audiences for campaigns. This pipeline has been evaluated on numerous retrospective datasets and is now being tested in-market as part of Verizon’s ‘MyPlan’ audience generation processes with the ‘Travelpass’ audience.

Anticipating the success of the initial audiences, we want to scale CausalAI and give end users the opportunity to trigger their own Causal audiences e.g. via a Lift product UI or through Edge. In order for this to be possible, as a minimum the campaign data must be evaluated for suitability and the Causal AI pipelines must be configured efficiently and accurately so that multiple CausalAI models can be run in short timeframes.

We have now manually evaluated enough campaign audiences that we can start to codify and automate the processes, further reducing the reliance on a human to evaluate the suitability of the data for a causal model.

Ultimately, to align with our strategy, we want these configuration steps to reach the point of full automation, so they could be configured by an LLM acting as a ‘triage agent’ and we can realise our strategic objective of allowing a customer to ask ‘any customer question’ and receive the insight that they need. The automated causal model configuration should be ready so that we can answer questions that are causal in nature. However achieving this strategic goal will take multiple steps.

## Current State

In 2023 The ADS team delivered a version of the CausalAI pipeline that we believe can underpin a first productized version of CausalAI. This pipeline was based on a product assumption that an initial release would be supported by a modified version of the Audience Maker UI to deliver Causal audiences to our customers (Paradigm 1 in figure 1 focuses on users choosing a historic campaign audience that they wish to optimize, and is the focus for this Shape-up)

[https://miro.com/app/board/uXjVKcC5Gg8=/](https://miro.com/app/board/uXjVKcC5Gg8=/)



The 2023 pipeline trains models and runs inference steps to generate ‘causal scores’ and build prescriptive audiences for the target campaigns that can be used in-market

In Q1 of 2024, the team built data visualization capabilities to support efficient validation of campaign data which had previously been performed using manual exploratory data analysis (EDA). 

[ADS Demo outlining capabilities as at March 2024](https://drive.google.com/file/d/1nJlZ7ust1RuMtOcbCz83agMBtNuQsgvU/view?usp=drive_link)

**Dashboard 1 - Outbound offer Overview**



**Dashboard 2 - Outbound Offer Campaign Deepdive**



# Problem

However, for our CausalAI methods to truly scale, we need to quantitatively assess the quality of campaign data, create specific evaluation metrics and then correctly parameterize the CausalAI models with minimal human interaction. We therefore need to:

- Automatically identify suitable historic campaign datasets for a campaign that contains enough data at sufficient quality
- Generate a set of clear and concise metrics and outputs that can guide both technical and non technical users. 
- If data cannot be found that meets any minimum quality threshold for a specific campaign, the CausalAI method needs to fail fast so that it may be possible to a fallback to an alternative lookalikes method (e.g. SMAC) while providing enough information to inform a user.
- Configure the CausalAI pipeline with appropriate parameters for the campaign and available data so that the model will run successfully
- Evaluate any additional confounding factors that could impact/bias the causal model and apply the appropriate remediations, such as:
  - controlling for users that have been repeatedly targeted over the campaign lifetime, thus diluting effect of the model 
  - adjusting for situations when customers have been targeted for multiple different campaigns/offers within a short timeframe where the link between the target campaign and the customer action is less clear. 

Currently this pipeline still requires significant manual input on the initial configuration of the pipeline to ensure that it both trains and runs inferences on the correct campaign data **and** that the data being used is suitable for the pipeline from a quality perspective. That role is currently being performed by Jiaqi Shi as an experienced CausalAI data scientist.

# Appetite

- We know that CausalAI audiences trained on historic campaigns are successful at optimizing future version of a campaign for Upgrades, Add-a-line and pricing campaigns, and we now have a much better understanding of the minimum data requirements for the models to be a success 
- The existing dashboards provide us with a quicker, richer view of conditions that impact performance - particularly the prevalence of repeat retargeting and individuals targeted across multiple campaign strategies in short time periods, but they do not make decisions. We now need to encode the decisionmaking process to ensure that the ADS team do not get tied up when running multiple causal models in a period. The appetite at Verizon is to be able to run causal models across significant volumes of Pricing, Upgrades and Add-A-Line campaigns in any given month, so we are targeting the ability to run >30 models a month out of this initiative.
- This process will also allow us to build/deploy a tool to support onboarding so that we can rapidly assess any new customer’s campaign data for Causal by iterating across their campaigns and scoring the quality.
- Feedback from sales team demonstrates increasing interest in our prospects in using the causal AI capabilities. Incorporating causalAI audiences into Lift creates a pathway to delivering effective lookalikes without weblogs
- Realising our ambitions at Verizon to cover >80% of their marketing footprint with Causal models necessitates a pipeline with minimal human oversight
- Intent HQ are are still one of the only (possibly THE only) companies globally with the combination of rich behavioral insight AND CausalAI capabilities in the marketing space.

# Solution

The solution will create the following:

**Quick decision pipeline for suitability:**

- A process to output set of thresholds and metrics that qualify any campaign’s historical data as suitable for the Causal AI pipeline, based on a traffic light system or similar (for example: red-fail, amber-marginal pass, green-pass), every time a model audience is defined, and ahead of attempting to run a causal model
- A set of tables that provide descriptive and statistical support to the traffic-light classification
- Clear documentation of the rationale, definition, justification and design of each metric, threshold and traffic for auditing purposes and to provide future product UI development with enough information to determine the importance of each metric to the end users
- All evaluation metrics, thresholds and traffic lights to be written to an easily referencable log for each run of the the processing pipeline, whether passed or failed 

**Clear end-to-end training pipeline design:**

- A comprehensive pipeline flowchart detailing all the necessary and optional model parameters
- A yaml file or equivalent for the causal model that contains all of the desired causal model parameters ahead of training the causal model and will be referenced by all model runs

## **Example**

Example 1 - Campaign coverage metrics



Example 2 -  Campaign delivery crossover metrics



Overall Flow



Prioritised QA Question scope 



# No-Goes

This initiative will not provide any frontend UI elements or user dashboards, as these would be considered within the scope of the Natural Language Prescriptive Audiences shape-up - which governs the End to End process of asking a question with a Causal component in a UI, triaging the question via an LLM to the causal model and, once the Causal model has run the inference, providing the insight/audience in a consumable form for the end user.

This specific initiative will not explicitly look at delivering CausalAI insight via Edge. This question is part of a separate spike planned for Q2H2 following currently ongoing conversations with Intent Israel to determine suitable datset for the development spike. We are happy that this initiative in its current form will not prejudice our future ability to deliver Causal audiences via Edge 

We identified other desirable outcomes that we do not think are achieveable in 6 weeks but will likely be part of a future focus:

- A process to output a metric that communicates the level of uncertainty in the causal score predictions based upon the statistical significance attributed to different causal features identified when training the causal model. 
  - This is straightforward for linear Causal models, however it is non-trivial for some of the better-performing non-linear causal models, and therefore would likely take more time to solve. Once we have Alex Silver and Tom Gibbs fully trained on Causal in Q2 , we will be able to address this problem. 
  - We should note that we do not think that not doing this work would block a first product release, as we are confident that even without full clarity on the uncertainty, the level of uncertainty is likely to be significantly lower than current best practice marketing approaches.

This initiative will not focus on determining the appropriate fallback mechanism if there is not enough data to train a causal model, as there are separate product decisions to be made regarding the evolution of SMAC and SMAC automation, that are not within the scope of Causal AI

We do not expect this initiative to achieve 100% automation, as it is likely that additional challenges will emerge from this work, and as we scale up the exectution of the model across many tens of campaigns. However the aim is to enable us to to be able to train a target of 30+ Causal models a month if needed



Done reading? Click here. → Jonathan Lakin

Jonathan Lakin I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| false |  | Kumutha Swampillai |  |  |