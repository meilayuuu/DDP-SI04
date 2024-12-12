from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, cara_menyerang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.cara = cara_menyerang
        
    def cetak_ular(self):
        super().cetak()
        print(f'hewan ini {self.berbisa} dan hewan ini menyerang dengan  cara {self.cara}')
        
print('======objek 1========')      
sanca = ular('ular sanca atau sawah', 'tikus', 'sawah', 'bertelur', 'tidak berbisa', 'melilit mangsanya')
sanca.cetak_ular()

print('======objek 2========')      
kobra = ular('ular kobra atau sendok', 'katak', 'darat', 'bertelur', 'berbisa', 'mematuk mangsanya dengan giginya yang memiiki bisa')
kobra.cetak_ular()
