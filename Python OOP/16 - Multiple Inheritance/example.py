class Team:

    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(f"Team: {self.team}")


class Type:

    def setType(self, type):
        self.type = type

    def showType(self):
        print(f"Type: {self.type}")


class Hero(Team, Type):

    def __init__(self, name, health):
        self.name = name
        self.health = health


ucup = Hero("Ucup", 100)
ucup.setTeam("Merah")
ucup.setType("Pecundang")

ucup.showTeam()
ucup.showType()
print(ucup.__dict__)