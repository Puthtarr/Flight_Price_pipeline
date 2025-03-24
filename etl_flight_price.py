from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from settings import load_config

# Load config
config = load_config()

minio_conf = config['minio']
spark_conf = config['spark']

# Spark Session
spark = SparkSession.builder \
    .appName(spark_conf['app_name']) \
    .master(spark_conf['master_url']) \
    .config("spark.hadoop.fs.s3a.endpoint", minio_conf['endpoint'].replace("http://", "")) \
    .config("spark.hadoop.fs.s3a.access.key", minio_conf['access_key']) \
    .config("spark.hadoop.fs.s3a.secret.key", minio_conf['secret_key']) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Mock Data
data = [("BKK", "HND", 13000), ("BKK", "SIN", 8000)]
columns = ["origin", "destination", "price"]

df = spark.createDataFrame(data, columns)
df = df.withColumn("load_date", current_timestamp())

# Write Delta to MinIO
df.write.format("delta").mode("overwrite").save("s3a://flight-price-datalake/flights")

print("✅ ETL Finished")
spark.stop()
