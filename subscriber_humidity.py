import paho.mqtt.client as mqtt 

BROKER = "localhost"
TOPIC = "lab/humidity"

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client()
client.connect(BROKER)
client.subscribe(TOPIC)
client.on_message = on_message

client.loop_forever()