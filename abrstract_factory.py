import abc

#Abstract Products 
class AbstractAnimal(abc.ABC):
    @abc.abstractmethod
    def voice(self):
        pass

class Toy(abc.ABC):
    @abc.abstractmethod
    def play(self):
        pass

class Food(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass

# Concrete Products
class Dog(AbstractAnimal):
    def voice(self):
        return "Woof"

class Bone(Toy):
    def play(self):
        return "Chewing a bone"

class Meat(Food):
    def eat(self):
        return "Eating meat"

class Cat(AbstractAnimal):
    def voice(self):
        return "Meow"

class Yarn(Toy):
    def play(self):
        return "Playing with a yarn"

class Fish(Food):
    def eat(self):
        return "Eating fish."

class AbstractPetFactory(abc.ABC):
    @abc.abstractmethod
    def create_animal(self):
        pass

    @abc.abstractmethod
    def create_toy(self):
        pass

    @abc.abstractmethod
    def create_food(self):
        pass

# Concrete Factories 
class DogFactory(AbstractPetFactory):
    def create_animal(self):
        return Dog()

    def create_toy(self):
        return Bone()

    def create_food(self):
        return Meat()

class CatFactory(AbstractPetFactory):
    def create_animal(self):
        return Cat()

    def create_toy(self):
        return Yarn()

    def create_food(self):
        return Fish()


def get_pet(factory: AbstractPetFactory):
    pet = factory.create_animal()
    toy = factory.create_toy()
    food = factory.create_food()

    print(pet.voice())
    print(toy.play())
    print(food.eat())

print("Dog Factory")
get_pet(DogFactory())

print("Cat Factory:")
get_pet(CatFactory())
