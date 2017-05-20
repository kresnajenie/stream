
import porcc as por
import constant as c
import time

a = 0
hours = 0
while a < 1:
    for minutes in range(0, 90):
        for seconds in range(0, 60):
		time.sleep(1)
		print(hours,":", minutes,":", seconds)
		pesan={}
		pesan["sport"] = c.SOCCER
		pesan["type"] = c.SOCCER_TIME
		s=str(minutes) + ":" + str(seconds)
		pesan[c.SOCCER_TIME]=s

		por.update(pesan)
hours = hours + 1



