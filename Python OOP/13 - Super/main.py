class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print (f"{self.name} dengan health {self.health}")

class heroIntelligent(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,100)
        super().__init__(name,100)
        super().showInfo()

class heroStrength(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        super().showInfo()

lina = heroIntelligent("Lina")
axe = heroStrength("Axe")