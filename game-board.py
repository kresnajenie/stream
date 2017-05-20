#ini versi jalan uda diganti
import pygame
#import paho.mqtt.publish as publish





def text_to_screen(screen,text,x,y,size, warna):
	font_type = "americah.ttf"

	font = pygame.font.Font(font_type, size)
	text = font.render(text, True, warna)
	screen.blit(text,(x,y))

pygame.init()
width = 288
height = 191
canvas = pygame.display.set_mode((width, height))

logo = pygame.image.load("score_template.png")

x = 0
y = 20
merah = (255,000,000)
hitam = (000,000,000)
putih = (255,255,255)

counter_bckgrnd=0
counter_sfx = 0
while 1:
	#pygame.time.delay(300)
	#canvas.fill(0)
	#canvas.blit(putih,(0,0))
	canvas.blit(logo,(x,y))
	#text_to_screen(canvas, str(text_mq), 78, 108, 140, hitam)
	#text_to_screen(canvas, str(text_mq), 70, 100, 140, putih)
	#text_to_screen(canvas, str(text_mq2), 328, 108 ,140, hitam)
	#text_to_screen(canvas, str(text_mq2), 320, 100 ,140, putih)	
	
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				background = pygame.image.load(filename[counter_bckgrnd])
				canvas.blit(background,(0,0))
				if counter_bckgrnd+1 < len(filename):
					counter_bckgrnd=counter_bckgrnd+1
			if event.key == pygame.K_m:
				counter_bckgrnd=counter_bckgrnd-1
				background = pygame.image.load(filename[counter_bckgrnd])
				canvas.blit(background,(0,0))
			if event.key == pygame.K_o:
				pygame.image.save(background,'test.jpg')

			if event.key == pygame.K_3:
				pygame.mixer.music.load(sfx[counter_sfx])
				pygame.mixer.music.play(-1)
				if counter_sfx+1 < len(sfx):
					counter_sfx=counter_sfx+1
			if event.key == pygame.K_9:
				counter_sfx=counter_sfx-1
				pygame.mixer.music.load(sfx[counter_sfx])
				pygame.mixer.music.play(-1)


			if event.key == pygame.K_s:
				pygame.mixer.music.stop()

			
		#publish.single("speak/kresna", str(text_mq) + " " + str(text_mq2), hostname="kresna.jaskapital.com")

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
