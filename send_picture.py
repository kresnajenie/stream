import pika
import logging
import constant as c
import base64
import sys
import porcc as por


f=open("leister.jpg","rb")
i=f.read()

encoded_data = base64.b64encode(i)

#print encoded_data

pesan={}

pesan[c.KEY_INPUTFILENAME] = "leister.jpg"
pesan[c.KEY_OUTPUTFILENAME] = "leister_2.jpg"
pesan[c.KEY_BASE64PICTURE] = encoded_data


por.kirimGambar(pesan)
