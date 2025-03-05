A way forwards is required  

**OBSERVE**  
*The new approach reduces deployment effort from 4 weeks to 3 days (unproven). The new approach to VZ size data reduces the operational costs of this model from c£4k to under £1k.*  

*The new topic modelling approach is not proven to work effectively with lower-volume topics. The overall precision, recall, F1 score look similar to BAU. The challenge is the volume of topics we are dealing with.* 

*The probability of performance being higher live is unknown, the sampling method was problematic, and the fact that the model is less reliable for lower-volume topics is a concern.  Can we be confident that the model works until we can see the topics in the dashboard (UAT) and compare them to other profile characteristics (e.g. demographics)?*

**ORIENTATION**  
*Unknown performance is a high to gamble to take.*

*To mitigate the performance risk we could:*

-  *Run parallel testing, which could be carried out as part of MTN deployment at the cost of 2-4 weeks of additional work of DS, which will not impact delivery of MTN by more than 3 days. Unfortunately, using the current model does not create the model deployment efficiency. This approach does not accept the risk, removes it completely, and will require further funding to progress the topic model.* 
- *Deploy with MTN, expose MTN to higher volume topics and use the time saved in deployment to improve the topics model performance. This accepts risk but reduces its impact while funding improvements.* 
- *The expected improvement in performance is not massive; its optimisation is not a significant game changer. Can the deployment gain be achieved with the old model? Do we want to invest further on this? Do we have bigger r&d opportunities?*

*The benefits of the additional spend on top of the £100+k already invested would deliver faster deployment time of the model for future clients (4 weeks down to 3 days) and cheaper annual operating costs £40k down to £12k (based on VZ size data). Recouping the costs will require 1 year of deployment to 3 clients.*

*Faster deployment time aligns with our top priority product strategy initiative (minutes, not months) to support the scalability of our operations.  
  
It is felt the approach has greater value potential than current as it represents a state of the art approach which will continuously improve over time, delivering a long term competitive advantage.  
  
Discussion points in meeting on 10th Feb:*

- *We can test the pipeline with one days data.* 
- *1 DS needed per iteration of model with the new approach, new iteration takes 3 days.* 
- *O2 to vz model took 4 weeks on old model.*
- *The new model could still be improved and can create a competitive edge.* 
- *New model can provide MTN value.* 

**DECISION**  
*We will use the new modelling approach based on behavioural embeddings (byproduct of brands) for MTN.*

*Document BAU as a backup just in case.*

**ACTION**  
*Operationally test the end-to-end pipeline of a new approach with “sample” data.* [Sebastian Martins](mailto:sebastian.martins@intenthq.com) *.*

*Document BAU as a backup* [Andy Cole](mailto:andy.cole@intenthq.com) *.*

*Continue sizing R&D - in progress - Xingzhe.*

*Continue optimisation R&D - in progress - Seb & Maciej.*