**Prod. Model:** `VarEmb V2` 

**Process**: [https://github.com/intenthq/ihq-embeddings/blob/main/customer_pipelines/verizon/README.md](https://github.com/intenthq/ihq-embeddings/blob/main/customer_pipelines/verizon/README.md) 

**Run on:**

- **Branch:** `main` 
- **Model Path**: `s3://226109243659-vzw-data-science-longterm/seb/reference-data/ai_products/brand_prediction/models/varemb_tfidf/1M/all/finetune_varemb_v2_month_08` 

**NOTE**: update path whenever a most recent version is created



**Prod. Model:** `VarEmb V2`  (Date 12/12/2024). Run by [Manuel Fidalgo](mailto:manuel.fidalgo@intenthq.com). Run for 10h. 10 min.

**Process**: [https://github.com/intenthq/ihq-embeddings/blob/main/customer_pipelines/verizon/README.md](https://github.com/intenthq/ihq-embeddings/blob/main/customer_pipelines/verizon/README.md) 

**Training output:**   


```
** EPOCH 4 ==> TRAINING: {'precision': 0.98827696, 'recall': 0.9124231, 'prc': 0.9865564, 'loss': 2.5594223}, VAL: {'precision': 0.9856099, 'recall': 0.9374583, 'prc': 0.9908755}
```

**Run on:**

- **Branch:** `manuel_finetuning` 
- **Model Path**: `s3://226109243659-vzw-data-science-longterm/manuel-fidalgo/reference-data/ai_products/brand_prediction/models/varemb_tfidf/1M/all/finetune_varemb_v2_month_08_finetune_on_20241125_epochs_5/vae.zip`
- **Safetensors version:**