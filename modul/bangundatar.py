import math

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi * sisi * sisi * sisi
    print (f'Luas Persegi {sisi} * {sisi} = {luas}')
    print (f'Keliling Persegi adalah {keliling}')
    
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar   
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang {panjang} * {lebar} = {luas}")
    print (f"keliling Persegi Panjang {keliling}")
    
def segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga {0.5} * {alas} * {tinggi} = {luas}")
    
def lingkaran(jarijari):
    luas = 3.14 * jarijari* jarijari
    print(f"Luas Lingkaran {3.14} * {jarijari} * {jarijari} = {luas}")
    
def jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas Jajar Genjang {alas} * {tinggi} = {luas}")