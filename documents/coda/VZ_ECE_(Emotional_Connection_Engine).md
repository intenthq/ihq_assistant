[https://coda.io/d/_dK5h4iVEEUo/_su5SF](https://coda.io/d/_dK5h4iVEEUo/_su5SF)

[https://coda.io/d/_dK5h4iVEEUo/_suIF6](https://coda.io/d/_dK5h4iVEEUo/_suIF6)

[https://coda.io/d/_dK5h4iVEEUo/_suXCE](https://coda.io/d/_dK5h4iVEEUo/_suXCE)

# Executive summary

Emotional Connection was originally presented and proposed to VZ under the name of emotional connection score (ECS). ECS attempted to identify and score users for their behaviorally inferred priority of service versus actual quality of service; how much a given user’s value expectation is fulfilled by a subscribed service or product.

This concept has since been modularized into three pillars each of which may present as stand alone categories of insight and build upon each other to provide a score similar to the original formulation of ECS.

## 3 Pillars of ECE
| Brand-Consumer Values | Engagement Expectation | Brand-Value Alignment |
| --- | --- | --- |
| In our behavioral framework personal values are the guiding principles by which individuals measure desirable when making decisions and performing actions. These are relatively stable, though subjective, qualities of personality. Companies also exhibit brand values according to their mission, product and service mix, and community sentiment. |  |  |


**Brand-Consumer Value POC implementation**

- 78 personal values and attributes identified from market research, articles, literature related to the topic of emotional connection.
- Top 100 brands by line volume at Verizon were selected for testing.
- For each of the top 100 brands the following prompt was used to produce a score for each of the 78 personal values.

“For the 78 values and personal attributes along the columns score those that Airbnb most fulfills for people through products and services. Use Reddit, Wikipedia, Airbnb's website, and any other web sources that may be useful for this task. all 78 values and personal attributes must receive a relative score. 100 means this value and attribute is most satisfied by Airbnb and 0 means least. A negative value means Airbnb does the opposite of satisfy this value and attribute.”

- Brand Values are normalized within brand. Given how subjective Values and how subjectively a brand may be judged to satisfy a value a choice was made to weight values on a within brand relative basis.
- To derive Consumer Value scores, the weighted arithmetic mean per line_id value is computed to provide final inferred consumer value.
  - a consumer value of 100 is relatively most important. 0 is relatively least important value for a given user.
- 2 thresholds are applied:
  - Not all Brands were used in this POC. Therefore not all line_ids will have sufficient reference activity to merit a comprehensive ~~confident~~ Value. Only line_ids with cumulative Brand centiles >=50% contribution from top 100 brands used to Brand Values were used (about 5 million line_ids)
- All Brands receive a score for all Brand Values. To simplify insights exploration a threshold was applied to limit the number of line_id:value combinations. For each value the top 10% of lines with highest scores were assigned the Brand Value. This means only those lines that relatively care most about a Brand Value are associated with that Brand Value regardless of the absolute score associated with the value.

**Project Plan Timeline**



# Guidelines for the lead Data Scientist

1. Go to the [https://coda.io/d/_dK5h4iVEEUo/_suDbY](https://coda.io/d/_dK5h4iVEEUo/_suDbY) page to see more information on the framework we follow and to find general guidelines.
2. Start with the Shape stage here: **[https://coda.io/d/_dK5h4iVEEUo/_suGJ6](https://coda.io/d/_dK5h4iVEEUo/_suGJ6)**
   1. Check out the link at the top of the page if you need specific stage guidelines 
   2. Once all the mandatory actions are completed (and documented in the checklist table), set up a Gate Meeting with key stakeholders
3. Once all stakeholders have signed off on the **Shape Gate** checklist, proceed to the next stage: **[https://coda.io/d/_dK5h4iVEEUo/_suh1y](https://coda.io/d/_dK5h4iVEEUo/_suh1y)**
   1. Repeat the process as with the first stage. The only difference is that instead of a Gate, we have a Checkpoint - a less formal point of transition to the next stage.
4. Once you have completed all the Checkpoint actions in the **Data Driven Design** stage, proceed to: **[https://coda.io/d/_dK5h4iVEEUo/_su8_n](https://coda.io/d/_dK5h4iVEEUo/_su8_n)**