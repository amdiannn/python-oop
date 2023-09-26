class Mangga:

    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "Debug - Mangga: {}\nJumlah: {}".format(self.nama, self.jumlah)

    def __str__(self):
        return "Mangga: {}\nJumlah: {}".format(self.nama, self.jumlah)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("Arumanis", 10)
belanja2 = Mangga("Manalagi", 30)

print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)