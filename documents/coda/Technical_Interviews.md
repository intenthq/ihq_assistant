# ML Engineering

1. Run through the format of the technical Interview in the 1st Stage interview



Technical Interview

1. 5-10 mins: Basic questions to warm the candidates up (Ask 1-2 questions below)
   1. SPARK: When starting up spark (either interactive or submitted) there are a number of parameters and configuration options you can set. 
      1. Describe the basic starting options (local/yarn/other, cluster/client, memory, nodes....)
      2. Now you need to run on the production data set and it’s 50T. What sort of changes would you need to consider? (Configuration changes in spark submit command to optimize a job performance)
      3. Your spark job keeps dying. You find containers exiting with [-143|-100]. What’s going on? What can you check/change/try?
      4. How would to monitor the progress of the spark job (Yarn RM UI and Spark UI). 
      5. How would you check data skewing is not taken place when loading data in spark job
      6. Brief Architecture of spark job on YARN RM (complexity - medium)
      7. How to determine the total number of tasks to be completed for a stage in a job (complexity - beginner)
2. How to know the number of tasks being run in parallel (complexity - beginner)
3. What does shuffling operation in spark mean (complexity - medium)
4. How to optimize a spark job (joins and optimizing joins/aggregations) (complexity - advanced)



   1. SQL: Explain what this SQL command does?
      1. How would you change this query to only select the students who have an average higher than 8?
      2. How would you change this query to return all students even those who haven’t yet received a grade?
      3. How would you change this query to select the top 4 scoring students?

```
select [std.id](http://std.id),std.name,grd.total,grd.avg
from student std
join grades grd
on [std.id](http://std.id) = grd.id
```

           iv. then cover questions - joins like inner, outer, left, right and how they are different from Cartesian product, questions about group by (filtering a group by result set) and aggregate functions (rank(), max(), sum())

Questions on Airflow:

How many task can be executed in parallel with the Sequential Executor? Do you know the reason why?

Do you know what executor is used by MWAA?

Having this DAG definition:

```
with DAG(
        dag_id='sample_dag',
        schedule_interval=@daily,
        start_date=datetime(2023, 1, 1)
) as dag:
```

When will the DAG be executed for the first time?  ANSWER: `2023-01-01T23:59`

Can you modify it so it starts right at the beginning of 2021 and keeps running on a daily basis?

(For reference: [https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html))



Questions on S3

1. How do you test applications that interact with S3? Are you familiar with any Library for Mocking AWS services?



Questions on EMR

1. what is the difference between a step and a bootstrap action? Which would you use to:
   1. download a config file from s3 onto the driver before running a script
   2. copy an s3 file from one location to another before running a script



Questions on Python.

Having this class

```
class Pet:
    def __init__(self, name):
        self.name = name         
```

What method you need to implement in that class so this snippet prints “True”

```
pet = Pet('Fido')
other_pet = Pet('Fido')
print(pet==other_pet)
```

Answer: 

```
def __eq__(self, other):
```



How does python free memory?

What is PEP 8 and why is it important?



Questions on Spark/Pyspark

1. Brief Architecture of spark job on YARN RM (complexity - medium)
2. How to determine the total number of tasks to be completed for a stage in a job (complexity - beginner)
3. How to know the number of tasks being run in parallel (complexity - beginner)
4. What does shuffling operation in spark mean (complexity - medium)
5. How to optimize a spark job (joins and optimizing joins/aggregations) (complexity - advanced)



SQL questions from marvel data set ([https://www.kaggle.com/datasets/minisam/marvel-movie-dataset?select=marvel.csv](https://www.kaggle.com/datasets/minisam/marvel-movie-dataset?select=marvel.csv) and online sql editor - [https://sqliteonline.com/](https://sqliteonline.com/)):

1. What is the maximum revenue of each distributor in the North America region? (complexity - beginner/medium)
2. What is the specific movie with maximum revenue for the “universal pictures” distributor across the world? (complexity - beginner/medium)
3. Find the list of distributors who have at least 5 movies with review percentage from rotten tomatoes of 70% and above. (complexity - medium)
4. What are the movies with second highest world wide revenues in each year starting from 2015. (complexity - medium)

## Open end questions:



## System Design Exercise

The system design exercise will be based on a template that has the input and the output of the system as well as some examples on how the data will look like. We expect candidates to draw their solution where the red line is drawn in the template.





Template can be found in here, it can be imported to [https://excalidraw.com/](https://excalidraw.com/): 



System design exercise:



## Coding Exercise

String processing function

When introducing the coding challenge, we should remind the candidate that:

  - Don’t worry about creating an optimal solution, a simple/basic solution is perfectly good
  - We are not looking for a specific solution
  - Please talk through your code as you write it
  - You’ll have a chance to optimize the code at the end, once it is running



# Data Science