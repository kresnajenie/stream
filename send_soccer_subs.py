
import porcc as por
import constant as c
#por.kirim("soccer/score", "Hello Kresna")

pesan = {}

keluar=raw_input("Nama yg keluar? ")
masuk=raw_input("Nama yg masuk baru? ")

pesan["sport"] = c.SOCCER
pesan["type"] = c.SOCCER_SUBS
pesan[c.SOCCER_KELUAR] = str(keluar)
pesan[c.SOCCER_MASUK] = str(masuk)

print pesan

por.update(pesan)


