# -*- coding: utf-8 -*-
import porcc as por
MQ_SERVER = "localhost"
MQ_QUEUE="#" # "cc/porcc"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	por.proses_pesan(msg.payload)
	#print "Topic: ", msg.topic+"Message: "+str(msg.payload)
	#print "hello"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQ_SERVER, 1883, 60)
client.subscribMQ_QUEUEIC)

client.loop_forever()