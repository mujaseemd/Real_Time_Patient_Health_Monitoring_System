import requests
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Map of API URLs to their respective Kafka topics
API_TOPIC_MAP = {
    "http://localhost:5000/source1": "health_data_source1",
    "http://localhost:5000/source2": "health_data_source2",
    "http://localhost:5000/source3": "health_data_source3"
}

while True:
    for url, topic in API_TOPIC_MAP.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print(f"Sending from {data['source']} to topic {topic}: {data}")
                producer.send(topic, data)
            else:
                print(f"API error from {url}: {response.status_code}")
        except Exception as e:
            print(f"Error fetching from {url}: {e}")
        time.sleep(1)




