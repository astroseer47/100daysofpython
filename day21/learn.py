# Class Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("underwater")

    def swim(self):
        print("Swimming")


nemo = Fish()
nemo.swim()
nemo.breathe()

print(nemo.num_eyes)