-- setup.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS healthcare;
USE healthcare;

-- Table for real-time vitals collected via Spark Streaming
CREATE TABLE IF NOT EXISTS patient_vitals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id VARCHAR(20),
    heart_rate INT,
    body_temperature FLOAT,
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    spo2_level FLOAT,
    timestamp DATETIME
);

-- Table for batch-processed results
CREATE TABLE IF NOT EXISTS processed_health_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id VARCHAR(20),
    heart_rate INT,
    spo2_level FLOAT,
    status VARCHAR(10), -- 'alert' or 'normal'
    timestamp DATETIME
);
