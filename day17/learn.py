class User:
    pass


user_1 = User()

user_1.id = 1
user_1.name = "HI"

print(user_1.name)


class Car:
    # Constructor
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def enter_race_mode(self):
        self.capacity = 2

bmw_car = Car("BMW", 6)
print(bmw_car.name)

a_car = Car("A", 13)
print(a_car.capacity)

a_car.enter_race_mode()
print(a_car.capacity)