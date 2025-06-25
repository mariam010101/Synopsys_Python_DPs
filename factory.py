class Dog:
    def __init__(self,name):
        self.name=name
    def get_voice(self):
        return f"{self.name} is a dog"

class Cat:
    def __init__(self,name):
        self.name=name
    def get_voice(self):
        return f"{self.name} is a cat"
    
class AnimalFactory:
    @staticmethod

    def createAnimal(voice,name):
        if voice=="dog":
            return Dog(name)
        elif voice=="cat":
            return Cat(name)
        else:
            return "whaat?"

animal1=AnimalFactory.createAnimal("dog","Winnie")
print(animal1.get_voice())
animal2=AnimalFactory.createAnimal('cat','Luna')
print(animal2.get_voice())


