import math

def kubus(sisi):
    volume = sisi * sisi * sisi
    luas_permukaan = 6 * sisi * sisi
    print(f'Volume Kubus {sisi} * {sisi} * {sisi} = {volume}')
    print(f'Luas Permukaan Kubus {6} * {sisi} * {sisi} = {luas_permukaan}')
    
def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
    print(f'Volume Balok {panjang} * {lebar} * {tinggi} = {volume}')
    print(f'Luas Permukaan Balok ({2}*{panjang}*{lebar}) + ({2}*{panjang}*{tinggi} + ({2}*{lebar}*{tinggi}) = {luas_permukaan}')
    
def tabung(jarijari, tinggi):
    volume = 3.14 * jarijari * jarijari * tinggi
    luas_permukaan = 2 * 3.14 * jarijari * (jarijari + tinggi)
    print(f'Volume Tabung {3.14} * {jarijari} * {jarijari} * {tinggi} = {volume}')
    print(f'Luas Permukaan Tabung {2} * {3.14} * {jarijari} * ({jarijari+tinggi}) = {luas_permukaan}')
    
def prisma(luasalas, tinggi, kelilingalas):
    volume = luasalas * tinggi
    luas_permukaan = (2 * luasalas) + (kelilingalas * tinggi)
    print(f'Volume Prisma {luasalas} * {tinggi} = {volume}')
    print(f'Luas Permukaan Prisma ({2} * {luasalas}) + ({kelilingalas} * {tinggi}) = {luas_permukaan}')
    
def bola(jarijari):
    volume = 4/3 * 3.14 * jarijari * jarijari * jarijari
    luas_permukaan = 4 * 3.14 * jarijari * jarijari
    print(f'Volume Bola {4/3} * {3.14} * {jarijari} * {jarijari} * {jarijari} = {volume}')
    print(f'Luas Permukaan Bola {4} * {3.14} * {jarijari} * {jarijari} = {luas_permukaan}')
    