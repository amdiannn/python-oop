class Hero:

    # enkapsulasi (menjadikan semua attribute object menjadi private)
    def __init__(self,name,health,attPower):
        self.__name = name
        self.__health = health
        self.__attPower = attPower

    # getter (cara agar bisa mengakses private object)
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def attacked(self, damage):
        self.__health -= damage

    def setAttPower(self, attPowerNow):
        self.__attPower = attPowerNow

# game start
earthshaker = Hero("Earth Shaker", 50, 5)

# game running
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.attacked(5)
print(earthshaker.getHealth())