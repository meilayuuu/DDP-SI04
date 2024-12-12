from animals import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan
        
    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna} dan hewan ini berjenis {self.jenis}')

print('======objek 1========')      
cupang = ikan('ikan cupang', 'pelet', 'air', 'bertelur', 'warna-warni', 'air tawar')
cupang.cetak_ikan()

print('======objek 2========')
hiu = ikan('ikan hiu', 'kerapu dan cumi-cumi', 'air', 'bertelur dan beranak', 'abu-abu', 'air asin dan air tawar')
hiu.cetak_ikan()