import pika
import porcc as por

connection = pika.BlockingConnection(pika.ConnectionParameters(
host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='soccer/picture')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
	#print body
	#print "received."
	print ' [*] Waiting for messages. To exit press CTRL+C'
	por.proses_gambar(body)	
#	f=open("outputimage.jpg","wb")
#	f.write(body)
#	f.close()


channel.basic_consume(callback, queue='soccer/picture', no_ack=True)

channel.start_consuming()