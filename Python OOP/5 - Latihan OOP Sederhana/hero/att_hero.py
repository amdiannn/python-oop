# Attribute Hero

class Hero:

    def __init__(self,name,health,attack,defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def menyerang(self, lawan):
        print(f"\n{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(f"{self.name} diserang {lawan.name}")

        damage_diterima = attack_lawan/self.defense
        print(f"Damage diterima: {str(damage_diterima)}")

        self.health -= damage_diterima
        print(f"Health {self.name}: {str(self.health)}")