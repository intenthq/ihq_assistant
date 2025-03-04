**Updates**

Dev gate for optimisation held on Monday July 8th - optimisation results documented [here](https://coda.io/d/Data-Science-and-ML-Eng_dK5h4iVEEUo/Dev-Gate-V2_suU6v#_luGCp). Initial UAT performed [here](https://coda.io/d/Data-Science-and-ML-Eng_dK5h4iVEEUo/Defining-the-right-segments-and-expected-patterns-for-brands-QA_sutuj#_luDaa). June inferences have been provided to send on-prem in production for Verizon users to use (C-level decision).  
  
Final UAT report in progress, ETA by the end of July with a (retrofitted) launch gate expected to run sometime mid-August. These should result in prioritisation of further optimisation iterations.

Review meeting held on May 20th - [recording here](https://intenthq.zoom.us/rec/share/f_coX5EQIUDxRZ2nquW_6WroGhEfsqbZVEgnceZwmqiYBXgdglgezBDEjl5O3016.p2_Sgp0L_Uw8_X_Q). Decisions:

- The DS team will start working on the class imbalance problem described below.
- A subgroup of CS, DS & Prod will work in parallel to define the required QA. It may be enough at this stage to do the QA manually rather than automation as long as the right criteria are correctly defined - TBD.

# Background

We have delivered the first version of modelled Brands into Verizon. However, we have observed that the model performs on average better for popular brands (visited by the most users within the timeframe) than the least popular, low-volume ones - these get ‘predicted’ with very low scores and setting up a fixed score allocation threshold (e.g. > 0.5) would result in very low volumes of users per brand and more than half of brands not being ‘predicted’ for any users therefore missing from the Insights Explorer views altogether.

### Current State

The model does output scores for all brands per user, so to decrease the effect of popular brands observed in insights explorer (which show the number of users that we predict to be interested in each brand), we have implemented a dynamic thresholding approach where we increase or decrease the allocation score threshold for each Brand to meet the expected number of users for that brand. More about why this decision was made [here](https://coda.io/d/_dK5h4iVEEUo/Adjust-score-thresholds-dynamically_sug3_).

We consider the expected number of users per brand to be within a +/-5% range of the number of users that visited the brand’s domain at least twice in a day within the inference time-range (one month in this case) See more about why this ‘positive interaction’ criteria has been chosen [here](https://coda.io/d/_dK5h4iVEEUo/Positive-Interaction-Definition_suN8O). This results in Brands being of allocated to users even when the prediction scores are very low, therefore creating a long tail of brands where we’re not very confident in the quality of the predictions.

More about this model and quantitative assessment [here](https://coda.io/d/_dK5h4iVEEUo/Stage-3-Develop_suARo).

# Problem

Modelled brands currently carry an imbalance issue which results in high volume brands such as TripAdvisor having their signal boosted while low-volume brand signals are diminished (e.g. Hanes). This bias in the model reduces the accuracy and nuance of the insights consumed by users (in Insights Explorer). 

### Target Audience

Until we observe campaign performance we cannot strongly comment on the true quality of the predictions, but we do carry some highly likely risks:

- **Campaign managers** that need to use more niche brands in campaigns will likely notice the odd patterns displayed in IE when filtering for such brands and - if they don’t - their campaigns can underperform which would result in user dissatisfaction and negatively impact our revenue targets. Most campaigns are usually using Verizon partners that are of the high-volume/high-performance category which have been assessed to display really good/credible results in Insights Explorer, but there have been some campaigns in the past that used lower volume brands too, so we expect this to happen again, though less frequently.
- **Campaign managers and analysts** exploring their user base to understand target segments or look for opportunities may observe odd correlations which could significantly impact their trust in our data depending on the frequency of such observations. We don’t currently have many  frequent users, but we expect to increase this as the on-prem roll-out of Insights Explorer continues.
- **Data scientists** that use our brand features for developing internal models (e.g. churn or upgrade). Outside the bespoke churn features delivered outside of the insights explorer directly to AI&D (the Verizon data science team), we have recently uncovered a new opportunity to get more of our features used for modelling which could have a high impact on our revenue targets. Users can define a segment in Insights Explorer and use the ‘Request smart audience’ feature to send a request to AI&D for a specific campaign. Such requests go into the team’s backlog where they can explore the filters used in the segment criteria as relevant features for a particular campaign. This isn’t currently used, but as soon as we have more confidence in the quality of our brand predictions, the CS team would like to leverage this use-case. 

### Problem overview

There have been a number of odd correlations observed in the Insights Explorer, which we believe to be a result of the bias towards volume of visits per brand:

- A qualitative assessment has surfaced some ‘flawed’ brands, most of which are low volume and/or low performance ones - see more detail about this assessment [here](https://docs.google.com/spreadsheets/d/1-haofM1Ejio92rhpmGdbK7NIqDSAdxlT/edit#gid=1074588614).
- The CS team used to experience a healthy mixture of high and low volumes surfacing in the top winners view, whereas now they see results mostly populated with low-volume brands for some commonly used filters, often CRM specific to Verizon such as mobile plan options. The top winners view is meant to show differences between the segment explored compared to the rest of the Verizon user-base, so it’s not expected to see direct correlation with the view where results are ranked by number of users. However, seeing only low volume brands rank high in this view is considered odd, especially since the correlations can’t be easily justified.



- The CS team has also observed a number of these brands surfacing high in the top winners view for a few different segments which is also a sign that there might an issue, since you wouldn’t expect many different segments to surface similar insights. These are: Chime, ADP, Tilly's, Popmoney (this brand has also been discontinued, so it would be interesting to understand why we see it at all), Fashion Nova, Foot Locker, Vivint, Shein. Notably, for high ARPU(average revenue per user) filters, these show up instead of what was before mostly populated with luxury brands which - intuitively - make much more sense for people that spend more with Verizon.

While we believe the imbalance is likely to be the main flaw in the model causing these problems, we will need to assess this along the way to validate and it is possible that part of the scope will need a separate stream of work to fix.

# Appetite

Brands are one of our USPs and core models used for behavioural segmentation in Insights Explorer. Ensuring that we have the maximum performance of these models is crucial especially as their outputs are used as features for modelling efforts on the client side.

Strategically speaking, the embeddings model underpinning brands is planned to replace the way we derive all behavioural insight for new and existing customers. It is also meant to form the basis of our Large Behavioural Model (LBM). Any optimisations at this stage would likely cascade into better performance of other downstream models. Therefore, we believe it is critical to account for the imbalance in the model - not only to mitigate the existing risk we carry at Verizon - but also to ensure that further R&D efforts and downstream models are built on top of a strong foundation.

### Goals & Success

- We aim to bring the performance of low volume brands up to BAU levels, while keeping the risk of replicating user profiles at the same levels of the current version. Specifically measuring precision, recall and F1 scores of the predictions per brand against the defined relevant interaction criteria: at least 2 true domain visits per brand in the month after the one used for inference (e.g. if the inference is done for the month of March, we assess against April true visits to understand the predictive power of the model).
- Furthermore, we found that it’s important to consistently run the qualitative (top winner) assessment before the data lands in Insights Explorer in order to validate the quantitative assessment against how users experience and interact with these insights. We’ve identified a number of checks that we could automate, largely to see brands’ correlations with:
  - Demographic groups such as age, gender, affluence and ARPU/ARPA.
  - Other brands and topics that are considered similar in our topic hierarchy a.k.a. IHQ graph.



# Solution

We plan to address the class imbalance in the model training. Currently the model is trained on a statistically significant random sample of data. This random sample reflects the overall distribution of brands across users’ behaviours which does over-weight popular brands like Google and Netflix, so we plan on trying a few ways to mitigate this weight distribution, such as (but not limited to):

- Balance the input data: we can adjust the sample data to control for the distribution of brand volumes.
- Adjust the model parameters to give more weight to less popular brands in the training set in order to account for the volume difference.
- More specific next steps being planned [here](https://coda.io/d/Data-Science-and-ML-Eng_dK5h4iVEEUo/Class-Imbalance-Plans_suQU5#_luEEq).

For automating qualitative (top winners) assessment we could use either the DS assessment script or the DB QA dashboard.

- We will need to work with the VZ QA team in order to establish which is the quickest and most usable option considering the qualitative metrics will need to be checked by the CS team.
- **Notably, including this assessment into the scope of this project implies either having a 2nd person dedicated to this work or extending the timeline** from min. 6 weeks required for optimisation work to min. 10 weeks to include the assessment.

## Rabbit holes

**Automating the qualitative assessment:**

- **Some CRM datapoints that are of value (e.g. FWA) are not available off-prem**. If these are required, we will need to go through a stage of getting these data sets approved for transfer off-prem or, if this isn’t possible, accept the risk of not checking these correlations before the data lands on-prem. We could also negotiate proxy data points that are available off-prem and help reduce this risk.
- There is a risk that attributes used for qualitative assessment are never sufficient as we’ve seen this in the past (e.g. we implement correlation with age, gender and affluence groups, but when the team goes through the assessment they don’t find it sufficient for having confidence in the output). This can increase timelines; it would be ideal if we could get some **dedicated capacity from CS stakeholders to decide on the min. number of expected meaningful checks** that allow us to more easily QA the outputs while being mindful of effort/time-to-value in order to reduce this risk.

## No goes

**P****roductisation** - considering current efforts to create a pipeline to run inference on a monthly basis using the existing brand model, deploying the new model in production should be a fairly trivial task. However, we do need to test that the outputs match expected baselines before releasing the new model in production and such tests can take an additional ~2 weeks depending on the problems found when running the tests.

**‘FMCG’ data correlation problem** - we have observed a number of odd correlations even in the legacy BAU version of our brand insights, largely associated with FMCG because most ‘odd’ brands observed belong to that category, but there are some that don’t. Because the legacy BAU isn’t actually modelled, but rather a near-true representation of user visits, we have identified that this problem is in the source data where we’re likely getting some ‘ghost’ interactions which generate artificial correlations down-stream, most likely influenced by the use of ad technology (e.g. if a few brands are using the same ad-tech provider, we’ll likely see correlations between these brands that aren’t truly reflective of user behaviour. 

- We believe this should be reduced as the model is meant to pick up on the most relevant patterns in the data and we have seen evidence of this in the first iteration, but limited to the higher-volume brands. This effect is still present for some brands and we think this should get reduced as a result of the optimisations planned in this iteration, but this is a wild-card as the flaws exist in the input data and we cannot fully control what the model learns and how it differentiates from relevant or non-relevant interactions. Once we reach optimal performance as seen above, we can re-assess if the problem is still observed and create a new stream of work to optimise for this.
- We are aware of the existing ADS fix for legacy brands which we could use to train the model instead and alleviate some of the ‘FMCG effect’, but we believe addressing the problem outlined above is of higher priority and we don’t want to introduce 2 different variables as that will make it difficult to know which of them actually solved the problem. If we find that the problem still exists post-optimisation, then this is likely going to be one of the things we try next.



Done reading? Click here. → 

 I’m aligned with the problems & goals

 I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Answer | Answerer | Vote | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| false | do we think the recurring appearance of brands like ADP and popmoney (which no longer exists as a service) is also due to the imbalance issue? | Sharifah Amirah | We already have a view on Popmoney, their domain still exists, but it redirects to Zelle. We probably need to change this all the way up to where we aggregate the data coming from VZ so that the domain correctly points to Zelle. I suspect the brand exists in legacy brands too though I can’t login to Citrix to check.<br/>Some of the other brands like ADP that come up frequently for key demographics do not fall under the low volume/low performance category, but we believe that by increasing the coverage of lower volume brands, these top winner views would display more diversity.  | Daria Barbalata |  |  |
| false | is the imbalance issue also attributing to the fact that we you filter high value customers, no luxury brands appear? and when high churn risk customers are filtered for, no speed test sites appear? | Sharifah Amirah | We can’t know for sure until we actually test the fix. None of this is guaranteed, but we believe it is likely. <br/>For example, on the point that luxury brands are expected to over-index for high value customers, we found ~10 low volume luxury brands that - when increased - could be indexing higher therefore making the top winner view more useful. | Daria Barbalata |  |  |
| false | this assessment appears to have been focused on brand-brand co-relation. please could we include interest to brand, demographic to brand and most importantly key VZ attributes to brand? worth noting that this is how the client would use brand... | Sharifah Amirah | Yes - detailed [here](https://coda.io/d/_d5hIdONEiOD/_surQS#_lum_n). There is a pretty important risk about VZ attributes detailed [here](https://coda.io/d/_d5hIdONEiOD/_surQS#_lurqJ) - I’ve asked some questions of the team to help us clarify which data points to check and if they are available off-prem or how to get them.<br/><br/><br/><br/>During the UAT, We have also included tests using user’s demographics. | Daria Barbalata |  |  |
| false | would like to understand if we could move faster pls | Sharifah Amirah | Depends what we’re willing to move out of scope - if we limit to class imbalance, descope further assessment automation and add another person to the stream, we might be able to.  | Daria Barbalata |  |  |
| false | Please can someone help me understand why we wouldn’t include this fix? [ADS FMCG fix] | Sharifah Amirah | We could, but:<br/><br/>We would need to test it separately from the class imbalance to have traceability over what fix works for what problem. If we were to do both things at once and find a problem, we wouldn’t know which of them caused it. Or even if there’s no problem, which of them fixed it.<br/>Testing separately would increase timelines here.<br/>The fix would for sure not solve the model bias problem and we believe that to be the highest priority<br/>As recognised, I believe, by all parties, that fix requires a bit of work to ensure it holds over time and data changes, unless something changed there that I’m not aware of.<br/><br/><br/><br/>In addition, when building the 1st iteration we explore the ads fmcg fix and we apply learnings/logic use for the fix to optimise the predicted model.<br/>From the UAT analysis, we have found a 2% of cases (1/44) where the appearance of FMCG brands where high (**more than 3**). | Daria Barbalata |  |  |
| false | The two goals seem a bit independent to me. The first one is about improving the performance. It's clear to me and it will involve coming up with solutions to make the model better. This second one is about having a better assessment pipeline, which by itself will not give us a better model, but only a tool to give us a better understanding of the model. As I see it, those are different problems to solve, and I am quite confident that the first one would take the full six weeks. Do we really have to group them together in the same shape-up? | Talvany Carlotto | We can discuss alternatives for assessment (e.g. one thing I’m exploring is if we could use the DB dashboard to do this to a reasonable confidence level). But the reason I think it’s important to include assessment here is because it seems like we weren’t able to correctly identify the issues ahead of time and we risk releasing inferences to users without fully understanding the impact. <br/>I take your point on timelines though and we should make this clear to discuss possible trade-offs to meet desired timelines. | Daria Barbalata |  |  |