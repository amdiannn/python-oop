class Hero: 
    # Class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"Membuat Hero dengan Nama {inputName}")

hero1 = Hero("Sniper",200,10,20)
hero2 = Hero("Mirana",100,30,50)
hero3 = Hero("Sniper",700,100,0)