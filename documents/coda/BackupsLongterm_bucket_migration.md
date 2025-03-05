[See here for guidelines on how to complete this stage](https://coda.io/d/_dK5h4iVEEUo/_suaY6)

# Links to Develop stage Artefacts 

[See below for instructions on how to

- **Code repository**: [https://github.com/intenthq/causal_model](https://github.com/intenthq/causal_model)
- **Model documentation**: 
  - [https://coda.io/d/_dK5h4iVEEUo/_suJIQ#_luqXq](https://coda.io/d/_dK5h4iVEEUo/_suJIQ#_luqXq)
- **Model evaluation**
  - [https://coda.io/d/_dK5h4iVEEUo/_suA6J](https://coda.io/d/_dK5h4iVEEUo/_suA6J)
  - 

# Instructions for filling this document

The Develop phase is where most of the Data Science work happens - you build and evaluate the solution in an iterative way.

Most of the artefacts below are only required at the end of this stage, to asses whether the solution addresses the business problem stated in the Shape stage and is fit for productionisation. However, it is a good idea to fill the documentation as you go along, especially recording the experiments and keeping your code in version control.

Feel free to delete or collapse this section after it’s no longer needed

## Code base

The solution code base should be version controlled, ideally with frequent commits - even if it consists only of Jupyter/Databricks notebooks. Add the link to the relevant Github repository [in the field above](https://coda.io/d/_dK5h4iVEEUo/_suGNT#_luvdc).

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

- If the project is an improvement or iteration of an **existing model,** find the appropriate page in the Model Catalogue and paste the link [in the field above](https://coda.io/d/_dK5h4iVEEUo/_suGNT#_luGlm)
  - Try to also add links to the latest Model Card and to the relevant Experiments
- If you’re starting work on a brand **new solution**, you can create a new page in the Model Catalogue, by [navigating to this page](https://coda.io/d/_dK5h4iVEEUo/_su3j-#_lu6mf) and clicking the big green button

Alternatively, you can just use this page, especially if you expect the solution to be simple and not requiring an extensive documentation. In this case, feel free to create the necessary sections below and link to them in the summary at the top of the document.

# Model evaluation report

...

# Develop Gate meeting

Develop Gate meeting held at: [please fill the date]

Meeting recording: [please add link (after moving the recording to Google Drive)]

## Stage gate checklist

**Action:** For each of the answered questions (marked as “DS completed), all stakeholders should indicate whether they are satisfied with the answer by clicking the “Stakeholder sign-off” button. The best time for this is during the scheduled Develop Gate meeting but it can also be completed offline.

| Section | Name | Required | Notes or link | DS completed | Stakeholder sign-off |
| --- | --- | --- | --- | --- | --- |
| Solution documentation | Did you complete the Model Card with necessary information? | Required | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | What dependencies (ML Libraries/Frameworks) do you have? | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | What Machine Learning techniques did you use? Did you rely on any particular ML libraries/frameworks | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | If appropriate, what loss function did you use and why? | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | How would you improve performance or effectiveness of the model in future iterations? | Optional | [Write the answer or link to relevant section here] | false |  |
| Solution documentation | How are you obtaining/sampling your dataset? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | What evaluation metrics did you use and why? | Required | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | If known, which features were the most effective/predictive? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | What hyperparameter tuning did you do and how did this affect performance? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | What performance did you achieve on the validation vs the test set? | Required | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | Did you do any fairness/bias testing, if so what? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | Did you evaluate if the model performance would degrade over time, if so how? | Optional | [Write the answer or link to relevant section here] | false |  |
| Evaluation report | How do you derive business value/impact from your model performance and what is the estimated impact? | Required | [Write the answer or link to relevant section here] | false |  |
| Best practices | Can you confirm that the development work has been sufficiently documented so that your results could be replicated and the model can be maintained by a different team? | Optional | [Write the answer or link to relevant section here] | false |  |
| Best practices | Is the code version controlled in a GitHub repository, with a readme and a frozen requirements files? | Required | [Write the answer or link to relevant section here] | false |  |
| Best practices | Are there unit tests? How much code is covered? | Optional | [Write the answer or link to relevant section here] | false |  |
| Best practices | Have you filled in the QA Checks table? | Required | [Write the answer or link to relevant section here] | false |  |


## Additional questions and comments

If you have any additional questions or comments, not addressed at the Shape Gate meeting, please leave them in the table below

| Author | Question | Answered | Answer | Answerer | Go Deeper |
| --- | --- | --- | --- | --- | --- |
|  |  | false |  |  |  |


## Final sign-off for productionisation

Please indicate your final sign-off by clicking the button below

As a project stakeholder I **agree** with the presented plan and I **support** productionising the model 

As a project stakeholder I **do not** support productionising the model as presented above