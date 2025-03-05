This page contains all the experiments run for key problem questions that may have been asked or explored.

## Experiments table
| Experiment name | Key Problem(s) | Key Question(s) | Outcome |
| --- | --- | --- | --- |
| [Applying the FMCG Fix](https://coda.io/d/_dK5h4iVEEUo/_suj6r) | There is an issue with FMCG (and some other) brands appearing excessively across the top winners.  | Can we apply the same fix Alex produced for interests to brand modelling without negatively impacting the performance of the model? | On hold while a bug in the FMCG fix is reviewed |
| [Multiple epochs](https://coda.io/d/_dK5h4iVEEUo/_suLLi) | We see relevant brands that are underrepresented in the output of the model. | Do we see model improvements when we train for multiple epochs? | In general, results stayed virtually the same |
| [More data (10M)](https://coda.io/d/_dK5h4iVEEUo/_su1V0) | We see relevant brands that are underrepresented in the output of the model. | Do we see model improvements when we train with more data? | It seems that adding more data does not improve the scores significantly. |
| [Cost Function](https://coda.io/d/_dK5h4iVEEUo/_suvez) | We see relevant brands that are underrepresented in the output of the model. | Can we adjust the cost function to get better representation of underrepresented brands? | BFCE (focal factor) seems to be the best model we have had so far. |
|  |  |  |  |