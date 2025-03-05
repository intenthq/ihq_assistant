Two things are considered on this page:

1. What is the bug we faced in this calculation and what is the fix/next steps?
2. What does novelty mean when modelling?

# What is the bug?

According to this run where we first identified the issue where max > 1 for some metrics:

[https://ihq-226109243659-vzw.cloud.databricks.com/?o=1409546164047445#job/177059395668623/run/670437963465901](https://ihq-226109243659-vzw.cloud.databricks.com/?o=1409546164047445#job/177059395668623/run/670437963465901)

BAU and Varemb are both fine for max <= 1 in unfiltered assessments (both user and item)  
BAU and Varemb both suffer from max > 1 in filtered (recurrent) assessments (user and/or item)  
(those exact summaries with issues below).

We found two problems:

1. duplicates in the preds
2. user metrics writing to item metrics location so summaries were incorrect

I reran the metrics with to fix bug #2 where user metrics were writing to item metrics and this fixed all the item metric related outputs, but not the user metrics ofcourse (I made no change there).

  
I don't know if the duplicates problem will fix the top ones for both VarEmb and BAU. But in any case, that should be fixed further up the pipeline, so, instead of continuing and adding some messy fix here and writing and deleting files - we are adding a line in the assessment notebook saying "there are a minor number of duplicates in the preds to investigate so you may see max >1 in some metrics)”, putting a pin in this to revisit when it becomes a priority, and closing out. 

```
BAU_001_user_recall_score_novelty_recurrent_novel_items
varemb_tfidf_user_f1_score_novelty_recurrent_novel_items
varemb_tfidf_user_precision_score_novelty_recurrent_recurrent_items
varemb_tfidf_no_blocklist_user_precision_score_novelty_recurrent_recurrent_items

BAU_001_item_recall_score_novelty_recurrent_novel_items FIXED
varemb_tfidf_no_blocklist_item_precision_score_novelty_recurrent_novel_items FIXED
varemb_tfidf_no_blocklist_item_f1_score_novelty_recurrent_novel_items FIXED
```

*Breakdown of summaries can be found at the bottom of this page.*



We could even tidy everything further IMO because we don’t need both unfiltered and recurrent for both BAU and VarEmbs - it gets confusing to explain (we only really need bau-unfiltered and varemb-recurrent to compare the model novelty performance). This leads to the question...

# What are we trying to learn from novelty split? What do we really need?

This is thinking about what we really want to learn from novelty split.

For this calculation we have df_pred (predictions) and df_target (generated on one month data with recurrent filter applied) - but we also df_prev (dataset with previous interactions - this usually is the `df_input`), which flags recurrent interactions (something a user has interacted with before). 

**For df_prev, do we want to apply the same recurrent filter we applied to the input data in the modelling?**

- If yes: this means we have the same input data for modelling and for novelty assessment - so if the model flags something as novel to a user, it may not actually be novel, as maybe it was something we excluded from the positive interactions and user actually has interacted with before.  
It answers: “how well does the model predict things that the model saw vs haven't seen.”
  - Pros: 
    - Highlights the model was able to capture things very close to the user interest
  - Cons: 
    - Doesn't capture the reality of all new behaviour  

- If no: we make sure we only capture the "true" novel behaviour for a user (positive interactions be damned) so we are testing the predictive capability beyond what we know from the whole month image of user behaviour.  
It answers: 🤔...
  - Pros: 
    - We get the true 'new' to user behaviour that the model identifies
    - Makes more sense to business when they understand the term "novelty" and also then we are also not just recommending a brand a user actually interacted with already but was just "hidden" by our definitions
    - When we think of it from item assessment, we get actual new users to a brand - if you want to market to new people  
(instead of marketing to a "hidden" user you actually already did once but was hidden by positive interaction)...
  - Cons: 
    - We lose some information between the positive interactions model input and what is novel to a user. 

























## Breakdown of the impacted summaries

```
Impacted summaries:

varemb_tfidf_no_blocklist_user_precision_score_novelty_recurrent_novel_items
+---+---+------+------------------+---+-------------------+------------------+---------+
|min| q1|median|                q3|max|               mean|            stddev|n_missing|
+---+---+------+------------------+---+-------------------+------------------+---------+
|0.0|0.0|   0.0|0.3333333333333333|2.0|0.17700010373214276|0.2719022689507057|   188049|
+---+---+------+------------------+---+-------------------+------------------+---------+

BAU_001_user_recall_score_novelty_recurrent_novel_items
+---+---+-------------------+-----+---+------------------+-------------------+---------+
|min| q1|             median|   q3|max|              mean|             stddev|n_missing|
+---+---+-------------------+-----+---+------------------+-------------------+---------+
|0.0|0.0|0.06451612903225806|0.125|2.0|0.0881359714709017|0.10573256733941279|     7666|
+---+---+-------------------+-----+---+------------------+-------------------+---------+

varemb_tfidf_user_f1_score_novelty_recurrent_novel_items
+---+---+------+----+---+--------------------+-------------------+---------+
|min| q1|median|  q3|max|                mean|             stddev|n_missing|
+---+---+------+----+---+--------------------+-------------------+---------+
|0.0|0.0|   0.0|0.08|2.0|0.049383021437181415|0.07242301678898007|   130307|
+---+---+------+----+---+--------------------+-------------------+---------+

varemb_tfidf_user_precision_score_novelty_recurrent_recurrent_items
+---+-----+--------+--------+-----------+--------+---------------+---------+
|min|   q1|  median|      q3|        max|    mean|         stddev|n_missing|
+---+-----+---------+-------+-----------+--------+---------------+---------+
|0.0|0.775|0.863636|0.928571|1.016666666|0.834944|0.1378557841273|       74|
+---+-----+--------+--------+-----------+--------+---------------+---------+

varemb_tfidf_no_blocklist_user_precision_score_novelty_recurrent_recurrent_items
+---+----------+-----------+-----------+------------+-----------+-----------+---------+
|min|        q1|     median|         q3|         max|       mean|     stddev|n_missing|
+---+----------+-----------+-----------+------------+-----------+-----------+---------+
|0.0|0.76923076|0.863636363|0.939393939|1.0666666666|0.841082359|0.135256442|       68|
+---+----------+-----------+-----------+------------+-----------+-----------+---------+






Below this line are those now fixed after fixing user to item write bug.
Originally problematic summaries:

varemb_tfidf_no_blocklist_item_precision_score_novelty_recurrent_novel_items
+---+---+------+------------------+---+-------------------+------------------+---------+
|min| q1|median|                q3|max|               mean|            stddev|n_missing|
+---+---+------+------------------+---+-------------------+------------------+---------+
|0.0|0.0|   0.0|0.3333333333333333|2.0|0.17699532660641445|0.2718988827250168|   188027|
+---+---+------+------------------+---+-------------------+------------------+---------+

varemb_tfidf_no_blocklist_item_f1_score_novelty_recurrent_novel_items
+---+---+------+----------+---+--------------------+------------+---------+
|min| q1|median|        q3|max|                mean|      stddev|n_missing|
+---+---+------+----------+---+--------------------+------------+---------+
|0.0|0.0|   0.0|0.08333333|2.0|0.049716842351442525|0.0821482927|   188027|
+---+---+------+----------+---+--------------------+------------+---------+

BAU_001_item_recall_score_novelty_recurrent_novel_items
+---+---+-------------------+-----+---+-----------------+------------------+---------+
|min| q1|             median|   q3|max|             mean|            stddev|n_missing|
+---+---+-------------------+-----+---+-----------------+------------------+---------+
|0.0|0.0|0.06451612903225806|0.125|2.0|0.088003669535328|0.1056274981999507|     7674|
+---+---+-------------------+-----+---+-----------------+------------------+---------+

they are now:

varemb_tfidf_blocklist_applied_item_precision_score_novelty_recurrent_novel_items
+---+-----+------+-----+---+-----+------+---------+
|min|   q1|median|   q3|max| mean|stddev|n_missing|
+---+-----+------+-----+---+-----+------+---------+
|0.0|0.009| 0.107|0.196|1.0|0.136| 0.152|    74546|
+---+-----+------+-----+---+-----+------+---------+

varemb_tfidf_blocklist_applied_item_f1_score_novelty_recurrent_novel_items
+---+---+------+-----+-----+-----+------+---------+
|min| q1|median|   q3|  max| mean|stddev|n_missing|
+---+---+------+-----+-----+-----+------+---------+
|0.0|0.0| 0.007|0.033|0.418|0.026| 0.045|    74546|
+---+---+------+-----+-----+-----+------+---------+

BAU_001_item_recall_score_novelty_recurrent_novel_items
+---+---+------+-----+---+-----+------+---------+
|min| q1|median|   q3|max| mean|stddev|n_missing|
+---+---+------+-----+---+-----+------+---------+
|0.0|0.0|   0.0|0.111|1.0|0.077| 0.141|    23138|
+---+---+------+-----+---+-----+------+---------+
```