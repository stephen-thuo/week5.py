class Vehicle:
    def __init__(self, make, model, year, engine_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity

        def display_identity(self):
            print(f"The {self.year} {self.make} {self.model} {self.engine_capacity}'s is one of the best cars ever produced.")

        def make_vehicle (self):
            print(f"The {self.make} {self.model}'s is a new model vehicle.")

        def pickup_speed (self):
            print(f"The {self.make} {self.model}'s goes from zero to a hundred kilometers per hour in three seconds.")

        def get_engine_capacity(self): 
                return self.engine_capacity


        def get_engine_capacity (self):
            if engine_capacity >= 2000:
                self_engine_capacity = engine_capacity
            else:
                print("Diesel consumption is low!")
                

class Fourwheel(Vehicle):
    def pickup_speed(self):
        print(f"{self.make} {self.model} picks to a hundred kilometers per hour under five seconds.")
class Threewheel(Vehicle):
    def pickup_speed(self):
        print(f"{self.make} {self.model} picks to a hundred kilometers per hour under seven seconds.")

def main():
    vehicle1 = FourWheel("Mercedes Benz", "C-Class", 2023, 2200)  
    vehicle2 = ThreeWheel("Tuk-tuk", "Classic", 2020, 1000)      

    vehicle1.display_identity()
    vehicle1.pickup_speed()

    vehicle2.display_identity()
    vehicle2.pickup_speed()

    print("Vehicle 1 Engine Capacity:", vehicle1.get_engine_capacity())  
    vehicle1.set_engine_capacity(2500)
    print("Vehicle 1 New Engine Capacity:", vehicle1.get_engine_capacity())
