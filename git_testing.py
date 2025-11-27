from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Githubtest").getOrCreate()

data1 = [(1, "Alice", 30, "New York", "HR", 70000),
    (2, "Bob", 25, "Los Angeles", "IT", 80000),
    (3, "Charlie", 35, "Chicago", "Finance", 90000),
    (4, "David", 28, "Houston", "IT", 75000)]
    
data2 = [(1, "Alice", 30, "New York", "HR", 70000),
         (4, "David", 28, "Houston", "IT", 75000),
         (5, "Eve", 32, "Phoenix", "Marketing", 85000)]

schema = ["ID","Name","Age","City","Department","Salary"]

test_df1 = spark.createDataFrame (data1,schema)
test_df2 = spark.createDataFrame (data2,schema)