# 🩺 Real-Time Patient Health Monitoring & Alert System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Apache Kafka](https://img.shields.io/badge/Kafka-3.5.1-black?logo=apache-kafka)
![Apache Spark](https://img.shields.io/badge/Spark-3.5.1-orange?logo=apachespark)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green)

> 📅 **Semester:** Jan–May 2025  
> 🎓 **Course:** UE22CS343BB3 – Database Technologies  
> 👨‍🏫 **Instructor:** Prof. Dr. NagaSundari  
> 👥 **Team 363_368:** Mujaseem D (PES1UG22CS363), N Swetha (PES1UG22CS368)

---

## 📌 Project Overview

A real-time health monitoring system that:

- Simulates patient vitals via a Flask API
- Streams data using **Apache Kafka**
- Processes data in real time using **Apache Spark Streaming**
- Stores alerts and results in **MySQL**
- Supports both **streaming** and **batch** modes for comprehensive health analytics

---

## 🧰 Tech Stack

| Component       | Technology Used                  |
|----------------|----------------------------------|
| Data Simulation| Flask (Python)                   |
| Stream Engine  | Apache Kafka 3.5.1               |
| Processing     | Apache Spark Structured Streaming|
| Storage        | MySQL 8.0                        |
| Language       | Python 3.x                       |
| Platform       | Ubuntu (WSL)                     |

---

## 🧑‍💻 Installation & Setup

# 1️⃣ Clone the Repository

1. Clone the Repository
git clone https://github.com/your-username/health-monitoring-system.git

cd health-monitoring-system


3. Set Up Python Virtual Environment
   
sudo apt install python3-venv  # Only once if not installed

python3 -m venv penv

source penv/bin/activate

pip install -r requirements.txt

5. Install Apache Kafka + Zookeeper
   
Download Kafka: kafka.apache.org/downloads

Extract it and run:

# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka
bin/kafka-server-start.sh config/server.properties

4️⃣ Create Kafka Topics

bin/kafka-topics.sh --create --topic health_data_source1 --bootstrap-server localhost:9092

bin/kafka-topics.sh --create --topic health_data_source2 --bootstrap-server localhost:9092

bin/kafka-topics.sh --create --topic health_data_source3 --bootstrap-server localhost:9092

🛢️ Database Setup (MySQL)

Start MySQL Server

Run the provided sql/setup.sql to create the DB & tables:

mysql -u root -p < sql/setup.sql

🚀 Running the Application

▶️ Start the Flask API Server

cd api

python api_server.py

▶️ Start Kafka Producer

cd kafka_producer

python multi_producer.py

▶️ Start Spark Streaming Job

cd spark_streaming

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 stream_processing.py

▶️ Run Batch Analysis (Optional)

cd batch_processing

python batch_processing.py


📚 References

Apache Kafka Docs
Apache Spark Docs
MySQL Docs



