# Scores

We analysed the distribution of the scores to determine how to determine if a new distribution of scores is valid. To do that, we compared the newest distribution (March refresh) to previous runs of the model. We used the same model for all of those runs.

For instance, when comparing February and March, these are the two distributions we get:



 

We can visually see that they are quite similar and hence the new scores seem to follow the distribution that we expected.

### Running statistical tests

Initially, we wanted to use a statistical test to detect if those curves come from the same distributions. Firstly, we tested whether the distributions were normal using the Shapiro Wilko test. As shown below, the pvalue was < 0.05, which indicates that the distribution was not normal. So we could not use parametrics tests like the t-test.



So we had to use nonparametric tests which do not require a normal distribution. For instance, we tried the Kolmogorov-Smirnov test. As we can see below, the pvalue was < 0.05, so the two distributions are not the same.





### Finding a threshold

Even though the distributions are not the same, we wanted to wanted to be able to compute how different they were, and hopefully find a threshold to determine if their difference is significant enough for us to be worried.

We decided to use the Kolmogorov-Smirnov test, since it uses the cumulative distribution function to detect if the distributions are equal. We ran the test comparing the March scores with the scores from the previous three months. The distributions and the scores of that can be found below.









The resulting statistic from the test varied from 0.02 to 0.05, so we are assuming anything below 0.05 to be good. However, that might be too restrictive and the test could fail too easily. So we decided to compare the March distribution with other distributions to get a sense of what a good threshold could be.

First, we compared March with a small sample (500 points) from the same dataset, so that we would get a different curve that would still resemble the original one.



The statistic generate there was 0.03.

Then, we generated normal distributions and compared them with March. These are the statistics we got:

| Mean | SD | Sample size | Statistic |
| --- | --- | --- | --- |
| 0.5 | 0.2 | 1,000 | **0.297** |
| 0.35 | 0.1 | 1,000 | **0.2052** |
| 0.42 | 0.198 | 1,000 | **0.100** |
|  |  |  |  |


The first two rows represent distributions vastly different from the distributions we are getting with the model, and the statistic reflects that (0.297 >> 0.05). The third row represents a normal distribution (so already different from the model distributions which are not normal) with exactly the same mean and standard deviation from the March run. In that case, the statistic (0.1) is closer to the model distributions. That seems like a good candidate for the threshold.

We decided to use the **threshold of 0.1** when comparing new runs of the model. If a Kolmogorov-Smirnov test comparing a new run the the last run results in a threshold of less than 0.1, we can generally assume that the distribution is roughly correct.

# Brands per user

This is the distribution of the counts of brands per user for the March run:





We decided to check for differences in the overall mean of the curve and also for the extremes (users with too many or too few brands).

To decide on thresholds for the mean, we looked at the statistics of the previous run to have a baseline to compare, since we considered these runs to be of acceptable quality.



The mean varied from 46.9 to 41.2 (14%) and the standard deviation from 45.84 to 41.55 (10%). Accounting for some expected variation, we decided we don't want either the mean or the standard deviation to vary more than 25% from the previous run.





# Assessment metrics



To decide on the relative thresholds for the assessment metrics, we looked at the relative difference of the February and March run with relation to January.  



We can see that the f-1 scores dropped twice, once at 0.7% (user) and once at 3.6% (brand). As a ballpark figure, we decided that **any relative drop higher than 5%** would be too large and **should stop the process**.

However, it's possible that a score keeps dropping every month, which would not be captured by the relative test above. So we needed an absolute threshold as well. To determine that, we looked at the average scores of the last three runs (January, February, March). 





We determined that an absolute decrease of 2% should issue a warning, and an absolute decrease of 5% should stop the process. Those values (2% and 5%) were based on common sense of what values we would be worried about in a manual inspection.



# Mapper

This is the mapper size when a new mapper is created for a refresh. This was created using the *predict_brand_pipeline_varemb.py* script, so it includes all filters including things like blocked brands.

## Mapper Counts
| Refresh | Count | Increase |
| --- | --- | --- |
| 2023-01-25 | 484,220 |  |
| 2023-02-25 | 492,256 | 1.66% |
| 2023-03-25 | 497,878 | 1.14% |
| 2023-04-25 | 509,860 | 2.41% |
| 2023-05-25 | 514,910 | 0.99% |
| 2023-06-25 | 520,297 | 1.05% |
| 2023-07-25 | 525,338 | 0.97% |
| 2023-08-25 | 529,983 | 0.88% |
| 2023-09-25 | 549,425 | 3.67% |
| 2023-10-25 | 555,008 | 1.02% |
| 2023-11-25 | 561,080 | 1.09% |
| 2023-12-25 | 565,521 | 0.79% |
| 2024-01-25 | 565,521 | 0.00% |
| 2024-02-25 | 569,614 | 0.72% |
| 2024-03-25 | 570,919 | 0.23% |
| 2024-04-25 | 573,721 | 0.49% |


The counts increase 1.14% per month on average.