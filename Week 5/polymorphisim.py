class Vehicle:
    def move(self):
        print("A vehicle can move in any direction.")


class Car(Vehicle):
    def move(self):
        print("It is driven on a tarmac road.")


class Plane(Vehicle):
    def move(self):
        print("Flies in the sky. ")


class Boat(Vehicle):
    def move(self):
        print("Cruises on the sea. ")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaled on land. ")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()