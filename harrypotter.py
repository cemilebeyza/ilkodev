class Wizard:
    def _init_(self, name, color, house):
        self.name = name
        self.color = color
        self.house = house


class Gryffindor(Wizard):
    def _init_(self, name):
        Wizard._init_(self, name, "red")

    def nameOfHouse(self):
        return "Gryffindor"

    def getValues(self):
        return ["Bravery", "helping others", "chivalry"]


class Hufflepuff(Wizard):
    def _init_(self, name):
        Wizard._init_(self, name, "yellow")

    def nameOfHouse(self):
        return "Hufflepuff"

    def getValues(self):
        return ["Hard work", "patience", "loyalty", "fair play"]


class Ravenclaw(Wizard):
    def _init_(self, name):
        Wizard._init_(self, name, "blue")

    def nameOfHouse(self):
        return "Ravenclaw"

    def getValues(self):
        return ["Intelligence", "knowledge", "planning ahead", "wit"]


class Slytherin(Wizard):
    def _init_(self, name):
        Wizard._init_(self, name, "green")

    def nameOfHouse(self):
        return "Slytherin"

    def getValues(self):
        return ["Ambition", "cunningness", "heritage", "resourcefulness"]


while True:
    name = input("Enter your name: ")
    color = input("Favourite Color: ")

    if color == "red":
        wizard = Gryffindor(name)

    elif color == "yellow":
        wizard = Hufflepuff(name)

    elif color == "blue":
        wizard = Ravenclaw(name)

    elif color == "green":
        wizard = Slytherin(name)

    else:
        print("Wrong color")
        break

    print("Your House: " + wizard.nameOfHouse())
    print("Your Values: " + str(wizard.getValues()))
