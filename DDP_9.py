#Soal1
print("\n---celcius ke fahrenheit---")
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 +32)
celcius_ke_fahrenheit(0)

#Soal2
print("\n---mencari bilangan genap---")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(9)

#Soal3
print("\n---melihat keterangan lulus dan tidak lulus---")
#rata rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 70:
        print("lulus")
    else:
        print("gagal")
skor (40)
skor (80)

#Soal4
print("\n---mencetak bilangan ganjil---")
def bil_ganjil(ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end=' ')
bil_ganjil(20)