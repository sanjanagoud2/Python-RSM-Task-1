class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def startveh(self):
       print("Started")

    def stopveh(self):
       print("stopped")

    def info(self):
       print("Make",self.make)
       print("Model",self.model)
       print("Info",self.year)

class Car(Vehicle):
    def __init__(self,make,model,year,num_doors,fuel_type):
        super().__init__(make,model,year)
        self.num_doors=num_doors
        self.fuel_type=fuel_type

class Motorcycle(Vehicle):      
    def __init__(self,make,model,year,num_doors,top_speed):
        super().__init__(make,model,year)
        self.top_speed=top_speed

class Truck(Vehicle):
    def __init__(self,make,model,year,num_doors,cargo_capacity,num_axles):
         super().__init__(make,model,year)
         self.cargo_capacity=cargo_capacity
         self.num_axles=num_axles


myCar=Car("Swift","Vxi",2014,4,"petrol") 
print("car details")
myCar.startveh()
myCar.info()
print()
myTruck=Truck("Truck","GMCHummerEV",2023,2,"82cubicfeet",4)
print("Truck details")
myTruck.startveh()
myTruck.info()
myTruck.stopveh()
print()
myMotorcycle=Motorcycle("Yamaha","MT15",2018,0,130)
print("Motorcycle details")
myMotorcycle.startveh()
myMotorcycle.info()
myMotorcycle.stopveh() 