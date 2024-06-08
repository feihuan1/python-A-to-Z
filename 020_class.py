# class is blueprints for objects

class Vehicle:

    def __init__(self, make, modle, speed):
        self.make = make 
        self.modle = modle
        self.speed = speed

    def moves(self):# methods
        print(f"{self.make} {self.modle} Moves at {self.speed} miles per hour...")


my_car = Vehicle("Toyota", "Prius", 70)# no fucking new keyword

my_car.moves()