class gempa:
    # Konstruktor Inisialisasi Atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    # Method Penentui Skala Gempa
    def dampak(self):
        # Logika/Statement
        if self.skala < 2 :
            print("Gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Gempa berdampak bangunan retak")
        elif 4 <= self.skala <= 6:
            print("Gempa berdampak bangunan roboh")
        elif self.skala > 6:
            print("Gempa besar berpotensi tsunami")
        
        # Menampilkan Lokasi dan Skala Gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')