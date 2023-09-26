class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )

class heroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # override method
    def showInfo(self):
        print("showInfo di subclass heroIntelligent")
        print("{}\n\tType: Intelligent\n\tHealth: {}".format(
            self.name,
            self.health
            )
        )

class heroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = heroIntelligent("Lina")
axe = heroStrength("Axe")

lina.showInfo()
axe.showInfo()