class Wizard:
    def __init__(self, name, color, values):
        self.name = name
        self.color = color
        self.house = self.nameOfHouse()
        self.values = values  # ["Bravery", "helping others", "chivalry"]

    @classmethod
    def nameOfHouse(cls):
        if cls is Gryffindor:
            return "Gryffindor"
        elif cls is Hufflepuff:
            return "Hufflepuff"
        elif cls is Ravenclaw:
            return "Ravenclaw"
        else:
            return "Slytherin"

    def getValues(self):
        return self.values


class Gryffindor(Wizard):
    def __init__(self, name):
        Wizard.__init__(self, name, "red", ["Bravery", "helping others", "chivalry"])


class Hufflepuff(Wizard):
    def __init__(self, name):
        Wizard.__init__(
            self, name, "yellow", ["Hard work", "patience", "loyalty", "fair play"]
        )


class Ravenclaw(Wizard):
    def __init__(self, name):
        Wizard.__init__(
            self, name, "blue", ["Intelligence", "knowledge", "planning ahead", "wit"]
        )


class Slytherin(Wizard):
    def __init__(self, name):
        Wizard.__init__(
            self,
            name,
            "green",
            ["Ambition", "cunningness", "heritage", "resourcefulness"],
        )


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
