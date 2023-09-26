class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini hanya berlaku untuk class
    def getJumlah2():
        return Hero.__jumlah
    
    # memakai staticmethod dan classmethod agar berlaku untuk keduanya
    # staticmethod tidak memakai argument
    @staticmethod
    def getJumlah3():
        return Hero.__jumlah

    # classmethod memakai argument
    @classmethod
    def getJumlah4(hero):
        return hero.__jumlah

ucup = Hero("Ucup")
# print(Hero.getJumlah()) <- tidak bisa berjalan
print(ucup.getJumlah())

sniper = Hero("Sniper")
print(Hero.getJumlah2())
# print(sniper.getJumlah2()) <- tidak bisa berjalan

rikimaru = Hero("Rikimaru")
print(Hero.getJumlah3())
print(rikimaru.getJumlah3())

drowranger = Hero("Drow Ranger")
print(Hero.getJumlah4())
print(drowranger.getJumlah4())