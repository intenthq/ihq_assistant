# Problem Definition and Purpose

# Background and Motivation

Shape Up: Predicted Brands V2[https://coda.io/d/Shape-Up-Product-Docs_d5hIdONEiOD/Modelled-Brands-V2-optimisation_surQS#_luZTl](https://coda.io/d/Shape-Up-Product-Docs_d5hIdONEiOD/Modelled-Brands-V2-optimisation_surQS#_luZTl) 

The current experiment focuses on improving the class imbalance performance and therefore the overall quality of the model, by experimenting with different loss functions that will enable the model to capture patterns in a more efficient manner.



**NOTE:** The current experiment combines a refactored VarEmb model (that include changes and optimisations in the model and the tracking of performance during training) and testing 2 key loss functions that adjust the learning process by:

- **Binary Focal Cross Entropy loss (BFC loss)**: balancing the weights of the brands based on their frequency.
- **Weighted Cross Entropy Loss**: having the weights of each brand as a parameter.

# Data Sources

The data sources used to assess these experiments are in common across all the work-streams and they are summarised [here](https://coda.io/d/_dK5h4iVEEUo/_suPaV#_luvm_).



**Nomenclature:**

- **BAU**: is the allocation model previously use in VZ account.
- **VarEmb V1**: is the current predicted brand model in production use in VZ account.

# Experiment Results

The following table summarises the results of the experiment:

**NOTE**: the median value is reported. Best performing model is highlighted in bold and yellow.

## User Level (Approved Brands) - Loss experiments
| Name | Precision | Recall | F1 score | NOTES |
| --- | --- | --- | --- | --- |
| BAU | 40.2% | 70.2% | 51.1% |  |
| VarEmb V1 | 56.3% | 52.9% | 54.5% |  |
| **VarEmb refactored V2 - BFC Loss** | 60.7% | 63.6% | 60.8% | Jobs:<br/><br/>**Train Model**:  [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/78724204943280/runs/43539793317138?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/78724204943280/runs/43539793317138?o=1409546164047445) <br/>**Predictions**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/249533736493299/runs/48773533852129?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/249533736493299/runs/48773533852129?o=1409546164047445)<br/>**Sizing:** [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/315128787278676/runs/631629720403904?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/315128787278676/runs/631629720403904?o=1409546164047445)<br/>**Calculate Assessment**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/316171590615493/runs/450385187604857?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/316171590615493/runs/450385187604857?o=1409546164047445)<br/>**Show Metrics**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/177059395668623/runs/481733692182778?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/177059395668623/runs/481733692182778?o=1409546164047445)<br/><br/><br/><br/>Distributions:<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> |
| VarEmb refactored V2 - Weighted Cross Entropy Loss - 1:20 | 61.8% | 58.7% | 58.3% | Weighted loss strategy:<br/><br/>**Fixed values**: 1 for all brands out of the allowlist, 20 for allowlist brands.<br/><br/><br/><br/>Jobs:<br/><br/>**Train Model**:[https://ihq-226109243659-vzw.cloud.databricks.com/jobs/78724204943280/runs/1054386315311878?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/78724204943280/runs/1054386315311878?o=1409546164047445) <br/>**Predictions**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/249533736493299/runs/48773533852129?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/249533736493299/runs/48773533852129?o=1409546164047445)<br/>**Sizing:** [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/315128787278676/runs/907520050168852?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/315128787278676/runs/907520050168852?o=1409546164047445)<br/>**Calculate Assessment**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/316171590615493/runs/277867199314419?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/316171590615493/runs/277867199314419?o=1409546164047445)<br/>**Show Metrics**: [https://ihq-226109243659-vzw.cloud.databricks.com/jobs/177059395668623/runs/456481624322143?o=1409546164047445](https://ihq-226109243659-vzw.cloud.databricks.com/jobs/177059395668623/runs/456481624322143?o=1409546164047445)<br/><br/><br/><br/>Distributions:<br/><br/><br/><br/><br/><br/> |


## Item Level (Approved Brands) - Loss experiments
| Name | Precision | Recall | F1 score | NOTES |
| --- | --- | --- | --- | --- |
| BAU | 9.4% | 38.4% | 15.1% |  |
| VarEmb V1 | 4.4% | 7.3% | 5.5% |  |
| **VarEmb refactored V2 - BFC Loss** | 14.7% | 21.4% | 16% |  |
| VarEmb refactored V2 - Weighted Cross Entropy Loss - 1:20 | 0.3% | 0.4% | 0.3% | Weighted loss strategy:<br/><br/>**Fixed values**: 1 for all brands out of the allowlist, 20 for allowlist brands.<br/><br/> |


**NOTE**: results are obtained from an out-of-training 1M user sample.

# Overall Conclusions and Outcomes

The experiment `VarEmb refactored V2 - BFC Loss` shows a significant uplift in comparison with `VarEmb V1`. The model also presents an overall higher performance than BAU, showing also a more balanced performance across precision and recall. 

The table below summarises **the difference of the winner solution against each model in absolute (proportions)**.

## VarEmb V2 performance uplift
| Name | Precision | Recall | F1 score | Text |
| --- | --- | --- | --- | --- |
| BAU - User level | **20.50% (51%)** | **-6.60% (-9%)** | **9.70% (19%)** |  |
| BAU - Item level | **5.30% (56%)** | **-17.00% (-44%)** | 1% (6%) |  |
| VarEmb V1  - User level | 4.40% (8%) | **10.70% (20%)** | **6.30% (12%)** |  |
| VarEmb V1 - Item level | **10.30% (234%)** | **14.10% (193%)** | **11% (191%)** |  |




# Live/Latest Solution 

Current version of the experiment is in a draft version and will require some extra DS work to be ready for productionisation.

- Links to:
  - Code Repo
  - Run Instructions/README.txt

# Future Work 

- Assess the impact on `privacy`.
- Analyse brand level performance and scores based on popularity (niche, mid, etc).
- Explore the impact of the current model with the best resampling strategy.
- Explore with custom weights per brand.

# CHANGE LOG

01/01/xx Changes - 

-