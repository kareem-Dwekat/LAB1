import paho.mqtt.client as mqtt 
import time
import random

BROKER = "localhost"
TOPIC = "lab/temp"

client = mqtt.Client()
client.connect(BROKER)

while True:
    temp = random.randint(20, 35)
    message = f"Temp: {temp} - StudentID: 12113932`"
    client.publish(TOPIC, message)
    print("Published:", message)
    time.sleep(2)