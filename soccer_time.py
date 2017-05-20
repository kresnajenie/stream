
import porcc as por
import constant as c
import time
import sys
import getopt

def cleanTime(number):

	number="0"+number
	result=number[-2:]



	return result


menit=0
detik=0
argv=sys.argv[1:]
try:
  opts, argv = getopt.getopt(argv,"hm:d:",["menit=","detik="])
except getopt.GetoptError:
  print 'soccer_time.py -m <menit> -d <detik>'
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
	print 'soccer_time.py -m <menit> -d <detik>'
	sys.exit()
  elif opt in ("-m", "--menit"):
     menit=arg
  elif opt in ("-d", "--detik"):
     detik=arg


print menit,detik

a = 0
hours = 0
while a < 1:
    for minutes in range(int(menit), 140):
        for seconds in range(int(detik), 60):
		time.sleep(1)
		print(hours,":", minutes,":", seconds)

		pesan={}
		pesan["sport"] = c.SOCCER
		pesan["type"] = c.SOCCER_TIME
		s=cleanTime(str(minutes)) + ":" + cleanTime(str(seconds))
		pesan[c.SOCCER_TIME]=s

		por.update(pesan)
hours = hours + 1



