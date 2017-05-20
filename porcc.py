# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json

MQTT_SERVER = "localhost"
MQTT_TOPIC="cc/porcc"

def kirim(topic,message):
	mqttc = mqtt.Client("porcc")
	mqttc.connect(MQTT_SERVER, 1883)
	mqttc.publish(topic, message)
	mqttc.loop(2) 

def update(pesan):

	kirim(MQTT_TOPIC,str(pesan))

def write_to_file(filename,text):
	file = open(filename,"w")  
	file.write(text) 
	file.close() 

def proses_pesan(pesan):

	print pesan
	# rubah ke dictionary
	dict_pesan = json.loads(pesan.replace("'", "\""))


	if dict_pesan["sport"] == "soccer":

		if dict_pesan["type"]=="score":
			print "Processing Soccer Score ..."
			file_home = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_home.txt" 
			file_away = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_away.txt" 
			write_to_file(file_home,dict_pesan["home"])
			write_to_file(file_away,dict_pesan["away"])

