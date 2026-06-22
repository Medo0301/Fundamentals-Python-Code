class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")


my_dog = Dog("Tobi", "Lion head")
my_dog.bark()
some_dog = Dog("Shar", "Huski")
some_dog.name += "ko"
print(some_dog.name)
