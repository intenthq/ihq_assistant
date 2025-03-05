# February predictions

I analysed the file generated with the November model using February data. The predictions I used can be found in the following path:

```
"s3://226109243659-vzw-data-science-longterm/talvany/ai_products/brand_prediction/predictions/20240225/varemb_tfidf/best_Feb15/E1_S2000/full_probs/002/sized_topk_users.delta
```

The problem of missing brands is much less significant in this file in comparison to the previous one. Before, we were missing a couple of hundreds of brands. Now, we only miss six:



- 'Verizon',
-  'Billboard',
-  'Verizon Digital Media Services',
-  'Tidal',
-  'Celine Dion',
-  'CBS Streaming'



Out of those, only two have wiki_ids in the mapper:



-  'Celine Dion',
-  'Verizon Digital Media Services'



Out of those two, Celine only had 10 valid data points in the input data, and the Verizon one only had 1:





The input data path I used there was this one:

```
"s3://226109243659-vzw-data-science-longterm/talvany/ai_products/brand_prediction/sampling_sets/random_True/user_size_1000000/input_20240225_target_202402/exclude_best_Feb15/refreshes/refresh_20240225/brand_total_counts_tfidf.delta"
```

I am not changing the allow list for now, as it does not seem we have any problems. We will keep track of this in the next file.