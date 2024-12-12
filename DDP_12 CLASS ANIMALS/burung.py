from animals import *

class burung (animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi
    
    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')
 
print('======objek 1========')       
Beo = burung ('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue dan orange', 'kamu jelek')
Beo.cetak_burung()

print('======objek 2========')
Elang = burung ('burung elang', 'daging', 'udara', 'bertelur', 'coklat dan putih', 'siulan yang bernada tinggi dan melengking')
Elang.cetak_burung()
