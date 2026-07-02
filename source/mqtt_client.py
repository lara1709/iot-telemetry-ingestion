import paho.mqtt.client as mqtt
import time
import json
from utils.payload_generator import generate_payload


BROKER = "test.mosquitto.org"
TOPIC = "lara/scooter/test"

client = mqtt.Client()

client.connect(BROKER, 1883, 60)

while True:
    message = generate_payload()
    client.publish(TOPIC, json.dumps(message))
    print("Sent:", message)
    time.sleep(1)
