# What is Core 4?

Developed by the creators of **DORA, SPACE, and DevEx**, Core 4 brings together years of research and real-world insights into a **unified developer productivity framework**. 

The framework is designed to help teams **move faster without burnout**, and Core 4 reflects everything learned from working with thousands of engineering teams. Companies like **Vercel, Intercom, and Dropbox** have already adopted it and seen significant results. 

## **Aimed at measuring and improving team velocity while avoiding burnout:**

**Product velocity is about both speed and direction.** When teams focus too much on "moving fast" without alignment on what to work on, they end up tackling competing priorities and pulling in different directions. In such cases, trying to move faster can actually **slow things down**. **Executing quickly** means ensuring all efforts are aligned in the same direction. It also means getting to market faster and, as a result, learning what our customers need more quickly.









## **How to measure product velocity?**

Core 4 is a set of metrics that unifies the principles behind DORA, SPACE, and DevEx (see below the image for info in each of those frameworks). 



## **The four dimensions of Core 4** are designed to hold each other in tension: 

- We don’t want to increase speed at the expense of developer experience, 
- Or spend more time on new features while quality takes a nosedive. 
- These metrics are designed to be used together as a system to provide a balanced look at overall team performance. 
- This is not a recommendation of singular metrics to track, but rather a basket of metrics that must be used together to be meaningful.



A few design choices are important to mention. First is the inclusion of PR throughput, measured by pull/merge requests per engineer, which can be controversial. It can be misused easily, for example looking at PR output on an individual level, or as a single measure. It’s important that this metric is used only as a system health metric, and always alongside other metrics in the framework.

The Impact dimension, with its key metric of percentage of time spent on new capabilities, is unique in that more does not always mean better. Too much reactive maintenance will stifle a company’s ability to innovate. But too little investment in proactive maintenance results in a poor-quality product with problems kicked down the road.

Another important design principle is that Core 4 balances qualitative and quantitative measurements. Quantitative measurements provide insight into what is happening, but qualitative insights tell us why. Ultimately, we need to understand the “why” of a team’s behaviour in order to change it, which is the whole point of measuring in the first place.

# Sources of data

[Mark Bunn](mailto:mark.bunn@intenthq.com) please add a table here with all the metrics and their source

# Development of Core 4

The **Core 4 framework** was co-authored by [Abi Noda](https://www.linkedin.com/in/abinoda/), a co-author of the DevEx framework, and me, in collaboration with [Nicole Forsgren](https://nicolefv.com/) (founder of DORA), [Margaret-Anne Storey](https://www.margaretstorey.com/) (co-author of the SPACE framework), [Michaela Greiler](https://www.michaelagreiler.com/) (co-author of the DevEx framework), and other researchers.

- **[DORA metrics](https://dora.dev/guides/dora-metrics-four-keys/)** are widely accepted “starter metrics” because of their popularity and focused scope. These metrics focus on software delivery capabilities (deployment frequency, lead time to change, change failure rate, and time to recover from a failed deployment), but they can often be misapplied.
- **[The SPACE framework of developer productivity](https://queue.acm.org/detail.cfm?id=3454124)** offers a robust definition of developer productivity covering five dimensions: satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. SPACE is very thorough, but it doesn’t come with a turnkey list of things to measure (by design).
- **[The DevEx framework](https://queue.acm.org/detail.cfm?id=3595878)** ties developer experience to three key dimensions: cognitive load, feedback loops, and flow. This framework is correlated with higher productivity but is somewhat disconnected from definitions of productivity used in other parts of the business.