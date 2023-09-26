class Hero:

    def __init__(self, name):
        self.healthPool = [0, 100, 200, 300, 400, 500]
        self.attPowerPool = [0, 10, 20, 30, 40, 50]
        self.armorPool = [0, 1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def showInfo(self):
        print("{}\n\tLevel: {}\n\tHealth: {}\n\tattPower: {}\n\tArmor: {}".format(
                self.__name,
                self.__level,
                self.__health,
                self.__attPower,
                self.__armor
            )
        )

    @property
    def healthPool(self):
        pass

    @property
    def attPowerPool(self):
        pass

    @property
    def armorPool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @healthPool.setter
    def healthPool(self, input):
        self.__healthPool = input

    @attPowerPool.setter
    def attPowerPool(self, input):
        self.__attPowerPool = input

    @armorPool.setter
    def armorPool(self, input):
        self.__armorPool = input

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__healthPool[self.__level]
        self.__attPower = self.__attPowerPool[self.__level]
        self.__armor = self.__armorPool[self.__level]

class HeroIntelligent(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 50, 100, 150, 200, 250]
        self.attPowerPool = [0, 20, 40, 60, 80, 100]
        self.armorPool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.levelUp = 1

class HeroStrength(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 100, 200, 300, 400, 500]
        self.attPowerPool = [0, 30, 60, 90, 120, 150]
        self.armorPool = [0, 2, 4, 6, 8, 10]
        self.levelUp = 1