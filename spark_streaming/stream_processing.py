from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PatientMonitoringConsumer") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0," + "mysql:mysql-connector-java:8.0.26") \
    .getOrCreate()

# Define the schema for incoming data
schema = StructType([
    StructField("patient_id", IntegerType(), True),
    StructField("heart_rate", IntegerType(), True),
    StructField("body_temperature", DoubleType(), True),
    StructField("blood_pressure_systolic", IntegerType(), True),
    StructField("blood_pressure_diastolic", IntegerType(), True),
    StructField("spo2_level", IntegerType(), True),
    StructField("timestamp", StringType(), True)
])

# Read streaming data from Kafka topics 'health_data_source1', 'health_data_source2', 'health_data_source3'
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "health_data_source1,health_data_source2,health_data_source3") \
    .load()

# Convert the Kafka message value from binary to string
json_df = df.selectExpr("CAST(value AS STRING) AS json_value") \
    .select(from_json("json_value", schema).alias("data")) \
    .select("data.*")

# Process alerts: filter patients with abnormal heart rate or SPO2 level
alerts = json_df.filter((col("heart_rate") > 80) | (col("spo2_level") < 90))

# Define function to write the processed data to MySQL
def write_to_mysql(batch_df, batch_id):
    try:
        print(f"Writing batch {batch_id} to MySQL...")
        batch_df.show(truncate=False)
        batch_df.write \
            .format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/healthcare") \
            .option("dbtable", "patient_vitals") \
            .option("user", "sparkuser") \
            .option("password", "password") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .mode("append") \
            .save()
        print(f"Batch {batch_id} written successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to write batch {batch_id} to MySQL: {e}")

# Start the streaming query to process and store the alerts into MySQL
query = alerts.writeStream \
    .foreachBatch(write_to_mysql) \
    .outputMode("append") \
    .start()

# Await termination of the streaming query
query.awaitTermination()
