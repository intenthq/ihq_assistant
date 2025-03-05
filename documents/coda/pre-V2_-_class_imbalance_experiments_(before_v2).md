Tests:

- **1M sample**



0) **Approach 0 - Bigger model, random over sample with replacement**

***Branch****: exp/class_imb_2*

*In this tests the following changes were done:*

*1) Increase the size of the nodes (keeping same number of layers)*





*2) Oversampling by cloning rows (aka, users) that have positive interactions with “small” brands.*

*See logic:* *[https://github.com/intenthq/ihq-embeddings/blob/exp/class_imb_2/customer_pipelines/verizon/predict_brand_pipeline_varemb_balanced_blocks.py#L663-L695](https://github.com/intenthq/ihq-embeddings/blob/exp/class_imb_2/customer_pipelines/verizon/predict_brand_pipeline_varemb_balanced_blocks.py#L663-L695)*



**User level scores**



**Item level scores**





**top brands**





**Results**: Poor performance



1) **Approach 1.a - Bigger model, random over sample with replacement dropping high volume in oversample**

*Branch: exp/class_imb_3*

*In this tests the following changes were done:*

*1) Increase the size of the nodes (keeping same number of layers)*



*2) Oversampling by cloning the users that have interacted with brands, but removing from their oversampling interactions the* *[high volume brands](https://github.com/intenthq/ihq-embeddings/blob/exp/class_imb_3/customer_pipelines/verizon/predict_brand_pipeline_varemb_balanced_blocks.py#L578)* *(still keeping the original rows). So, the model will see the same user but one with all the brands and the other (or others) without the high volume brands.*

*3) Training on ~5M rows*

See sampling logic: [https://github.com/intenthq/ihq-embeddings/blob/exp/class_imb_3/customer_pipelines/verizon/predict_brand_pipeline_varemb_balanced_blocks.py#L664-L698](https://github.com/intenthq/ihq-embeddings/blob/exp/class_imb_3/customer_pipelines/verizon/predict_brand_pipeline_varemb_balanced_blocks.py#L664-L698)



**User level scores**



*Original scores:*



**Item level scores**



*Original scores:*





**top brands**





**Results**: Slight improvement item level (increase of F1 score 1.1% absolute, 20% relative), but decrease at user level.



1.b) **Approach 1.b - Bigger model, random over sample dropping high volume in oversample**

*Branch: exp/class_imb_3b*

*Same as 1.a, but using MSE loss instead of BinaryFocalCrossEntropy*

*In this tests the following changes were done:*

*1) Same logic as 1.a*

*2) Use MSE loss*



**Item level scores**





**Results**: Poor performance



2) **Approach 2 - under/over sample by brand volumes**

*Branch: exp/class_imb_1*





**Item scores**





**Top brands**





**Results**: Poor performance



3) **Approach 3 - Top 10k users for ~all brands**

Having problems with scores super low.

**Results**: Not working.

4) **Approach 4 - Adjust model to run weighted MSE**

Having problems to scale using full dataset. Working on dummy dataset.

It might be relevant to explore if reducing the number of item might help.

**Results**: Not working.

## Distributions
| Name | F1 score >= 0.5 | F1 score >= 0.1 | F1 score >= 0.05 |
| --- | --- | --- | --- |
| BAU  | 300 | 2,181 | 2,721 |
| bfce_1M  | 78 | 1,300 | 2,044 |
| **Approach 0** |  |  |  |
| **Approach 1.a** | 57 | 1,185 | 1,788 |
| **Approach 2** | 37 | 925 | 1,539 |