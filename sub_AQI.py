import paho.mqtt.client as mqtt
import time

broker_host = "localhost"
subscribe_topic = "adlink/datain"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(subscribe_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    msg.payload = msg.payload.decode("utf-8") # If msg.payload doesn't decode to "utf-8". The result will become b' msg.payload.
    print(time.strftime("%H:%M:%S"))
    print(msg.topic + " " + msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_host, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()