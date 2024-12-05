from gempa import *

# Membuat Objek Gempa dengan Lokasi dan Skala
gempa1 = gempa("Banten", 1.2)
gempa2 = gempa("Palu", 6.1)
gempa3 = gempa("Cianjur", 5.6)
gempa4 = gempa("Jayapura", 3.3)
gempa5 = gempa("Garut", 4.0)

# Info Gempa
print("## Gempa Bumi Info ##")
print()
gempa1.dampak() # Memanggil method dampak
print("==========")
print("## Gempa Bumi Info ##")
print()
gempa2.dampak()
print("==========")
print("## Gempa Bumi Info ##")
print()
gempa3.dampak()
print("==========")
print("## Gempa Bumi Info ##")
print()
gempa4.dampak()
print("==========")
print("## Gempa Bumi Info ##")
print()
gempa5.dampak()