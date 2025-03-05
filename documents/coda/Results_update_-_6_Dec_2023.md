Summary of current results, assessing new predictions for 2nd iteration:

**NOTE**: the following analysis is only centred on `allowed brands` and using a sample of 1M users.

**Total number of brands in** `**allow list**`: 3_397

We are comparing 4 models:

- **BAU:** predictions using VZ production model.
- **tfidf_Nov28**: varemb tfidf predicting all the brands with threshold >= 0.5 (aka, current model deploy on IE Canary).
- **tfidf_sized_adjusted_50fix**: varemb tfidf size adjusted using 0.4 probabilities with a minimum of 50 brands per user.
- **tfidf_sized_adjusted_20fix**: varemb tfidf size adjusted using 0.4 probabilities with a minimum of 20 brands per user.

# Results - DRAFT metrics need to be re-done

**Number of rows predicted:**

- **BAU:** 74_826_962
- **tfidf_Nov28**: ~22M
- **tfidf_sized_adjusted_50fix**: 43_092_313
- **tfidf_sized_adjusted_20fix**: 26_241_170



### User level performance

**Precision:**



**Recall:**



**F1 score:**



### **Item** level performance

**Precision:**



**Recall:**



**F1 score:**





**Sizes and biases**

**min 50 model**

*Higher sizes predicted by model*



*Lower sizes predicted by model*



## Conclusions

- The model is centred in a reduced number of allowed brands. We need to explore why and define ways to extend the predictions towards all the allowed brands.
- The trade-off between precision and recall and the use of probabilities, doesn’t seem to be helping to improve performance (aka, those with slightly lower probability to the 0.5 threshold are not good indicators). We might want to explore ways of improving the model capability:
  - Expose the model to new users (for training new epochs with them)
  - Expose the model to new users that have interacted with these missing brands [and some sample of the others] (for training new epochs with them)

**NOTE**: These requires to have the ability of train from disk the model.

- If the model is biased towards activity (as expected, but need to check user level analysis to confirm)
  - Test the model with the min/max number of brands per users (although I'm not sure how much will the impact of these be). We might want to explore current distributions
- 



### Actions:

- Deploy for testing on Canary model: 



Things to explore, understand and improve:



Continue **analysis of biases/errors at user and brand level,** should be around that. Aka, we should be able to answer:

**1) Is the model more biased towards patterns on certain:**

- **At user level:**
  - activity? - user with many brands vs users with a few
    - Explore how many brands users have on input and on output?
      - Where can we find the biggest differences? what type of users are they?
        - check against age, gender
        - most common brands in those groups
  - Other things to explore:
    - age groups performances
    - gender performances
    - age + gender - performances
- **At brand level:**
  - What brands are missing in the output? Explore why?
  - What are the lowest and highest represented brands in the model? How different are their presence comparing against interactions data (input data)?
  - How is the performance of the model based on brand popularity?
    - Is the model doing better on popular sites, vs more niche?
  - How is the performance per brands in different categories (topics?): Explore brands distributions and sizes, Compare against interactions sizes.
    - FMCG brands.
  - Given a set of key `brands` use to query `top winners` , analyse:

**NOTE**: this could be done locally using a version of `top winners` or more manually copying the results from IE.

    - Are they brands that appear in a high frequency (aka, in 50% of all the queries done, the same brand was in the top brands)
    - What are the topics most frequently recommended based on the top brands?
      - How many topics within the same categories than the topics related to the brand in the original query?
    - (optional) Explore results when combining 2 brands.



**NOTE**: Exploring outputs and input data can be useful to understand results.

**2) Continue with model improvement:**

- See points mentioned on [conclusions](https://coda.io/d/_dK5h4iVEEUo/_suJsx#_luNGT)

**3) Continue improving sizes, iterate to have a better estimation of expected size per brand.**

**4) Test with a higher number, but 64M might not be necessary for now.**











Ticket: [https://intenthq.atlassian.net/browse/AIPROD-671](https://intenthq.atlassian.net/browse/AIPROD-671)

**Goal**: The original plan was to start working on error analysis, centred around brands. The usual expected workflow for this type of analysis involves:



Image from plan: [https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764570998217987&cot=14](https://miro.com/app/board/uXjVMrQgRm0=/?moveToWidget=3458764570998217987&cot=14)

It’s expected to learn things with the EDA, and extend (or discard) points from the analysis based on the learnings.

Giving the current time (less than 2 points), I was thinking to focus on an small subset of points, to start with (leaving the brainstorming and other steps for new tickets, however if there are a key learning that requires more attention, we should consider it and re-prioritise them). 

List of initial questions to answer with the error analysis:

  - What brands are missing in the output? Explore why?
  - What are the lowest and highest represented brands in the model? How different are their presence comparing against interactions data (input data)?
  - How is the performance of the model based on brand popularity?
    - Is the model doing better on popular sites, vs more niche?



**NOTE**: For this you might want to use the probabilities outputs of the model, the metrics and the input use to train the model.

**Recommendation**: I would recommend the analysis to be centred and focus only in the 3.5k brands in the allow list.

**Acceptance criteria:**

- Documented analysis answering the initial error analysis questions
  - with summary of findings and possible actions to address the issues find (if any)
- Code script to replicate this analysis with any new model, on github

**NOTE**: given the current time, I would suggest that implementing any possible fix will be part of future tickets.