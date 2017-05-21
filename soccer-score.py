#ini versi jalan uda diganti
import pygame
#import paho.mqtt.publish as publish
import datetime
import time
import porcc as por
import argparse

def text_to_screen(screen,text,x,y,size, warna):
	font_type = "font_score.ttf"

	font = pygame.font.Font(font_type, size)
	text = font.render(text, True, warna)
	screen.blit(text,(x,y))

# parse argument
# soccer-score.py --help 

parser = argparse.ArgumentParser()
parser.add_argument("-m","--menit", type=int,help="start awal menit untuk waktu berjalan")
parser.add_argument("-d","--detik", type=int,help="start awal detik untuk waktu berjalan")
parser.add_argument("-o","--home",help="nama tim home max 3 karakter, contoh [BHK], [CC]")
parser.add_argument("-a","--away",help="nama tim away max 3 karakter, contoh [BHK], [CC]")

args = parser.parse_args()

if args.detik==None:
	args.detik=0

if args.menit==None:
	args.menit=0


detik=int(args.detik)
menit=int(args.menit)
home=args.home
away=args.away


pygame.init()
width = 288
height = 120
canvas = pygame.display.set_mode((width, height))

logo = pygame.image.load("score_template.png")

x = 0
y = 20
merah = (255,000,000)
hitam = (000,000,000)
putih = (255,255,255)
ungu = (064,002,067)


home_score = 0
away_score = 0
#home_name = "KAN"
#away_name = "THE"
home_name = home
away_name = away
strip = "-"
#menit=0
#detik=0
t1=datetime.datetime.utcnow()

while 1:
	#pygame.time.delay(300)
	#canvas.fill(0)
	#canvas.blit(putih,(0,0))
	t2=datetime.datetime.utcnow()
	t3=t2-t1
	#t3.total_seconds()
	if t3.total_seconds()>1:
		#print "1 sec"
		detik=detik+1
		if detik>59:
			menit=menit+1
			detik=0
		#print menit,detik
		t1=datetime.datetime.utcnow()
		# kirim gambar
		pygame.image.save(canvas, "screenshot.png")
		por.kirim_gambar("screenshot.png","score.png")

	canvas.blit(logo,(x,y))
	if home_score > 9:
		text_to_screen(canvas, str(home_score),100, 32, 25, ungu)
	else:
		text_to_screen(canvas, str(home_score),110, 32, 25, ungu)

	#print waktu
	if menit > 9:
		text_to_screen(canvas, str(menit),100, 72, 25, ungu)
	else:
		text_to_screen(canvas, str(menit),110, 72, 25, ungu)
	#print waktu
	if detik > 19:
		text_to_screen(canvas, str(detik),150, 72, 25, ungu)
	else:
		text_to_screen(canvas, str(detik),155, 72, 25, ungu)

	#text_to_screen(canvas, str(detik),155, 72 ,25, ungu)
	text_to_screen(canvas, ":",138, 70, 25, ungu)


	#text_to_screen(canvas, str(home), 70, 100, 140, putih)
	text_to_screen(canvas, str(strip),138, 32, 25, ungu)


	text_to_screen(canvas, str(away_score),155, 32 ,25, ungu)
	#text_to_screen(canvas, str(away), 325, 100 ,140, putih)	

	text_to_screen(canvas, str(home_name),15, 32 ,25, putih)
	text_to_screen(canvas, str(away_name),210, 32 ,25, putih)
	#pyimageload untuk ngambil gambar
	#background = pygame.image.load(background)
	#canvas.blit(background,(0,0))
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				home_score = home_score + 1
			if event.key == pygame.K_2	:
				away_score = away_score + 1

			
		#publish.single("speak/kresna", str(text_mq) + " " + str(text_mq2), hostname="kresna.jaskapital.com")

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		