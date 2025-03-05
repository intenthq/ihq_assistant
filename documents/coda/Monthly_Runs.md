We run our assessment metrics on a 1M sample every time we produce our monthly data. The documentation each monthly run is below.

Up until May 2024, these are results from V1 - the model which we trained on the November refresh. That model was used to infer on January data initially, and then sequentially also on February, March and so on.

From June 2024 onwards, the results are from V2 - trained using the March refresh.

From August onwards, the results are from V2 finetuned on each month.

The high level results for user and brand level are below. They were performed on a sample of one million users and assessed across users and brands. The diff columns are with regards to the January results.

## Refresh model performance (Median)

## User Level (Approved Brands)
| Name | Precision | Recall | F1 score | NOTES |
| --- | --- | --- | --- | --- |
| September | 70.5% | 72.9% | 70% | Using finetuned VarEmb V2 (month_08) |
| August | 67.7% | 74.1% | 69.3% | Using finetuned VarEmb V2 (month_08) |
| July | 70% | 71.2% | 69.2% |  |
| June | 69% | 73% | 69.6% | Using VarEmb V2 |
| April | 60.4% | 53.7% | 55% |  |
| March | 60.4% | 53.8% | 55.1% |  |
| Feb | 60% | 53.5% | 54.1% |  |
| Jan | 56.3% | 52.9% | 54.5% | Using VarEmb V1 |


## Item Level (Approved Brands)
| Name | Precision | Recall | F1 score | NOTES |
| --- | --- | --- | --- | --- |
| September | 32.6% | 32.6% | 32.5% | Using finetuned VarEmb V2 (month_08) |
| August | 29.2% | 45.2% | 32.7% | Using finetuned VarEmb V2 (month_08) |
| July | 29.6% | 29.6% | 29.5% |  |
| June | 26.8% | 36.1% | 28.6% | Using VarEmb V2 |
| April | 5.1% | 7.4% | 5.8% |  |
| March | 5.3% | 7.8% | 5.8% |  |
| Feb | 4.6% | 7.5% | 5.3% |  |
| Jan | 4.4% | 7.3% | 5.5% | Using VarEmb V1 |


## July







## June



## **May**







## April







April has very similar metrics to March. Not a significant drift yet. I wonder if this is an indicative that the model is not very seasonal, and what it is capturing are things which the user displays throughout the year.



## March









The results are overall pretty comparable, having decreased slightly in the February and increased slightly in March. If we look at the f1 scores, in February they **decreased** about **0.5% for user** metrics and **0.1% for brand** metrics, while in March they **increased** about **0.6% for user** metrics and **0.4% for brand** metrics. This is aligned with our expectations that results would not vary greatly when analysing a couple of months ahead. It is interesting that the March results are slightly higher, but this could be just randomness, as the difference is probably not statistically significant.

## February





## January







##