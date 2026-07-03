import paho.mqtt.client as mqtt
import time
import json
from fleet_simulator import create_fleet


BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_BASE = "lara/scooter/telemetry"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code", rc)

def on_disconnect(client, userdata, rc):
    print("Disconnected. Trying to reconnect")
    try:
        client.reconnect()
    except:
        time.sleep(2)

def start_mqtt_fleet_publisher(scooter_count=10, interval=1):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    fleet = create_fleet(scooter_count)

    while True:
        for scooter in fleet:
            payload = scooter.generate_payload()
            topic = f"{TOPIC_BASE}/{scooter.deviceId}"
            client.publish(topic, json.dumps(payload), qos=1)
            print(f"Sent to {topic}: {payload}")
        time.sleep(interval)

if __name__ == "__main__":
    start_mqtt_fleet_publisher(scooter_count=10, interval=1)