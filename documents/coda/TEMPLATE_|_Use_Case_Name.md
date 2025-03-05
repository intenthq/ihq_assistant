**Please do not change this template.**

**To use: right click on this page in the left hand menu > duplicate.**

# Problem Definition and Purpose

- What problem are we trying to solve and for who?
- Why does this problem matter and what value does solving this provide?
- What does success look like? 
- What is the appropriate evaluation metric for the model?

# Background and Motivation

- What is the background/context of the problem?
- Is there an existing solution?
- What is an appropriate baseline?
- Have other attempts been made to solve it?
- What led you to the current experiment? What’s your hypothesis?

# Data Sources

- What data is available for this use case?
  - Please note any data that you would like to have but is not currently available. 
- Where is the data stored?
- Was a specific cut of the data (e.g. a date range in the behavioural data) selected?
  - Why was this range chosen? Is it important to use the same data for all experiments, or should we use an equivalent cut on newer data?
  - If it has to be the same data, is that impacted by data retention policies?
- What query string / script was used to acquire the data?

# Exploratory Data Analysis

- Some general EDA on the training/input data if needed. 
- Some ideas:
  - Data shape
  - Profiling
  - Schema
  - Appropriate data quality checks

# Experiment Results

Subpage links for detail of different runs, hyperparameters and results for each model? Give them a unique name e.g. experiment: algorithm so they’re easily identifiable?

[ML Approach 1: Random Forest](https://coda.io/d/_dK5h4iVEEUo/_suiS6) 

[ML Approach 2: XGBoost](https://coda.io/d/_dK5h4iVEEUo/_suDu_) 

Then summary tables containing the relevant results can be surfaced here

The was done by creating a linked table and applying the filter “thisRow.Accuracy = thisTable.Accuracy.Max()”

(I like the idea of a “best result for each model” summary)

## Random Forest Summary 13
| Name | Num Trees | Max Depth | Accuracy |
| --- | --- | --- | --- |
| Random Forest | 100 | 7 | 86.3 |


## XGBoost Summary 13
| Name | Hyperparameter1 | Hyperparameter2 | Hyperparameter3 | Accuracy |
| --- | --- | --- | --- | --- |
| BASELINE - Best Random Forest Model |  |  |  | 86.3 |


# Overall Conclusions and Outcomes

- What is the overall result for this use case?
  - Have we changed the initial objectives of this use case, and how?
- How can this solution be deployed?
- What have we learned from this?

# Live/Latest Solution 

- How has this solution been productionized/implemented?
- Links to:
  - Code Repo
  - Pipeline Documentation
  - Run Instructions/README.txt
  - Model Container or Model Artifacts

# Future Work 

- What did we **not** manage to do here that we wanted to?
- What remains uncertain even if you don’t know how to address it?
- Given the results, what new experiments should we try in the future?

# CHANGE LOG

01/01/xx Changes - 

- Added flanges to future work section
- Included 3 additional experimental results
- Updated data sources to add x data sources
- Updated key links to additional documentation