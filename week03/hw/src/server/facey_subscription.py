import paho.mqtt.client as mqtt

MQTT_HOST="mqtt"
MQTT_PORT=1883
MQTT_TOPIC="facey"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)
	
def on_message(client,userdata, msg):
    #TODO: Put payload in S3
    print(f"New face from: {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)

client.loop_forever()
