print("++++++++++++++++++++\n")
print(" EXERCISE")


class House:
    def __init__(self, type, age, material, roof, color):
        self.type = type
        self.age = age
        self.material = material
        self.roof = roof
        self.color = color

    def description(self):
        return f"The {self.color} house is {self.age} years old - It has {self.roof} roof top, it is a {self.type} unit "


red_house = House("bungalow", 15, "brick", "Corrugated", "Red")
pink_house = House("Family", 20, "wood", "Corrugated", "pink")
print(red_house.description())
print(pink_house.description())
