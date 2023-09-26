class Hero:
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

class heroIntelligent(Hero):
    pass

class heroStrength(Hero):
    pass

lina = Hero("Lina",100)
techies = heroIntelligent("Techies",50)
axe = heroStrength("Axe",200)

print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)