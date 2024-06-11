# class is blueprints for objects

class Vehicle:

    def __init__(self, make, model, speed):
        self.make = make 
        self.model = model
        self.speed = speed

    def moves(self):# methods
        print(f"{self.make} {self.model} Moves at {self.speed} miles per hour...")


my_car = Vehicle("Toyota", "Prius", 70)# no fucking new keyword

my_car.moves()
print(my_car.model)

your_car = Vehicle('Tesla', 'model3', 120)

print(your_car.make, your_car.model)
your_car.model = 'modelX'
print(your_car.make, your_car.model)

class Airplane(Vehicle):
    # if define int in child , need call super to get parent property and define its own property
    def __init__(self, make, model, speed, faa_id):
        super().__init__(make, model, speed)
        self.faa_id = faa_id

    def moves(self):# this over-writes the original veihicle
        print('this is a plane, it flies')



class Truck(Vehicle):
    # without super called in init func, it will automaticly inheritant parent
    def moves(self):# this over-writes the original veihicle
        print("rambles alone")

class GolfCart(Vehicle): 
    pass # thsi inheritance everything from parent


cessna = Airplane("Cessna", "Skyhawk", 400, "aa222")
mack = Truck("Mack", "Pinnacle", 70)
print(mack.make)
golf_wagon = GolfCart("Yamaha", "GC100", 30)


cessna.moves()
mack.moves()
golf_wagon.moves()

print(cessna.make)

print('\n\n')
####Polymorphism is a concept that a methods can be interchanged on diferent object, same metjods gives diferent out put, because each child can modify it's own method inheretat from parent
## it just means methods inheretant from parent can behave diferently depends on how they build

for v in (my_car, your_car, cessna, mack, golf_wagon):
    v.moves()
