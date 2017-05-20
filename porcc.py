# -*- coding: utf-8 -*-
import json
import constant as c
import time
import pika
import base64


MQ_SERVER = "localhost"
MQ_QUEUE="cc/porcc"


def getTime():
	return time.strftime("%d/%m/%Y %H:%M:%S")

def kirim_gambar(input_filename, output_filename):
	f=open(input_filename,"rb")
	i=f.read()

	#encode gambar ke base64
	encoded_data = base64.b64encode(i)

	#print encoded_data

	pesan={}

	pesan[c.KEY_INPUTFILENAME] = input_filename
	pesan[c.KEY_OUTPUTFILENAME] = output_filename
	pesan[c.KEY_BASE64PICTURE] = encoded_data


	kirimGambar(pesan)



def kirimGambar(message):

	queue_name=c.QUEUE_SOCCER
	str_message=str(message)
	connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_SERVER))
	channel = connection.channel()
	channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=str_message)
	connection.close()

def kirim(message):

	title=message["sport"]
	subtitle=message["type"]
	queue_name=title+"/"+subtitle
	str_message=str(message)

	connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_SERVER))
	channel = connection.channel()
	channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=str_message)
	connection.close()

def update(pesan):
	kirim(pesan)

def write_to_file(filename,text):
	file = open(filename,"w")  
	file.write(text) 
	file.close() 

def proses_gambar(pesan):
	d_pesan = json.loads(pesan.replace("'", "\""))
	input_filename= d_pesan[c.KEY_INPUTFILENAME]
	output_filename= d_pesan[c.KEY_OUTPUTFILENAME]
	#print len(d_pesan[c.KEY_BASE64PICTURE])
	file_binary = base64.b64decode(d_pesan[c.KEY_BASE64PICTURE])
	f=open(output_filename,"wb")
	f.write(file_binary)
	f.close()
	print "File " + output_filename + " written."

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

		if dict_pesan["type"]==c.SOCCER_TIME:
			print getTime() + " UPDATE " + pesan
			file_home = dict_pesan["sport"] + "_" + dict_pesan["type"] + "_time.txt" 
			write_to_file(file_home,dict_pesan[c.SOCCER_TIME])
