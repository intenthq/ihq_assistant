Here are some example configurations used to run some of the scripts and the times they took. These were mostly run around October/2024.

**Configs:**

- **Databricks environment**: Databricks Runtime Version 14.3 LTS ML (includes Apache Spark 3.5.0, GPU, Scala 2.12)
- **python version**: Python 3.10.12
- **spark version**: Spark 3.5.0

| script | size | time | config | Notes |
| --- | --- | --- | --- | --- |
| create_data_sample | 1M | 55m | 1-20 workers i3.16xlarge |  |
| transform data input | 1M | 1h8min | 1-40 workers, i3.8xlarge |  |
| train/finetune model | 1M | 10h 18m | Single node: g5.8xlarge [A10G] · On-demand · DBR: 14.3 LTS ML (includes Apache Spark 3.5.0, GPU, Scala 2.12) · us-east-1a | Epochs=5<br/><br/>RUN_MODE = [<br/><br/>    RunMode.RELOAD,<br/><br/>    RunMode.TRAIN,    <br/><br/>    RunMode.SAVE_MODEL, <br/><br/>    RunMode.SAVE_TRANSFORMED_INPUT, <br/><br/>    RunMode.LOAD_TRANSFORMED_INPUT,  <br/>] |
| predict_varemb_at_scale | 65M | 12 hs | single worker g5.8xlarge | Using workflow with multiple parallel jobs (~20) |
| predict_brand_model_assessment | 1M | 37min | 1-30 workers i3.8xlarge |  |
| sizing_brand_predictions_topk_users | 65M | 5h | 1-50 workers i3.8xlarge |  |
| format_predictions_for_IE | 65M | 1h15min | 1-10 workers, i3.16xlarge |  |




P.S.: When training 1M users in Orange, each epoch took around 12h with similar configuration to VZ.