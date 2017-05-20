# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import constant as c
import time

MQTT_SERVER = "localhost"
MQTT_TOPIC="cc/porcc"


def getTime():
	return time.strftime("%d/%m/%Y %H:%M:%S")

def kirim(topic,message):
	mqttc = mqtt.Client("porcc")
	mqttc.connect(MQTT_SERVER, 1883)
	mqttc.publish(topic, message)
	#mqttc.loop(2) 

def update(pesan):
	kirim(MQTT_TOPIC,str(pesan))

def write_to_file(filename,text):
	file = open(filename,"w")  
	file.write(text) 
	file.close() 

def proses_pesan(pesan):

	#print pesan
	# rubah ke dictionary
	dict_pesan = json.loads(pesan.replace("'", "\""))


	if dict_pesan["sport"] == c.SOCCER:

		if dict_pesan["type"]==c.SOCCER_SCORE:
			print getTime() + " UPDATE " + pesan
			file_home = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_home.txt" 
			file_away = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_away.txt" 
			write_to_file(file_home,dict_pesan[c.SOCCER_HOME])
			write_to_file(file_away,dict_pesan[c.SOCCER_AWAY])

		if dict_pesan["type"]==c.SOCCER_SUBS:
			print getTime() + " UPDATE " + pesan
			file_home = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_keluar.txt" 
			file_away = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_masuk.txt" 
			write_to_file(file_home,dict_pesan[c.SOCCER_KELUAR])
			write_to_file(file_away,dict_pesan[c.SOCCER_MASUK])
