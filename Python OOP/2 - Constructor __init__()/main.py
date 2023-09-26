class Hero: 

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("Sniper",200,10,20)
hero2 = Hero("Mirana",100,30,50)
hero3 = Hero("Sniper",700,100,0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)