
import porcc as por

#por.kirim("soccer/score", "Hello Kresna")

pesan = {}

home=raw_input("Berapa score home? ")
away=raw_input("Berapa score away? ")

pesan["sport"] = "soccer"
pesan["type"] = "score"
pesan["home"] = str(home)
pesan["away"] = str(away)

print pesan

por.update(pesan)


