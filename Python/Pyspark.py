# initiate pyspark notebook in vscode
import findspark
findspark.init()

from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.master("local[*]").appName("PySpark Notebook").getOrCreate()

# Check the Spark session
print(spark)

# initiate pyspark notebook in Jupyter notebook
# Create a Spark DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()


# print the dataframe
df.show()

# collect rows of df as a list of row elements
data = df.collect()

# select specific columns of a df
df.select("column_name").show()

# take the first few rows of a df
data = df.take(n)

