[See here for guidelines on how to complete this stage](https://coda.io/d/_dK5h4iVEEUo/_suaY6)

| Name | Role in the project | RACI | Role in the company | Comments |
| --- | --- | --- | --- | --- |
| Kumutha Swampillai | DS manager | Accountable | Data Science Director |  |
| Sebastian Martins | Lead DS | Responsible | Principle Data Scientist |  |
| Talvany Carlotto | Data Scientist | Responsible | Data Scientist |  |
| Daria Barbalata | Product owner  | Responsible | Product Owner |  |
| Andy Cole | QA lead | Consulted | Global Director of Applied Data Science and Analytics |  |
| Sharifah Amirah | Head of Product | Consulted | Chief Customer Success Officer |  |
| Sangram Reddy | ML Architect | Consulted | Head of ML Engineering and Architecture |  |
| Anthony Channon | CTO | Consulted | CTO |  |
| Sriram Muli | Productionising model | Informed | Machine Learning Engineer |  |
| Eddie George | Productionising model | Informed | Machine Learning Engineer |  |
| Rachel Yeomans | Product User | Informed | Customer relationship lead |  |
| Candace Kala'i | Product User | Informed | Customer support |  |
| Kalin Kirev | Product User and Interface with Client Team | Informed | Programme manager |  |
| Aaron Schick | Product User/Maintenance | Informed | Data Analyst |  |
|  |  |  |  |  |


# Links to Develop stage Artefacts 

- **Code repository**: [github.com/intenthq/ihq-embeddings](github.com/intenthq/ihq-embeddings) 
- **Model documentation**:
  - Model card: [https://coda.io/d/_dK5h4iVEEUo/_suGH6](https://coda.io/d/_dK5h4iVEEUo/_suGH6)
- **Model evaluation**
  - Iteration 1: [https://coda.io/d/_dK5h4iVEEUo/_suP7X#_luZCW](https://coda.io/d/_dK5h4iVEEUo/_suP7X#_luZCW)

# **Purpose of the Develop Gate**

Our objective is to review model experiments and evaluation with project Stakeholders to collectively decide whether 

a) it is ready for User Acceptance Testing and a potential Beta release?

b) the model requires a further iteration of R&D to better meet the requirements of the use case?

c) we should pause any further development using this approach and instead reshape an alternative solution?

# **Scope Recap**

## **User Story Brief**

**As a campaign manager, I want to explore the brands that my customers interact with using AI Audience on-prem, and use them to build audiences that target the right customers for my marketing campaigns.**

## Requirements

In order to fulfil the above User Story, brands need to be created that meet the following requirements:

1. Ensure that behavioural profiles viewed through Top Winners in IE are intuitive and interpretable by our users such that we can be assured that brand profiles continue to **preserve key behavioural signal**.
2. Ensure that brands used as selection criteria for Audience Maker seeds are equally **effective in marketing campaigns.**
3. As brands are used to select audiences for *future* marketing campaigns, ensure they model **future user interactions** rather than model past ones.
4. Provide a measurable level of confidence that we are **not replicating user brand engagement profiles**. This is because *VZs legal team have deemed Allocated Brands (BAU) unsuitable* for use on prem due to the one-to-one nature of User-Brand allocations.

A solution was shaped and designed to meet the above requirements. Details of the underlying deep learning technique used for the new brand prediction model - variational autoencoders - can be found [here](https://coda.io/d/_dK5h4iVEEUo/_sulzC#_luMfM). A number of cycles of R&D have been iterative carried out to improve the performance of this model. 

## [Success Criteria](https://docs.google.com/document/d/1sefCn94MtyKNz4oR77NlEcWbGcIX7ceJfhyVu8E81-0/edit)

**[1) User’s Behavioural Embeddings](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luTCe)**: Build behavioural representations that **preserve the key signal while ensuring the likelihood of replicating user brand engagement profiles.**

- The output provides an equal or higher performance than BAU when comparing against **future user engagement** (aka, 30 days user’s engagement).

**[2) Understanding the most relevant users for each brand](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_lup6q)**: Predict user segments for each brand in the VZ allow_list

- The output needs to satisfy the user's expectations when using the results on `**Insight Explorer**` (See details [https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq).)

**[3) Risk of replicating user profiles:](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_lutba)** We need to ensure to a measurable level of confidence that we are **not replicating user brand engagement profiles**.

## Document Outline

This document presents the results of the first iteration of the model, focusing on how it well it meets the above success criteria. **Section 1** explains the model evaluation process, BAU baseline and the metrics used to measure performance. **Section 2** details the performance of the model in predicting a user’s brand interactions in the next 30 days, demonstrating it’s ability to preserve behavioural signal. **Section 3** details the model performance identifying the best users to engage at brand level, as well as a qualitative assessment of it’s ability to preserve signal using Top Winners. **Section 4** investigates the risk of this model replicating user brand profiles and finally, **Section 5** outlines recommended next steps and future work for the project.

# **Section 1 - Model Evaluation Process**

We have built a process to assess the quality of the brands, assessing the likelihood of identifying recurrent and novel user behaviour. We compare the predicted model against BAU evaluating the results using metrics like precision, recall and f1-score, following the standard statical practices for A/B testing and power analysis.

### **Why comparing against BAU**

BAU is the current aggregative brand model in production, that is the tool that VZ team uses to create segments, identifying the most relevant users for a brand. 

The predictive brand modelling will be a replacement of this solution on-prem, and therefore using the current model provides a good baseline indicator to assess the performance of a new solution.

### **Statistical Power and Sample size for the assessment**

For our assessment, we wanted a representative sample of our users. Based on traditional sampling practices, you would need a way smaller sample than that to have a representative sample.

| Name | Value |
| --- | --- |
| **Statistical power** | 95% |
| **Significance Level** | 1% |
| **Baseline conversion rate** | 15% |
| **Minimum Detectable effect** | 1% (absolute) |
| **Recomended sample size** | 45,903 |


To be on the safe side, we decided to user a sample higher than that for the assessment. As we were already using 1M user samples for training, we chose **1 million users** as the size for the assessment.

Experiments were implemented on different periods, testing the model performance against the months: August 2023, December 2023 and January 2024. Result were consistent across the different timeframes, presenting in this page the ones obtained for January 2024.



### 

### **Quick recap on precision, recall and F1 score.**

  - **Precision:** Out of the number of predictions, how many were correctly predicted (**quality of prediction**)
  - **Recall:** Out of the number of things we should have predicted, how many were correctly predicted (**coverage** of the predictions)
  - **F1 score:** the harmonic mean of precision and recall (**combination of precision and recall**)

# **Section 2- User’s Behavioural Embeddings**

This section assesses the capability of the representations to capture relevant behaviour to understand the users interactions and predict their future behaviour.

The image below the kind of profile we are trying to capture in this section.









### a) Predictive Capabilities: assessing predictions against future behaviour

How do we define **future user behaviour** (also known as `Relevant Interactions` )?

