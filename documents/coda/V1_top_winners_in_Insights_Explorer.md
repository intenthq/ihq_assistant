**Alignment meeting held on Jan 4th with** [Andy Cole](mailto:andy.cole@intenthq.com) [Kumutha Swampillai](mailto:kumutha.swampillai@intenthq.com) **&** [Sebastian Martins](mailto:sebastian.martins@intenthq.com) **agreeing on the following:**

- We are **optimising VAE to provide unbiased synthetic data to maximally preserve the signal in the data while ensuring we have high confidence that we are not replicating user brand engagement profiles.**
- We will review the current iteration of the model on three tasks:
  - precision and recall of brand engagement predictions in the next 30 days
  - ability of the model to generate the input data (error of the model)
  - the likelihood of a predicted user brand profile replicating an existing user's brand profile.
- **§We will apply business rules to the outputs in order to meet user expectations where the model doesn't directly do that;** e.g. expected semantic co-occurrence between brands in the IE top winner view. These rules have been documented from CS assessment [https://coda.io/d/_dK5h4iVEEUo/V1-top-winners-in-Insights-Explorer_sutwf](https://coda.io/d/_dK5h4iVEEUo/V1-top-winners-in-Insights-Explorer_sutwf).
- The above will be used to approve modelled brands, ideally for a Feb delivery of the Jan refresh;
  - The refresh mechanism will use the inference engine going forward along with a monitoring process that allows us to understand the quality of our predictions in campaigns and evolve the model past this initial version.

## **Business rules:**

- Everyone seems to **use one or a combination of other behavioural insights to assess modelled Brands against**, such as Interests, Natural and Smart Audiences, Life Stage (Axiom), but also a Verizon model (Cust. DNA).
- Ideally we should **aim for a few Brands of the same category as the applied filter to show up in the top 24 results** in the dashboard to increase user confidence in the data and potentially support in marketing use cases. 
  - One interesting use-case is that some users try to find related Brands for a particular topic in the other top winning Brands displayed by IE; e.g. if they’re looking for food delivery Brands and filter for DoorDash, they expect to ‘discover’ other food delivery Brands in there, but they switch between size and top winners view, so this doesn’t always have to be true in top winners.
