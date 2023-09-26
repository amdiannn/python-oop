class Hero:

    # class variablle
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # private instance variable <- tidak bisa diakses dan diubah
        self.__private = "private"

        # protected instance variable <- bisa diakses, tidak bisa diubah
        self._protected = "protected"

lina = Hero("Lina", 100)

print(f"{lina.__dict__}\n")
print(f"{Hero.__dict__}\n")
# print(f"{Hero.__privateJumlah}") <- tidak bisa diakses