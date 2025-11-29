import paho.mqtt.client as mqtt 
import time
import random

BROKER = "localhost"
TOPIC = "lab/humidity"

client = mqtt.Client()
client.connect(BROKER)

while True:
    hum = random.randint(30, 70)
    message = f"Humidity: {hum} - StudentID: 12113932"
    client.publish(TOPIC, message)
    print("Published:", message)
    time.sleep(2)