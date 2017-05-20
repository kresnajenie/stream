# -*- coding: utf-8 -*-
import sys
import getopt
import pika
import porcc as por
MQTT_SERVER = "localhost"
MQTT_TOPIC="#" # "cc/porcc"


def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)	
	por.proses_pesan(body)
	#print "Topic: ", msg.topic+"Message: "+str(msg.payload)
	#print "hello"

queue_name = ''
argv=sys.argv[1:]
try:
  opts, argv = getopt.getopt(argv,"hq:",["queue="])
except getopt.GetoptError:
  print 'server_porcc.py -q <queue_name>'
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print 'server_porcc.py -q <queue_name>'
     sys.exit()
  elif opt in ("-q", "--queue"):
     queue_name = arg

if queue_name=="":
     print 'server_porcc.py -q <queue_name>'
     sys.exit(2)

print 'Listening to Queue: ', queue_name

connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQTT_SERVER))
channel = connection.channel()

channel.queue_declare(queue=queue_name, durable=True)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print(' [*] Waiting for messages in queue ' + queue_name + '. To exit press CTRL+C')
channel.start_consuming()