- **A large number of indirectly correlated but possible brands is, however, frequent and accepted**, especially for Brands that are popular across a wide range of demographics that are likely to have very different behaviours otherwise. (e.g. Netflix). 
- **Users expect to see a representative volume across a wide range of Brands, both commonly used a.k.a. popular (e.g. Facebook) and more specialised (e.g. Strava)**. We are currently missing or under-representing quite a few relevant & specialised brands from the output and it has been observed that the volumes drop quickly after the first 20 or so Brands by size.
- **Many brands of the same category, while unrelated to the filter raise alarm bells.** Users are ok with brands that are unrelated to the filter topic because they accept the possible correlating behaviour (e.g. young people like Oreo). However, having a large number of Brands from the same topic up in the top 24 winners for a totally unrelated filter is not accepted (e.g. VitaminWater, Quaker, Doritos, Red Bull, Coors, Pampers all come up on the first page when filtering for Disney+).
- **Similarly, Brands that frequently come up in top winning Brands for many different filters are also red flags (e.g. Bitmoji).**
- Profiles that look good today (more detail [here](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_lufu5)): Gaming, food delivery, discount shopping, 25-34 year olds with high affluence, working professionals.
- Profiles that don’t look good today (more detail [here](https://coda.io/d/_dK5h4iVEEUo/_sutwf#_luSLa)): 18-24 year olds, Tiktok, Disney+, Fitness, Spanish Language, Telco competitor representation, low affluence.
  - Observing higher volumes on some FMCG brands than actual visits (seen in descriptive Brands) such as Minute Maid and Glaceau SmartWater.

**Long-term success criteria (to optimise for post-V1):**

- **Correlation between same topic Brands**: users expect 2-5 brands from the same category as their filter to come up in the top 24 winners displayed in IE.
- **We do not, however, expect all top winning Brands to be of the same category** - there should be diversity to form comprehensive customer personas.
- **Correlation between most Brands of different topics shouldn’t be high**: users are concerned if they see many Brands of the same category come up for an unrelated filter, most observed is FMCG.
- **Expected representation of predictions for both common/popular and more specialised ones**; we should have a similar distribution of sizes to the input data, especially for the curated list of Brands where we trust that the input data is indicative of real interest in the Brand.
  - Low volumes expected for Brands where it’s unlikely people actually visit the websites (e.g. Minute Maid or Smart Water). This is expected even if the input data may indicate high volumes, but definitely not expecting higher volumes for predictions than seen in the data.
- **We shouldn’t fully represent the websites people have visited**; ie: there should be significant difference between the input and output data.

**Note:** While the identified flaws are solvable through output processing in order to deliver Brand predictions satisfactorily in the short-term, the underlying input data flaws are important to address for the long-term health of our behavioural representations. 

- We have already removed some of these Brands from the output (e.g. mParticle is not in the Verizon allow list), but the models are still trained on data which we believe to be contaminated with fake visits and this is likely to influence the user-user similarity learned by our embeddings.

## Brand predictions - observations from a sample of 1M users below

Assessing other top winning Brands when adding different filters in Insights Explorer:

  - ones that have been used most by users in the past 12 months;
  - ones known to be useful for certain use-cases (e.g. lookalikes);
  - other ones that could be of interest for our CS team to support customers;

**‘Looks good’**

- LinkedIn, Lyft, Walmart, ESPN and Netflix are pretty good examples where the top 24 winning Brands displayed in IE are representative and/or credible for the profile of customers for which these Brands are predicted.
- Gaming looks good - Courtney uses Interests and Natural Audiences as filters and then checks the top winning modelled Brands (see her recording from 10:51)
  - There are some specific Games that are expected and not showing though such as Minecraft and Pokemon.

> *Yeah, I don't hate this at all, so this looks pretty good to me.*

- Food delivery (filtering for modelled Brand - DoorDash, Courtney recording min. 15:26)
  - Happy with top winning behaviours in Interests and Nat. Audiences
  - Not seeing many other food delivery Brands in top winners, but not particularly bothered by it after seeing the correlation with other behavioural attributes.
- Walmart - very good example:
  - Seeing Sam’s Club rank 2nd in top winning Brands (higher than Affinities) is very positive.
  - Happy with Pampers ranking 3rd here (”*pampers is something that you would buy in bulk often at one of these places, so that's not a red flag to me.”)* though it is an FMCG brand.
  - Glad to see Target too on the top 24 winning Brands as opposed to Affinities. Also Home Depo, Petco and Lowe’s (other related discount stores), though she would’ve expected to also find Costco which doesn’t come up.
  - Also glad to see Price Conscious Shopping, Department Stores and Bargain Hunter as well as other related Interests.
- 25-34 & high affluence (see Aggie recording from 3:10)
  - Happy with top winning brands related to travelling, finance and social media.
- Apple Music Enthusiast (Cust DNA filter) - see Aggie’s recording from 12:40
  - top winning Brands are very relevant, many other Apple related products though the filter brings up a very small number of users (1.5K)
- Professionals (Nat. Audience) - see Aggie’s recording from 15:45
  - Seeing work software Brands which is expected - quite similar to descriptive Brands too.

> So the companies that come up here are exactly what I would expect.

- Ideally we should aim for a few topic-related Brands to show up in the top 24 to increase user confidence in the data and potentially support in marketing use cases. 
  - One interesting use-case observed in Courtney’s assessment (recording in the appendix) is when users try to find related Brands for a particular topic in the other top winning Brands displayed by IE; see streaming example in Courtney’s recording from min. 20:50)
  - A large number of indirectly correlated but possible brands is, however, frequent and accepted, especially for Brands that are popular across a wide range of demographics that are likely to have very different behaviours otherwise. (e.g. Netflix). 

**‘Doesn’t look good’**

- Missing or too little predictions for some Brands that are frequently used such as T-Mobile, Mint mobile (competitors), Rakuten, Google Nest, Arlo technologies, HBO (seeds), Strava, Garmin, Paramount - this might be solved once we upload predictions for the full population rather than the 1M sample.
- More predictions of commonly used services (such as Facebook) than actual visits - we would expect these not to be super relevant for a user’s profile, but the predictions seem to be weighting these brands more than others.

> *Some worry that the volume of the modelled interests are becoming more polarised - very few high volume brands are higher, and the long tail gets longer with lower volumes. -* Ben Marnan

- The team often starts by assessing the younger demographic which has been known to display large amounts of FMCG brands in the top 24 winners and is also a under-represented demographic for Verizon that they are likely to want to analyse in order to target for retention or understand their interests for acquisition efforts.
  - Filtering for 18-24(see Courtney’s recording from min. 2:57) surfaces a lot of FMCG brands in the top winning 24 Brands.

> *We still have this interesting situation, where, we have parent companies of brands showing up as we're interested in them when in reality, is someone that interested in coca cola? I don't know, and then I think other ones get under represented in the same way.*

  - However, some FMCG Brands are expected.

> *I do like seeing Oreo. I think that one might actually be kind of legitimate.*

  - She also expects to find Gaming brands in the top which are not present, but that doesn’t seem to be a major red flag.
  - Tiktok is expected to surface much higher than it is, definitely above Apple for this demographic, but it’s in the top 24 alongside other Brands like Pinterest and Snapchat which makes it ok-ish despite the lower rank.
- Fitness Enthusiast (Cust DNA VZ model) or Health, Fitness & Travel (Nat. Audience) - see Aggie recording from 5:07
  - Not much fitness coming up in top 24 winners, though they are aligned with Interests, but not the filter.
  - Travel is well represented, but nothing regarding sports - some do come up in descriptive Brands such as Garmin and Strava.
  - Though this may be a cause of the models used in filters, even filtering for Fitbit, the other top winning modelled Brands are not representative of Sports or Fitness. Some relevant Brands are in fact missing from our prediction (Strava & Garmin).

> *But the brands modelled haven't really changed in the way that we would expect them to.*

- Spanish Language - see Ben’s analysis [here](https://docs.google.com/spreadsheets/d/1gODP_XpRrWuXUVA8KksQMT3cZY7Hc-qM1scnGF6gvxQ/edit#gid=1051092493)

> *Using 'Spanish Language' - we need to see at least some of the top indexing sites to be Spanish Language sites. This was the case with Brand Affinities, but has been lost in Brands Modeled QA*

- Low affluence - see Ben’s  analysis [here](https://docs.google.com/spreadsheets/d/1gODP_XpRrWuXUVA8KksQMT3cZY7Hc-qM1scnGF6gvxQ/edit#gid=1051092493)

> *High affluence looks good. However, low affluence results are good for Brand Affinities, but not as good for Brands Modelled QA - because there is a relationship with younger customers, FMCG and other frequently occurring questionable results reappear.*

- Minute Maid - very high volume which is unlikely

> *Brands Modeled Qa finds 39.3k. The model allocates it more than the likes of Expedia, IMdB and The New York Times.*

  - Similar with Glaceau SmartWater - see Ben’s analysis [here](https://docs.google.com/spreadsheets/d/1gODP_XpRrWuXUVA8KksQMT3cZY7Hc-qM1scnGF6gvxQ/edit#gid=1051092493)
- Many brands of the same category, while unrelated to the filter raise alarm bells.
  - When you filter for Disney+, there are 10 Brands coming up in the top 24 winners - all consumer goods typically found in supermarkets such as food, drink or personal care. 
    - This is almost half the top Brands that are assessed by our model to be ‘behaviourally similar’ to the original filter. So the insight from a user perspective would be that the most popular things amongst Disney+ customers are supermarket brands, so they might decide to partner with the a supermarket brand - would that be the right choice?
  - Tiktok’s top winners also have 10 FMCG brands in the top 24, some the same as Disney (Vitamin Water and Glaceau Smart Water, others different but of the same category.
- Similarly, Brands that frequently come up in top winning Brands for many different filters are red flags.
  - Besides FMCG, we have observed other Brands behave that way such as Invisalign or Bitmoji.

**‘THE FMCG PROBLEM’** 

We are seeing many common supermarket Brands over-indexing, especially for the young demographic and we believe this is unlikely to be true and more importantly, it is damaging the user’s perception of the data and could impact their trust in the product.

- Suspect that this data is contaminated and doesn’t actually reflect the true number of visits to such websites. This is because we don’t think it’s likely that many people visit or buy from their websites (e.g. Coca-Cola).
- While there are studies to show FMCG is using Tiktok to grow their brand awareness and popularity (see article on the subject [here](https://econsultancy.com/fmcg-brand-strategy-tiktok/)), the large number of correlated FMCG Brands coming up together pretty frequently for uncorrelated filters is still bizarre, especially since some of these Brands are owned by the same parent company.
- It is believed that there are other factors such as ad-tech, redirects or sdk signals making it look like users visited all those websites when in fact they haven’t actually visited all of them. 
- Though this is largely observed for FMCG, there are other Brands such as mParticle that are likely to be affected by the same issue. 
  - It appears as mParticle is visited by 30M Verizon customers in a month, which we believe to be unlikely as mParticle is a b2b customer data platform (CDP) company specialised in Marketing AI - in fact a competitor to IHQ. 
- While the observations above are solvable in order to deliver Brand predictions satisfactorily in the short-term, the underlying input data flaws are important to address for the long-term health of our behavioural representations. 
  - We have already removed some of these Brands from the output (e.g. mParticle is not in the Verizon allow list), but the models are still trained on this data which is likely to influence the user-user similarity learned by our embeddings.
- This is essentially our first use-case to validate behavioural representations against, but the embeddings that underpin these predictions will form the building block of Intent’s large behavioural model. Hence, understanding and correcting for input data flaws will be an important factor to the real-life value of these embeddings to discern signal from noise and be able to identify patters of behaviour that should be leveraged for marketing efforts.
  - We could explore normalising the data against some external data source that provides a better representation of the volume of visits to these websites, but we don’t have a clear view of how to correct for this at the moment.

**Appendix**

Recordings:

- [Ben](https://intenthq.zoom.us/rec/share/CNAJ4tifXqA1PulfruMU4bRQ0HGRPnPuLVU7b5cb00rz0Vj3gMMVmmXCVzmVkQ.Rvd-8s2NgXquhMXZ?startTime=1702307620000) + follow-up observations in spreadsheet [here](https://docs.google.com/spreadsheets/d/1gODP_XpRrWuXUVA8KksQMT3cZY7Hc-qM1scnGF6gvxQ/edit#gid=1051092493)
- [Courtney](https://intenthq.zoom.us/rec/share/EMjH-ObzwTyXbhn1E4rLFlmYaXWFixSZpKERA5YbP7Eyf27I5wQpVeXCyR5xMx1B.7GEvq2LEQpu8F8Yw?startTime=1702314472000)
- [Aggie](https://intenthq.zoom.us/rec/share/B823dv4VdDTuuryQFVta95UnO7WTYW2RXLPWbSytBlcxdFsPc9nFSYgLwVzkWIQ.0xLlfUPG3A5l_6Cj?startTime=1702548379000)
- Useful to see an overview of how the VZ QA dashboard in databricks is used [here](https://intent.slack.com/archives/C011854N4LT/p1702671622323819).
  - As indicated by Rachel - other assessments will be undertaken via the QA dashboard in DataBricks to identify trends or anomalies over time. MoM changes will continue to be a key indicator for this and they should either be explainable or investigated as points of improvement;

IE screenshots on a selection of Brands 👇

https://miro.com/app/live-embed/uXjVMrQgRm0=/?boardAccessToken=r8XDpSbCgRnbcl00C35BpBAYuaFbAUWy&autoplay=true&embedMode=view_only_without_ui