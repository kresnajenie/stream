
import porcc as por
import constant as c

#por.kirim("soccer/score", "Hello Kresna")

pesan = {}

home=raw_input("Berapa score home? ")
away=raw_input("Berapa score away? ")

pesan["sport"] = c.SOCCER
pesan["type"] = c.SOCCER_SCORE
pesan[c.SOCCER_HOME] = str(home)
pesan[c.SOCCER_AWAY] = str(away)

print pesan

por.update(pesan)


