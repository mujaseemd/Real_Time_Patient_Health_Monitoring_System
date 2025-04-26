import mysql.connector
import time
from datetime import datetime

# Step 1: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="sparkuser",
    password="Mujju@2004",
    database="healthcare"
)

cursor = connection.cursor(dictionary=True)

# Step 2: Process logic
def process_record(record):
    heart_rate = record['heart_rate']
    spo2_level = record['spo2_level']

    avg_heart_rate = heart_rate
    avg_spo2_level = spo2_level

    # Condition for alert based on heart rate or SPO2 level
    if  heart_rate > 80 or spo2_level < 90:  # SPO2 level threshold
        status = "alert"
    else:
        status = "normal"

    return {
        'patient_id': record['patient_id'],
        'avg_heart_rate': avg_heart_rate,
        'avg_spo2_level': avg_spo2_level,  # Use spo2_level in the result
        'status': status
    }

# Step 3: Insert processed data
def insert_processed_data(data):
    insert_query = """
        INSERT INTO processed_health_data_1 (patient_id, avg_heart_rate, avg_spo2_level, status)
        VALUES (%s, %s, %s, %s)
    """
    values = (
        data['patient_id'],
        data['avg_heart_rate'],
        data['avg_spo2_level'],  # Use spo2_level in the insert query
        data['status']
    )
    cursor.execute(insert_query, values)
    connection.commit()

# Step 4: Batch processing with metrics
def batch_processing(batch_size=100):
    start_time = time.time()
    start_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    fetch_query = f"SELECT * FROM patient_vitals LIMIT {batch_size}"
    cursor.execute(fetch_query)
    records = cursor.fetchall()

    if not records:
        print("No data found.")
        return

    print(f"[{start_timestamp}] Fetched {len(records)} records for batch processing...")

    alert_count = 0

    for record in records:
        processed = process_record(record)
        if processed['status'] == "alert":
            alert_count += 1
        insert_processed_data(processed)

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    end_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"[{end_timestamp}] Batch processing complete.")
    print(f"Records processed: {len(records)}")
    print(f"Alerts triggered: {alert_count}")
    print(f"Time taken: {duration} seconds")

# Step 5: Run
batch_processing(batch_size=100)

# Step 6: Close
cursor.close()
connection.close()
