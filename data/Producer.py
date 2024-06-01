import json
import random
import time
from datetime import datetime
from confluent_kafka import Producer

def setup_producer():
    config = {
        'bootstrap.servers': 'localhost:9092'
    }
    return Producer(config)

def generate_adversarial_data(producer, topic):
    attack_types = ['DDoS', 'Phishing', 'Malware', 'SQL Injection', 'XSS']
    response_codes = [200, 403, 404, 500]
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'python-requests/2.25.1',
        'curl/7.64.1',
        'Mozilla/5.0 (compatible; Googlebot/2.1)'
    ]

    while True:
        cidr = f"{random.randint(10, 192)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0/24"
        attack_type = random.choice(attack_types)
        severity = random.choice(['Low', 'Medium', 'High'])
        payload_size = random.randint(40, 1500)  # In bytes
        response_code = random.choice(response_codes)
        user_agent = random.choice(user_agents)

        entry = {
            "source": f"APT{random.randint(1, 4)}",
            "attack_type": attack_type,
            "severity": severity,
            "timestamp": datetime.now().isoformat(),
            "payload_size": payload_size,
            "response_code": response_code,
            "user_agent": user_agent,
            "cidr": cidr
        }
        
        producer.produce(topic, json.dumps(entry).encode('utf-8'))
        producer.poll(0)  # Non-blocking
        time.sleep(random.uniform(0.1, 1.0))  # More frequent data generation

if __name__ == "__main__":
    producer = setup_producer()
    topic = 'adversarial_impacts'
    generate_adversarial_data(producer, topic)