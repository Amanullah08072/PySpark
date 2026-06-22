# broadcast join on fact and dimention table
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Practice").getOrCreate()

# dimension_data = [(1,'Tech'),(2,'Fashion'),(3,'living'),(4,'Sports')]
dimension_data = [(i,f'Tech{(i)}') for i in range(1,1000001)]

dimension_df = spark.createDataFrame(dimension_data,['category_id','category'])
# dimension_df.show()

fact_data = [(i, (i%1000000) + 1) for i in range(1,10000001)]

fact_df = spark.createDataFrame(fact_data,['transaction_id','category_id'])
# fact_df.show()

result_df = fact_df.join(F.broadcast(dimension_df),on = 'category_id', how='inner')
result_df.show()
