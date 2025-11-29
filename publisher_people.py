import paho.mqtt.client as mqtt 
import time
import random

BROKER = "localhost"
TOPIC = "lab/people"

client = mqtt.Client()
client.connect(BROKER)

while True:
    people = random.randint(0, 10)
    message = f"People Counter: {people} - StudentID: 12113932"
    client.publish(TOPIC, message)
    print("Published:", message)
    time.sleep(2)