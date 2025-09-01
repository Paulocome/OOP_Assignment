# Base class
class Vehicle:
    def move(self):
        pass  # generic method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

if __name__ == "__main__":
    car1 = Car()
    plane1 = Plane()

    vehicles = [car1, plane1]

    for v in vehicles:
        v.move()
