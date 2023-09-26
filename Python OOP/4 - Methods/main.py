class Hero: 
    # Class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # Method tanpa return dan argumen (Void function)
    def siapa(self):
        print("Namaku adalah " + self.name)

    # Method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Mario Bros", 90, 5, 10)

hero1.siapa()
hero1.healthUp(50)
print(hero1.getHealth())