Our goal is to establish a definition of what we can consider a Relevant/Positive User Interaction with brands that introduces the minimal number of assumptions. The main focus is about finding recurrent behaviours, aka users interactions that are repeated across time and therefore can be considered as a relevant signal to target them.

### What does it mean to be interested in a Brand?

After analysing the likelihood of users to engage with a brand again, giving different levels of historical interaction, we found that:

Having **at least 2 clicks in the course of 1 month** provides the lowest level of engagement while removing a big proportion of the noise (aka, interactions that can be considered irrelevant as users never interacted again with the same brand).

To analyse the predictive capabilities, we have run assessment experiments across multiple windows. We can iterate across time (using sliding windows) to train, assess and make inference of the users’ future behaviour.



*[Source](https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764572934152044&cot=14)*

why 30 days window? The typical lead times from defining an audience criteria to a campaign being launched in market is estimated at 30 days from our previous experience with Verizon campaigns.



[Source](https://docs.google.com/spreadsheets/d/1lMPRd6qVhURNfrZ1kA6GqMH5Bfw69L-Cq97oQz0uC3g/edit#gid=1209693993)



**Highlights:**

- F1 score is almost the same across both models, however, VarEmb has significant higher precision but a lower recall. That means: 
  - VarEmb predictions will be of higher quality: which provides a more **accurate representation of a user profile**. 
  - VarEmb predictions **have a lower brand coverage**: the user profile will contain fewer brands than BAU, which contributes to a less similar user profile (incidentally, that aspect is also desired for the privacy constraints requested by VZ).

The results of the VarEmb model in the table above reflect predictions generated by training on the November 2023 refresh and compared against January data. Additionally to that, we also compared those predictions against December data, and the results in both experiments were equivalent. That tells us the we should expect the same prediction performance in at least the next two subsequent months of data the model is trained on. 

The table below shows the total number of predictions generated by BAU and VarEmb for the whole population of ~66M users.

## Total number of predictions per user 2
| Name | Total number of brand predictions | Average number of brands per user |
| --- | --- | --- |
| BAU | 10.4 B | 157 |
| VarEmb | 3.3 B | 49 |


The image below illustrates an average user (using the average prediction number). It shows that, while the VarEmb coverage was smaller, the quality of the data (% of correctly identified brands) is significantly higher.



*[Source](https://docs.google.com/presentation/d/1lOYHMSiVG_8ky7BEPNjZEtjwsnesTNYLuQU_eP2dfpU/edit#slide=id.g2bc828015ad_0_0)*

**Highlights**:

- The difference in sizes and in the proportion of correctly identified brands means that VarEmb should:
  - Reduce the spam and the digital waste by reducing the amount of incorrectly target people (aka, more precise when it indicates that a user is interested in something).
  - Generate a more accurate representation of the users, allowing us to find more meaningful behaviour in similar users, and therefore, generating seeds that contain more relevant people to expand and capture the right audience (the noise to value ratio is of 1/2 on VarEmb vs 1/3 in BAU).
- **BAU** generates a much **high number of predictions** the the actual number of true predictions. The reason for this is that approach is very lenient regarding what constitutes an interaction. If a user clicks once on a brand that is already an interaction for BAU, for instance. Additionally, the input data we are using is three whole months, while we are assessing against one month. More input data means more predictions in this case.
- BAU generates around 3X more predictions, which explains the higher coverage, however, 64% of those are incorrect.
- It’s relevant to highlight that in **VarEmb**, the size of the predictions per brand are optimised to adjust to the expected volumes seen on historical trends. This aims to provide a more accurate and representative size of the audience interested in a brand, better aligning with the users expectation, and therefore, their confidence/trust in the solution.

### **Novel/Recurrent performance**

In this section we further analyse the performance of the model by splitting them into 2 categories:

- **Recurrent behaviour**: brands that users have already interacted in the past and are expected to continue engaging with in the future.
- **Novel behaviour**: brands that users have **NOT** interacted with in the past but will in the future. By future we mean unseen user behaviour at the time the recommendations were made.

**Recurrent behaviour**



**Novel Behaviour**



**Highlights:**

When splitting the analysis between known recurrent behaviour and novel user behaviour, we can observe the following:

- **VarEmb** shows some initial capability to capture **novel behaviour** (~3/4%). Showing not only the ability to understand the user profile, but also to complete with some relevant additional recommendations.
  - As expected BAU doesn’t have capabilities to identify novel brands for a user.
- **VarEmb** model significantly **outperforms** **BAU** approach on **recurrent behaviour at user** level (by 10%). 
  - This significant difference in comparison with the global score is caused by an statistical behaviour known `Simpson Paradox`, where VarEmb average overall performance is decreased by its attempt to capture novel behaviour (which is not done by BAU model).

### b) Synthetic Capabilities: assessing predictions against input data

This section analyses the performance of the model capturing the patterns present in the input data, and its ability to reproduce the main recurrent behaviour seen **at user level**.



The results shown in the previous table are consistent with the previously described for the predictive future behaviour.

# 

Taking the points above into account, it would be a fair conclusion to say **VarEmb slightly outperforms BAU when analysing its capability to understand and predict user profiles**

# **Section 3- Understanding most relevant users for each brand**

This section assess the model’s capability of identifying the best users to engage at brand level, according to historical and future interactions.

The image below represents the perspective of the analysis performed in this section:





## Total number of predictions per brand 2
| Name | Total number of brand predictions | Average number of users per brand |
| --- | --- | --- |
| BAU | 10.4 B | 3.2M |
| VarEmb | 3.3 B | 1M |


Note that predicting a brand profile is a much harder and less exact task than predicting user profiles. For each brand you could be predicting millions of users on average. Additionally, brands profiles are way more volatile than user profiles - that is, user profiles tend to be more consistent across time. Therefore, the metric **results** in this section **will be much lower** than the results for user profiles. 

### a) Predictive Capabilities: assessing users that are most likely to interact with the brand in the short-term future



[Source](https://docs.google.com/spreadsheets/d/1lMPRd6qVhURNfrZ1kA6GqMH5Bfw69L-Cq97oQz0uC3g/edit#gid=1209693993)



**Highlights**:

- F1 score is the same across both models when comparing all the brands that users interacted with, however VarEmb **underperforms** BAU for the **approved brands**.
- VarEmb underperforms mainly in low-volume brands (more explained below). We are discussing strategies to account for that (e.g. under/over sampling brands)

### **Novel/Recurrent performance**

**Recurrent behaviour**



**Novel Behaviour**



**Highlights:**

- **BAU** still **outperforms** **VarEmb** at **item level**, but only slightly (reduced to ~1%). 
  - The trade-off between precision and recall is still preserved on these results.
  - As the f1-score difference is minimal, we can expect VarEmb to perform at similar levels as BAU for recurrent behaviour.

**NOTE**: The significant difference in comparison with the overall performance of VarEmb is produced by trying to predict on novel brands (a much harder task), which the BAU process cannot do. This effect is a known statistical behaviour called `Simpson Paradox.`

### Analysing brand level performance by size

The following table shows the models performance at brand level for some of the approved brands:

## Examples of brand scores 2
| Brand | BAU - F1 | VarEmb - F1 | estimated size |
| --- | --- | --- | --- |
| Apple Inc. | 86% | 95% | 52,405,279 |
| The Weather Channel | 86% | 72% | 27,236,828 |
| Venmo | 72% | 57% | 13,957,473 |
| Lyft | 54% | 32% | 3,450,658 |
| ABC News | 24% | 36% | 1,037,445 |
| Olive Garden | 18% | 7% | 758,489 |
| Jo-Ann Stores | 24% | 11% | 722,781 |
| Allegiant Air | 43% | 9% | 653,216 |
| Jeep | 18% | 9% | 462,839 |
| HBO | 7% | 1% | 81,310 |
| Women's Wear Daily | 5% | 9% | 77,533 |
| Quiksilver | 12% | 2% | 62,395 |
| Linguee | 8% | 1% | 10,569 |
| Prince (musician) | 13% | 0% | 1,027 |
| Teenage Mutant Ninja Turtles | 0% | 0% | 6 |


- The table above is ordered by size, and it shows the correlation between brand volume and scores. Brands with more data tend to perform better in both models.

## Size 2
| Cat | # unique users | # brands |
| --- | --- | --- |
| **Small** | 100,000 | 1,551 |
| **Medium** | 1,000,000 | 1,248 |
| **Large** | >=1,000,000 | 359 |








*Source:* *[brand level scores](https://docs.google.com/spreadsheets/d/158SQqRZGb9qbFxOBgEj0UoWenEsd3PpBytynhUIufTY/edit#gid=1125207804)*

**Highlights:**

- BAU solution performs better in 57% of the approved brands, and across each of the categories.
- Both models find it difficult to understand the recurrent patterns on ~16% of the approved brands (almost all of *small size*). Where either of the approaches identifies less than 10% of the right audience.
- The predicted brand model shows a biased based on brand sizes, having a better performance the more popular a brand is.
  - This is illustrated in the plot by the increase in proportion in the amount of wins on the Medium and Large categories.

### Work in Progress

Current Work In-Progress and future work to solve the **known model limitations**:

The team is currently working (and has additional steps in the short-term roadmap) on a new version that improves the performance of the solution by addressing the previously mentioned limitation. These are:

- Implement a `balancing strategy` by brand sizes: aims to minimise the biases on the model regarding this aspect. This involves adjusting the impact (or weighting) of the most popular brands with the goal of training the model to better capture patterns for smaller brands. Several strategies are currently been tested to identify the optimal approach, such as:
  - Implement a `weight balancing` approach in the cost function that the model use to find and optimise the patterns in the data, to efficiently (from a computational and design perspective) balance the impact of the brands in the model performance.
  - Implement a brand level (under/over) sampling approach, balancing the presence of brands in the model and therefore allowing the model to better understand small size brands.
- `Model Architecture` Optimisations: implement strategies to increase the power of the model to learn more (and more complex) patterns by:
  - Increasing the size of the model, both in number of layers and neurons.
  - Improve the regularisation and cost functions use to minimise the chance of overfitting allowing the model to train for more iterations and capture more complex patterns.

### Raw Resources

raw table: [https://docs.google.com/spreadsheets/d/11WuuVlAcrIlmpd3IZKhbHLWy9V41Jh0uhZAul-i5bl0/edit#gid=0](https://docs.google.com/spreadsheets/d/11WuuVlAcrIlmpd3IZKhbHLWy9V41Jh0uhZAul-i5bl0/edit#gid=0)

### b) Synthetic Capabilities: Assessing brand understanding based on current user interactions

This section analyses the performance of the model capturing the patterns present in the input data, and it’s ability to reproduce the main recurrent behaviour seen in **at brand level**.



**The results shown in the previous table are consistent with the previously described for the predictive future behaviour.**

### **c) Assessing segments in Insights Explorer (Qualitative analysis)**

We need to ensure that the switch from allocated brands to modelled brands does not degrade the quality of insights which we are able to explore and use for audience building. Specifically,

1. The easy interpretability of top winners in the Insights Explorer;
2. The top winners and QA metrics on a number of commonly used brands;
3. The ability to model lookalike audiences starting from Brands that have previously been used for such use-cases;

We will assess a these visually in IE; the test owner will give pass/fail result with justification and supporting screenshots (following [https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq).)

**Assessment summary:**

- Most used Brands in Verizon campaigns look good and are aligned with other behavioural attributes;
- Social media brands tend to index lower (when not specifically filtering for social media) than they do with descriptive brands which has always been expected given these are commonly used by most people and not distinctive behaviour.
- The FMCG effect reduced may very well be a result of those brands no longer being part of the approved brands, but generally FMCG brands that are still there (e.g. Pampers) index lower when they come up compared to the (old) descriptive brands.

### Test Cases Sanity Checks - visualised in IE 2
| Test description | Purpose | Success criteria | Result | Test owner | Test date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Brand filter: Netflix | Frequently used for partner perk campaigns | Top winning Brands & Interests align with user expectations | Passed - expect to see streaming & takeaway overindex. | Daria Barbalata | 2/29/2024 | <br/><br/> |
| Brand filter: Disney+ | Frequently used for partner perk campaigns | Top winning Brands & Interests align with user expectations | Passed - expect streaming and takeaway, but also ‘younger’ Brands like Nyx, Elf, Bose, Lego & Gaming Natural Audience over-indexing. Some of the assumed FMCG flaw is present but only for 4 Brands in the top 24 which isn’t enough to raise red flags. These are also not unlikely brands to truly over-index alongside Disney and they rank lower than seen in the (old) descriptive brands. | Daria Barbalata | 2/29/2024 | <br/><br/> |
| Brand filter: HBO | Frequently used for partner perk campaigns | Top winning Brands & Interests align with user expectations. | Passed - not as convincing, but also not obviously flawed & over-indexing Natural Audiences are validating. | Daria Barbalata | 2/29/2024 |  |
| **Brand filter: Walmart** | Frequently used in IE over the past 12 months | Top winning Brands & Interests align with user expectations | Passed - expect seeing other department & discount stores over-index + Interests are highly correlated.  | Daria Barbalata | 2/29/2024 | <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>Comparison: [https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764581367987741&cot=14](https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764581367987741&cot=14)<br/><br/><br/><br/><br/><br/> |
| Brand filter: Tiktok | Frequently used in IE over the past 12 months | Top winning Brands & Interests align with user expectations | Passed - expecting to see most top winners made of commonly used social media apps and websites, but reassuring to see Pinterest & Snapchat index higher than all others here as apps known to be used mostly by a similar demographic to Tiktok. | Daria Barbalata | 2/29/2024 | <br/><br/> |
| Brand filter: T-mobile | VZ’s key competitor | Top winning Brands & Interests align with user expectations | Passed - expect to see other telecommunications companies over-indexing as well as the interest. Extra assurance to see the over-indexing younger age-group (and Gaming Natural Audience as it’s known to Verizon that their competitor T-mobile is stronger in that demographic. | Daria Barbalata | 2/29/2024 | <br/><br/> |
| Brand filter: Arlo Technologies | Low-volume brand previously used in campaigns | Top winning Brands & Interests align with user expectations | Passed - expect to see other smart home brands and these rank higher than they do in the old (descriptive) brands despite the low volume. Interests could be better aligned, but there is correlation there too. | Daria Barbalata | 3/1/2024 |  |
| Brand filter: ESPN | Male skewed brands used in the past to explore customer profiles | Top winning Brands & Interests align with user expectations | Passed - expect to see other sport brands, the correlated interest as well as a middle-aged male skew. | Daria Barbalata | 3/1/2024 |  |
| Brand filter: Whole Foods Market | Trending brand used in the past to explore customer profiles | Top winning Brands & Interests align with user expectations | Passed - Top winning brands aren’t too convincing, but nothing jumps out to be obviously wrong. Interests are very aligned and some of the other things over indexing (like interior design or mindfulness) are likely to be true for the behavioural profile of people buying organic food. | Daria Barbalata | 3/1/2024 | <br/><br/><br/><br/> |
| Brands filter: Wayfair | Distinctive brand expected to show interesting customer profile | Top winning Brands & Interests align with user expectations | There are some other homewear brands and many other ‘surprising’ but fairly consistent over-indexing behaviours. Not convinced by the order (e.g. IMDB ranking 2nd) | Daria Barbalata | 3/4/2024 | <br/><br/> |
| Brands filter: Ticketmaster | Distinctive brand expected to show interesting customer profile | Top winning Brands & Interests align with user expectations | Passed - seeing more event brands over-indexing + other consistent behaviours. CRM interest is a bit weird - should it even be an target topic for marketing? | Daria Barbalata | 3/4/2024 | <br/><br/> |
| Interest filter: Streaming | Frequently used for partner perk campaigns | Top winning Brands align with user expectations | Passed - related brands over-index higher. There is still some of the dodgy FMCG effect, but less Brands and ranked lower, thus no longer raising a red flag. | Daria Barbalata | 3/1/2024 |  |
| Interest filter: NFL | Frequently used for campaigns | Top winning Brands align with user expectations | Passed - lots of related sports brands over-indexing. | Daria Barbalata | 3/1/2024 | <br/><br/> |
| Interest filter: Social Media | Frequently used in IE over the past 12 months | Top winning Brands align with user expectations | Passed - you would expect a lot of different things to be relevant for people that use social media (almost everyone) and importantly the FMCG effect is less pregnant than in the (old) descriptive brands.  | Daria Barbalata | 3/1/2024 | <br/><br/> |
| Interest filter: Consumer Electronics | Frequently used in IE over the past 12 months | Top winning Brands align with user expectations | Given the other over-indexing interests this looks ok-ish, but not seeing consumer electronics brands in there. This should be adressed by aligning topic modelling to Brands - shapegate for it [here](https://coda.io/d/_dK5h4iVEEUo/_suke-) | Daria Barbalata | 3/1/2024 | <br/><br/> |
| Interest filter: Video Games | Frequently used in IE over the past 12 months | Top winning Brands align with user expectations | Passed - many gaming brands come up though the order can be questionable (e.g. Voodoo first). | Daria Barbalata | 3/1/2024 |  |
| Smart Audience filter: New Movers | Recent Verizon camapign | Top winning Brands align with user expectations |  | Rachel Yeomans | 3/1/2024 |  |
| Lookalike: Disney-Bundle - seed = Disney+, Netflix, HBO | Monthly recurring audience requests | Expansion passes QA & output top winning Brands & Interests match previous runs |  |  |  |  |
| Lookalike: Plus-Play - seed = Netflix, National Footbal League (should we separate these? why are they together?) | Monthly recurring audience requests | Expansion passes QA & output top winning Brands & Interests match previous runs |  |  |  |  |
| Lookalike: Apple-One - seed = Apple Music | Monthly recurring audience request; This is currently modelled from previous takes because the Apple Music seed wasn’t homogenous enough to model against - interesting to see how the new one works; | Expansion passes QA & output top winning Brands & Interests match previous runs |  |  |  |  |


# Section 4- Risk of replicating user profiles

Our model uses **Variational Auto-encoders**, which are generative AI. Part of that architecture involves learning how to handle a component of randomness in the compression of the data, which means that outputs will not be a direct mapping of the inputs (as it would be the case in a regular auto-encoder). This gives us a **high level of confidence that we are not replicating user profile data**.

As we apply transformations to the model output to generate the brands and we want to demonstrably prove this to Verizon, we run further analysis to assess the risk of replicating use profiles.

This section assesses the **likelihood of replicating**, with different levels of risk, **a user profile** by assessing the expected frequency of generating a user representation that replicates with high level of similarity the original user representation (input).

### Results

To identify and assess the level of risks, we have catalogue the risks into 3 levels:

- High risk: we replicate a user profile with a 99% or more similarity.
- Medium risk: we replicate a user profile within a 90% and 99% of similarity.
- Low risk: we replicate a user profile within a 85% and 90% of similarity.

An example of a Medium risk user is shown below:

 *[Source](https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764577442390521&cot=14)*

Giving a user with 100 recommended brands, a for a user at High risk, we would either replicate the user interactions, not include 1 of the brands that the user has engaged with or have an extra brand recommended that the user hasn’t interacted with.

The results generated on a sample test of 1M user profiles shows the following results:



**NOTE**: if we consider all the users with 80% or more similarity, the total will increase to 1726 (0.18%).

**Conclusions:**

- the **likelihood of replicating a user profile with 85% of coincidence or more is lower than 0.1%** (~0.08% in 1M users), which means that for every 1M users profiles, less than 1k users will have this risk.
- less than 0.01% of users will be in the high risk zone, which means that for every 1M users profiles, less than 100 users will be in this zone.

Further analysis on how popular are the brands of the users identified in the highest level of risks, to understand in more detail how unique those profiles are and therefore how likely is to identify the users based on those interactions.

### See: More details

Below you can visualise the table presenting in more detailed the previous results. 



*[Source](https://docs.google.com/spreadsheets/d/1KcQmjCWfYNA9JDQmmIvi7jW9PPHu6cL7vRUJdLkzd3o/edit#gid=1651262150)*



# **Section 5 - Conclusions and Recommendations**

## Assessment Summary

Based on the information presented in this document, we can summarise the following conclusions organised by success criteria:



**[1) User’s Behavioural Embeddings](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luTCe)**: Build behavioural representations that **preserve the key signal while ensuring the likelihood of replicating user brand engagement profiles.**

- The output provides an equal or higher performance than BAU when comparing against **future user engagement** (aka, 30 days user’s engagement).

**Takeaways**: 

- **VarEmb brand profiles perform better** than BAU brand profiles when evaluating against future 30 day brand engagement (3.4% uplift in f1 score). This demonstrates that this model is capable of preserving high quality signal. 
- The VarEmb model is not directly leveraging the users historical data when predicting brands and therefore it is capturing signal in a far more difficult way than BAU which directly maps users brand interactions. This makes equivalent performance between VarEmb and BAU all the more impressive. Unlike BAU **it is able to retain signal without directly mapping brands and can generate user profiles that capture both recurrent behaviour and future novel behaviour.** 



**[2) Understanding the most relevant users for each brand](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_lup6q)**: Predict user segments for each brand in the VZ list of approved brands

- The output needs to satisfy the user's expectations when using the results on `**Insight Explorer**` (See details [https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luTsq).)

**Takeaways:**

- **When doing an overall analysis: BAU outperforms VarEmb on brand level** (-9.6% uplift in F1 Score for approved brands)**.** 
  - We observed that the model had more difficulty capturing low-volume brands, while performing slightly better on bigger size brands.
  - However, when analysing the performance at the same tasks that BAU focuses (aka, on recurrent behaviour only), the uplift is considerably reduced to only 1.2% (while presenting a 10.1% at uplift at user level).
- **Recurrent vs Novel Behaviour**: While the VarEmb model has slightly worse performance than BAU on recurrent behaviour it is able to predict novel behaviour which BAU is not able to do at all. 

**Initial assessment on Insight Explorer** anecdotally shows that predictive brands are performing well on Insight Explorer:

- The **most used Brands in Verizon campaigns look intuitive** and are aligned with other available behavioural attributes on Insight Explorer, with a lower indexing of social media brands as expected, as these are commonly used by most people and not distinctive behaviour.
- The **effect of FMCG brands seems reduced**, having lower ranks when they come up compared to the (old) descriptive brands.

The results at Brand level, specifically for low volume brands, are not yet where we would like and propose a second iteration of model development to assess and improve the performance.



**[3) Risk of replicating user profiles:](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_lutba)** We need to ensure to a measurable level of confidence that we are **not replicating user brand engagement profiles**.

We have proposed 3 categories to classify the level of risk on replicating users profiles. Based on those categories and after analysing the likelihood of replicating user profiles, we can conclude that:

- VarEmb approach shows that the **risk of replicating  a user profile with a 85% or higher level is lower than 0.1%**. 

Therefore, we understand that the **criteria** for this section **has been met**. However, we understand that further questions and analysis might be required to assess and understand if these levels are acceptable to VZ and their legal team.

## Conclusion

**Data Science are satisfied that the model results presented above for VarEmb v1 indicate that it is ready to move to** ***Productionisation*** **and** ***Testing*** **and then to** ***Deployment*** **subject to sufficient performance on the test plan.** 

## Next Steps

- **Complete productionisation** for the model including: integration into the refresh cadence via the Inference Engine; building monitoring process and designing and implementing QA.
  - NB once we do this upfront work, subsequent model versions will take less than a day to deploy and release in the inference engine
- **Execute UAT** for this version of the model to both assess performance and uncover any issues that need addressing prior to deployment. This should include collaborating with CS on:
  - Assessment of Brands using Top Winners in IE
  - Assessment of look-a-likes
  - A/B testing of Audiences in campaigns
- **Iterate on the model to improve performance**, specifically at Brand level. A high level 2-3 month plan is included below. 

## High Level Plan for Model Development Iteration  

These are our priorities for a second iteration of model development aimed at improving model performance. We expect the iteration to take 2-3 months.



**Brand level model performance** - We have identified a few points to improve the overall metrics at brand level. The main ones are:

- Over/undersampling - Since we are only training on a fraction of the data we have available it will be really easy to over sample niche brands to generate more signal for them in the model. We can also dampen the effect of the popular brands where necessary.
- Weight balancing  - Implement a weight balancing approach in the cost function that the model uses to optimise the patterns in the data. This can efficiently (from a computational and design perspective) balance the impact of the low and high volume brands in the model performance.
- Regularisation - Improve the regularisation of the model to minimise the chance of overfitting allowing the model to train for more iterations and capture more complex patterns.
- Dynamic recall/precision thresholding -  to increase the recall and decrease the precision of the brands that aren't performing as well. We can work collaboratively with CS team to define appropriate thresholds.

 

**Further analysis** - There are further investigation points that we would like to look into to better understand the results we have and discover ways to optimise the model.

- User subgroups - e.g. are users with very little browsing data being accurately predicted, should we exclude them from the training?
- Niche brands - which niche brands are performing better than others, can we understand why that might be the case?

 

**Overall VAE architecture** - We can explore and change the model architecture to try and make the model learn more from the data.

- Embedding size - We trained the model with 10M users (10x the amount in the current model) but didn't see much improvement. This suggests that the size of the embeddings (50d) could be too small to capture the complexity of the data.
- Encoder and decoder models - We have used a small number of fully connected layers. We could expand this architecture to further layers or even more complex ones to allow the model to learn patterns it is not able to currently.

 

**Data cleaning** - Past exploration of the data showed there's substantial noise present in the data we are using. No recent effort has been put in to improving the block list or detecting noise in the input data, for instance. There are likely substantial gains to be gotten from that.

## Caveats, Risks & Mitigations

- The model produces scores that are not being surfaced for users on Insight Explorer - this can be enabled in the future alongside UX optimisations to maximise the usefulness of this data to users depending on their campaigns. 
  - For now, the output will be visualised in the same format as the current (descriptive) Brands card and it will replace it at least in the on-prem environment.
- Further improvements can be explored by enriching our process using campaign results data.
  - Current approach uses implicit feedback (based on users recurrent interactions) as the best correlated data to understand the user interest (and engagement) with each brand.
- Flawed data inputs are captured by the model such as FMCG correlations.
  - The allowlist filters out most of these so they won’t be visible. We’ll need to make some decisions on prioritising input data corrections depending on the impact on campaigns and/or other factors.
- We have introduced a `expected size` criteria in the model that adjusts the predicted brand volumes to the forecasted sizes based on historical interactions. This has the goal of better representing the brand volumes and give the user a better
  - Output scores are adjusted to ensure we meet expected sizes 

# Questions and Comments

If you have any additional questions or comments please leave them in the table below

| Author | Question | Answered | Answer | Answerer | Go Deeper |
| --- | --- | --- | --- | --- | --- |
| Sharifah Amirah | The material suggests we did a first iteration for July 2023 and possibly a second for Aug 2023? Are the results presented here based on 1 iteration or more? Did we consider running the model over a different time of year to see if that has an impact? Did we run some temporal (or other) analysis to review stability / consistency of model? | false | The results we show on this page were from a model which trained on Nov 2023 data. We compared that output with both Dec 2023 and Jan 2024. Results were virtually the same across those two months, so we can infer the predictions are at least valid for two months (if not more).  <br/>We also trained the model on July 2023 data to compare with Aug 2023 data. Those results are not present in this page, but they were also not too dissimilar to the ones we present here. We have not done that for further months, but we can expect that the model can be retrained and used throughout the year.  | Talvany Carlotto |  |
| Sharifah Amirah | Seems like we have about 60-70% reduction in latent space / number of brands & avg per user - are we comfortable with such a big reduction? | false | We model the number of brands to predict by counting a user clicking on a brand twice in the past month as a positive interaction. As you observe this is far fewer than BAU is generating as it is more lenient in how it defines a brand interaction (i.e. a single click), however during our exploratory data analysis we observed that single clicks were often noise rather than intentional brand engagement. It is for this reason we chose this sizing.  | Talvany Carlotto |  |
| Sharifah Amirah | If I’m reading the brand scores table correctly, it looks like the new model outperformed BAU on 3 out of 14 brands. What conclusions can we draw here? | false | You can not draw any conclusions from this sample, as it has been provided for illustrative purposes. However, those results relate to the known bias that the model currently has related with the brand sizes and the performance at item level. These are known limitations that we are currently working to improve (more info can be found in [this](https://coda.io/d/Data-Science-and-ML-Eng_dK5h4iVEEUo/Stage-3-Develop_suARo?utm_source=slack#_lu72Z) section). | Talvany Carlotto |  |
| Sharifah Amirah | Given that the new model is better at predicting some popular brands, what can we say about the utility of the model?  | false | Popular brands perform better for both BAU and VarEmb. This is expected in most ML models - the more data you have, the better the quality of your predictions. <br/><br/>In terms of the utility of the model, niche brands will have the correct expected volume across the user base, however they may be assigned to different users than those who end up engaging with them. Despite this, the underlying patterns and signal should be preserved to some degree so we expect that these brands still provide some level of insight in Insights Explorer. This qualitative evaluation of a selection of niche brands should be included in UAT prior to beta release.<br/><br/>  <br/>Whilst we have significantly improved the performance of niche brands during this iteration of R&D, we are not satisfied with this performance and we have work in progress to better represent those in the dataset.  | Talvany Carlotto |  |
| Sharifah Amirah | With a 0.01% uplift on historical brand engagement, can we really make the statement that the “model is excellent at preserving signal”?  | false | Yes, we can for a couple of reasons:<br/><br/>IE top winners has demonstrated that BAU Brands are preserving signal and the model performs as well, if not slightly better than BAU. <br/>VarEmb is capturing signal in a far more difficult way which makes equivalent performance all the more impressive. It is able to retain signal without directly mapping brands and generate user profiles that capture both recurrent behaviour and future novel behaviour. This is unlike BAU which preserves signal by mapping the user data directly. <br/><br/>So even if both of the uplift numbers were 0% indicating equivalent performance with BAU, I would still suggest this demonstrates excellent signal preserving capabilities. | Talvany Carlotto |  |
| Sharifah Amirah | How should we read the big difference in historical brand engagement uplift vs 30 day future prediction uplift? | false | We do not consider this a big difference. In both cases the performance of VarEmb compared to BAU is roughly the same. However, what this demonstrates is that the Variational Autoencoder’s compression and decompression architecture allows it to predict novel behaviour for a user which BAU is unable to do. This is a positive result. | Talvany Carlotto |  |
| Sharifah Amirah | Did we analyse brand distribution from a user perspective? e.g. are there cohorts of customers that score consistently high across brands, and perhaps co-relations of higher scores to browsing patterns? | false | The [user level results](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luTCe) analyse how the model performs across users at a macro level (as opposed to across brands). Due to time constraints, we did not go into subdivisions of user groups or further error analysis, however we intend to analyse specific user segments in the next iteration of Brand Model development.  | Talvany Carlotto |  |
| Sharifah Amirah | Can we confirm that the evaluation was ‘clean of’ the FMCG ‘spike’? | false | We cannot confirm this, however we have observed in the initial UAT presented by Daria yesterday that this is lessened. A qualitative evaluation of a selection of FMCG brands should be included in UAT prior to beta release. | Talvany Carlotto |  |
| Sharifah Amirah | Have we done any other ‘validation’ exercises e.g. using the brands as seeds into SMAC, looking at the characteristics of the brands that were better predicted vs those that are less well predicted etc? | false | We have not done any Audience Maker validation as yet. However this has been considered and Row 18-20 in the [UAT plan](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_lu8hZ) detail three expansions that are planned for investigation. <br/><br/>Further analysis at Brand level has also been considered. You can find some ideas for analysis we intend to do in the next iteration of model development [here](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luNjt).<br/><br/>We welcome discussing these plans and any suggestions for further analysis.  | Talvany Carlotto |  |
| Sharifah Amirah | If we have time, or if already available, pls can we be reminded on why we selected VAE and why we think it’s the better model to use? I believe we also looked at Recommender and Graph | false | VAEs were chosen for their bigger potential to capture complex signal over the other approaches and we have a high level explanation of VAEs [here](https://coda.io/d/_dK5h4iVEEUo/_suitU#_lukwV).<br/><br/>There isn’t any documentation at hand on this topic but happy to set up a meeting to discuss further. | Talvany Carlotto |  |
| Andy Cole | In this chart, BAU is identified as providing 65% ‘incorrectly identified brands’, It should be clarified that the definition of an interaction being 2 or more sessions in the period could be playing a significant part in the definition of ‘incorrect’. <br/><br/>Given that BAU is a direct attribution ‘model’, i would be keen to understand how much of that 64% is because a user only clicked once vs actual volativity between the training period (i.e user interacted in november) and evaluation period (user didn’t interact in december)<br/><br/><br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-vHy5d0Yk8w/6598d0b48796452b1d1c93accf9a550feadfa40c2a62e7780f4cefe23f80ba6a3e13b602f7557b2da9d3e483cfd88f379536b6ff56ab82dc0e812eed83b843aec1e4572d89deabb37f36013ccb7afc9093175043c0b4f3602ddc46df3fe2033e843cb5e1) | false |  |  |  |
| Andy Cole | Question previously asked in the dry run: It would be great to have some clear visual showing how much the precision, recall and F1 scores vary for both models by brand when ‘predicting’ the training period interactions and predicting the assessment period interactions. Similar to above this would provide a sense of the effect of volativity over time vs overall capabilities of the model. I suspect that there would be substantial differences in volativity by both brand size and brand ‘category’ | false | We agree. This analysis is planned as part of the next iteration of model development.  |  |  |
| Andy Cole | Does the fact that performance on ‘novel behaviour’ is so low highlight that the model is not actually predicting behaviour but actually just providing a noiy low-fidelity reproduction of the existing data (e.g like a very low bitrate mp3 file)? If we assume novel behaviour is only novel for the individual user, why are these results so low?<br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-DTQQ1665DQ/7c5568d0114b5f09031ce831ddddb84c80bc8ebe4e43cac3835942c427af27605bfa3ac2646653b21d32536d3ac349c9e4ef779e4d6056f58df1cc390233194eb3158f65ac00458a88a8d8ef5c9f626f2ddf5ae15cbdf3ff3f403b7d367e1318297ba2b0) | true |  |  |  |
| Andy Cole | In the novel/recurrent sectionl, I’m not sure what we should be comparing this table with<br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-uaUNgKkBwu/761b1d66347c5ec1c1c1ae670b9e5b1a05053fbd12ff46716921791aa317ce878924973edfa9415b157f5da25fbd6647bd5f6c5d4026206a3a25c3faedbf314f0f4b171e245cecd5087c8c9fa9b4ade08c509f5cac95f597792155be0baa8816e6ac43a3)<br/><br/>If it is this table (the main recurrent behaviour performance table) how can both models be better at predicting the future than at reconstructing the present?<br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-y4UVWWmU4S/34d12062cf6734c0dc1fee9c0a1755399301b2214c85d6e2733f5e374187103b60ebb9e70754abe99e157e97ff8abfa861a4f4446ff652aae6d80a48c3844b4e9f85963209e66ea40901f3cc335a678a4bfef17f48e39a2727abd438ddb78caeb3a96f20) | true |  |  |  |
| Andy Cole | As recognised by the team, i think the challenge is here is balancing the treatment of the small vs large brands. I suspect we need to do more thinking around the significance of an interaction.<br/><br/>for a large brand, such as Wlmart, two interactions in a month is wholly insignificant i.e. someone who lands at [Walmart.com](Walmart.com) only twice in a month is probably pretty uninterested in Walmart.<br/><br/>However for a small brand, the significance of even a single interaction could be quite profound. For example a visit to a local business to send some feedback for example could be a valuable signal. <br/><br/>I’m aware that the team are looking to do more work to ensure smaller brands are appropriately represented in the predictions - i wonder if some smart modification/weighting of the interpretation of the ground truth in some way might play a role.<br/><br/>My main concern is still around the extremely low recall that is universal across small brands. This snapshot of brands around the 500k mark highlights the issue well.<br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-aXTyzJUD2D/1b070c6479110750bbe457bb2be1dbc98bbedc150d434b2a7e1361e04457a5c4f8a6e835cb850ddc2f0fa7f23247010ee19e6116945f3956560bb5b22eb3d45cc7522793e3a26f872894b6b8bcb31401a52b841acc642ad445696adaed77220f7c2a5153)<br/><br/>The majority of the brands have sub-10% recall, meaning that of the e.g. 500k people that actually engaged with the brand, the model is finding less than 50k of them. The smaller brands get, the bigger this problem becomes. Some sort of ‘balanced ground truth’ could help in this regard  | false | That’s absolutely right. We will be looking into how we can increase performance, especially recall, on those smaller volume brands. Keen to hear your thoughts on how adjusting the ground truth could improve things.  <br/><br/><br/><br/>Some of the experiments we would plan to explore are:<br/><br/>**Brand level model performance** - We have identified a few points to improve the overall metrics at brand level. The main ones are:<br/><br/>Over/undersampling - Since we are only training on a fraction of the data we have available it will be really easy to over sample niche brands to generate more signal for them in the model. We can also dampen the effect of the popular brands where necessary.<br/>Weight balancing  - Implement a weight balancing approach in the cost function that the model uses to optimise the patterns in the data. This can efficiently (from a computational and design perspective) balance the impact of the low and high volume brands in the model performance.<br/>Regularisation - Improve the regularisation of the model to minimise the chance of overfitting allowing the model to train for more iterations and capture more complex patterns.<br/>Dynamic recall/precision thresholding -  to increase the recall and decrease the precision of the brands that aren't performing as well. We can work collaboratively with CS team to define appropriate thresholds.<br/><br/>**Overall VAE architecture** - We can explore and change the model architecture to try and make the model learn more from the data.<br/><br/>Embedding size - We trained the model with 10M users (10x the amount in the current model) but didn't see much improvement. This suggests that the size of the embeddings (50d) could be too small to capture the complexity of the data.<br/>Encoder and decoder models - We have used a small number of fully connected layers. We could expand this architecture to further layers or even more complex ones to allow the model to learn patterns it is not able to currently. |  |  |
| Andy Cole | It would be useful to understand what the sub-70% precision and recall populations look like here:<br/><br/>![image.png](https://codahosted.io/docs/K5h4iVEEUo/blobs/bl-FGEA0hvbmo/a8d6b3bfca828edc8c5cf5992cc98fd78de572aa8cfca9f9050298f88407e5173c9b2f1025f1e5144bee8843fa9b59d5d88498e9de719384e599024cbf2fc45fa55c12b73fa0abe10c72973a8c345bfad7f6210f6c3071d7c4ef63ed383bbf5d9ddf2216)<br/><br/>I know that wasn’t the purpose of this table, but given that nearly 98% of users have an overall recall of below 70%, it would be interesting to see the volumes of people where the predicted profiles look almost entirely unlike the actual profiles | false |  |  |  |
| Andy Cole | The main go/no go consideration for me is the impact of the 3bn predictions vs 10bn BAU predictions. What does this mean in how manhy brands fall below the size threshold for SMAC expansions? | false | [Andy Cole](mailto:andy.cole@intenthq.com) can you clarify what the size threshold is for SMAC expansions please.  |  |  |
| Kalin Kirev | How many months of historical data is used to generate VarEmb?  | false | We use three months of data to train a model (a full refresh). Additionally, one of the advantages of the model is that you can continue training the previous model therefore we will iterate across time retraining and improving the model |  |  |
| Kalin Kirev | What are some of the other insights that would be based on the VarEmb | false | We have extracted embeddings from the VarEmb and are exploring how to use them for topic modelling (work led by maciej). If we establish that they are able to do that then we have the possibility of providing these user-context embeddings directly to VZ to use as features.  |  |  |


## Final sign-off for productionisation & UAT

Please indicate your final sign-off by clicking the button below

As a project stakeholder I **agree** with the presented plan and I **support** productionising and UAT of the model Kalin Kirev, Karina Gorasia, Chris Schildt, Eddie George, Sangram Reddy, Andy Cole, Courtney Dowd, Kumutha Swampillai, Daria Barbalata, Aaron Schick, Rachel Yeomans, Sharifah Amirah, Talvany Carlotto, Sebastian Martins

As a project stakeholder I **do not** support productionising and UAT of the model as presented above 



# Develop Gate meeting

Develop Gate meeting held at: March 6th 2024

Meeting recording: [Link](https://drive.google.com/file/d/1eNjwZ4Ke7mOTdusuf1x7dvAGU89v8b5k/view?usp=drive_link)



# Instructions for filling this document

The Develop phase is where most of the Data Science work happens - you build and evaluate the solution in an iterative way.

Most of the artefacts required only at the end of this stage, to asses whether the solution addresses the business problem stated in the Shape stage and is fit for productionisation. However, it is a good idea to fill the documentation as you go along, especially recording the experiments and keeping your code in version control.

Feel free to delete or collapse this section after it’s no longer needed

## Code base

The solution code base should be version controlled, ideally with frequent commits - even if it consists only of Jupyter/Databricks notebooks. Add the link to the relevant Github repository [in the field above](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luUe9).

[Link to a template/example repository?]

The repository should contain:

- A Readme file
  - How to install (if relevant) and run the solution
- Frozen requirements:
  - Python version
  - All the relevant dependencies with the used version
- (ideally) Example:
  - Dummy example to run model (without need of running on customer data)
- All the code relevant for the implementation of the solution
  - Docstrings
  - A clear end to end process to run the solution. Ideally there should be only 1 point (file) that can run the full solution
- (optional) tests

## Model documentation

The best way to record the solution documentation, including experiments and the Model Card, is to use the existing [https://coda.io/d/_dK5h4iVEEUo/_su3j-](https://coda.io/d/_dK5h4iVEEUo/_su3j-).

- If the project is an improvement or iteration of an **existing model,** find the appropriate page in the Model Catalogue and paste the link [in the field above](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luCtu)
  - Try to also add links to the latest Model Card and to the relevant Experiments
- If you’re starting work on a brand **new solution**, you can create a new page in the Model Catalogue, by [navigating to this page](https://coda.io/d/_dK5h4iVEEUo/_su3j-#_lu6mf) and clicking the big green button

Alternatively, you can just use this page, especially if you expect the solution to be simple and not requiring an extensive documentation. In this case, feel free to create the necessary sections below and link to them in the summary at the top of the document.

# Experiment documentation and model evaluation report

This should answer why do you believe that the model is solving the problem and should be deployed.

Experiment docs → document internal steps, to make sure we record failings and successes (even if we don’t reach deploy stage).

Model evaluation report → final results for the problem you were trying to solve.

Click here to create a new experiment sub-page



## Stage gate checklist

**Action:** For each of the answered questions (marked as “DS completed), all stakeholders should indicate whether they are satisfied with the answer by clicking the “Stakeholder sign-off” button. The best time for this is during the scheduled Develop Gate meeting but it can also be completed offline.

| Section | Name | Required | Notes or link | DS completed | Stakeholder sign-off |
| --- | --- | --- | --- | --- | --- |
| Solution documentation | Did you complete the Model Card with necessary information? | Required | /_suTf_GH6 | true |  |
| Solution documentation | What dependencies (ML Libraries/Frameworks) do you have? | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | What Machine Learning techniques did you use? Did you rely on any particular ML libraries/frameworks | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | If appropriate, what loss function did you use and why? | Optional | [Talvany Carlotto](mailto:talvany.carlotto@intenthq.com) some of our stakeholders might have an interest in this. I’ve been asked how we’re optimising the loss function many times | false |  |
| Solution documentation | How would you improve performance or effectiveness of the model in future iterations? | Optional | Addressed under next steps [here](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luWRD). | true |  |
| Solution documentation | How are you obtaining/sampling your dataset? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | What evaluation metrics did you use and why? | Required | [Linked here.](https://coda.io/d/_dK5h4iVEEUo) | true |  |
| Evaluation report | If known, which features were the most effective/predictive? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | What hyperparameter tuning did you do and how did this affect performance? | Optional | [Talvany Carlotto](mailto:talvany.carlotto@intenthq.com) I think there was lots of this - any summary conclusions worth calling out?  | false |  |
| Evaluation report | What performance did you achieve on the validation vs the test set? | Required | [https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luXw_](https://coda.io/d/_dK5h4iVEEUo/_sut9n#_luXw_) | true |  |
| Evaluation report | Did you do any fairness/bias testing, if so what? | Optional | analysis to show the risk of replicating user behaviour [here](https://coda.io/d/_dK5h4iVEEUo/_supSN) | false |  |
| Evaluation report | Did you evaluate if the model performance would degrade over time, if so how? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | How do you derive business value/impact from your model performance and what is the estimated impact? | Required | [Write the answer or link to relevant section here] | false |  |
| Best practices | Can you confirm that the development work has been sufficiently documented so that your results could be replicated and the model can be maintained by a different team? | Optional | [Write the answer or link to relevant section here] | false |  |
| Best practices | Is the code version controlled in a GitHub repository, with a readme and a frozen requirements files? | Required | [http://github.com/intenthq/ihq-embeddings](http://github.com/intenthq/ihq-embeddings) | true |  |
| Best practices | Are there unit tests? How much code is covered? | Optional | [Write the answer or link to relevant section here] | false |  |
| Best practices | Have you filled in the QA Checks table? | Required | Not yet done and will be a large chunk of the productisation work - should this be part of the dev gate [Maciej Pfutzner](mailto:maciej.pfutzner@intenthq.com) [Kumutha Swampillai](mailto:kumutha.swampillai@intenthq.com) ? | false |  |




# RAW material



Verizon’s legal department deemed our descriptive Brand mapping methodology unsuitable for use in their cloud infrastructure. As part of the effort to deploy our full product offer on prem, they have requested modelled brands instead. Success criteria:

- **Optimise VAEs to provide unbiased synthetic data to maximally preserve the signal while ensuring we have high confidence that we are not replicating user brand engagement profiles.** To be reviewed on three tasks:
  - precision and recall of brand engagement predictions in the next 30 days
  - ability of the model to generate the input data (error of the model)
  - the likelihood of a predicted user brand profile replicating an existing user's brand profile.
- ~~**Apply business rules to the outputs in order to meet user expectations where the model doesn't directly do that.**~~ ~~e.g. expected user allocation volumes per brand;~~

More about this [here](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luz_R).



### Other docs

- [High level data flow diagram](https://app.diagrams.net/#G1x4KFxY42fOBGXFpzg2hQMuczOnUw7R2U) and [description](https://coda.io/d/Product-propositions_dgMDDph8PXa/Data-flow_suhg_#_lupMM)







To validate:

**Novel vs recurrent**

When splitting the analysis between known recurrent behaviour and novel user behaviour, we can observe the following:

- VarEmb model over-performs BAU approach on recurrent behaviour, while providing a new capability regarding identifying and therefore suggesting new brands that users are more likely to be interested and therefore engage in marketing communications. 
  - This new capability generates an opportunity for us and VZ to run different campaigns (and therefore messaging) for tailored to new customers (acquisition) vs targeting current loyal (or existing) customers to a brand (retention) while working with partners.



**NOTE**: these results are currently under validation, but if holding truth this means that the overall performance of VarEmb is reduced by trying to predict on novel brands (a much harder task), that in the case of reducing the effort of the model in this direction will provide a similar or higher performance than the current solution provided to VZ.





#