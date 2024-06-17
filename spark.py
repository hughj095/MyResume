import pyspark as ps
# OR
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

# create dataframe or notebook
data = [('Alice', 25), ('Bob', 30)]
columns = ['name', 'age']
df = spark.createDataFrame(data, columns)

# read CSV
df = spark.read.csv('file.csv', header=True, inferSchema=True)

# display first few rows
df.show()

# select columns
df.select('age')
df.select('name', 'age')

#filter df
df.filter(df['age'] > 25)

# add new column
from pyspark.sql.functions import col
df = df.withColumn('new_col', col('age') + 5)

# group by
df.groupBy('name').agg({'age': 'mean'})

# clean missing data
df.dropna()
df.fillna(0)

# merge dataframes
df1.join(df2, on='key')

# apply functions
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def add_one(x):
    return x + 1

add_one_udf = udf(add_one, IntegerType())
df = df.withColumn('age', add_one_udf(col('age')))



