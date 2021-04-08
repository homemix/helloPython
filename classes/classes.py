class Dog:
    species = "canis familiarise"

    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


Jimmy = Dog("jimmy", "breed1", "brown", 5)
Jack = Dog("Jack", "breed2", "brown", 5)
Tobi = Dog("Tobi", "breed1", "brown", 5)

print(Jimmy.color)
# print(Tobi.description())
print(Jimmy.species)
print(Jack.species)
print(Jack.speak("hello python"))
print(Jack)

