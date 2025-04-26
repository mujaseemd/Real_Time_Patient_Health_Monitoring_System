  GNU nano 7.2                                                                         api_ser.py                                                                                   from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

def generate_vitals(source, pid_range):
    return {
        "source": source,
        "patient_id": random.randint(*pid_range),
        "heart_rate": random.randint(60, 100),
        "body_temperature": round(random.uniform(36.0, 38.5), 1),
        "blood_pressure_systolic": random.randint(100, 140),
        "blood_pressure_diastolic": random.randint(60, 90),
        "spo2_level": random.randint(90, 100),
        "timestamp": datetime.now().isoformat()
    }

@app.route('/source1', methods=['GET'])
def source1():
    return jsonify(generate_vitals("Device_A", (1001, 1003)))

@app.route('/source2', methods=['GET'])
def source2():
    return jsonify(generate_vitals("Device_B", (2001, 2003)))

@app.route('/source3', methods=['GET'])
def source3():
    return jsonify(generate_vitals("Device_C", (3001, 3003)))

if __name__ == '__main__':
    app.run(port=5000)