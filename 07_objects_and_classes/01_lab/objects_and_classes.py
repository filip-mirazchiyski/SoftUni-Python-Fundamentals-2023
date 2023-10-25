class Car:
    cars_number = 0 #Class attribute - it remains unchanged for all instances, unless you change it in the Class
    def __init__(self, brand, model, year):
        self.brand = brand #self._brand = brand
        self.model = model
        self.year = year

    def get_branch_info(self):
        return.self(brand)

    def change_brand(self):
        self._brand(new_brand)

car1 = Car(brand= "Mercedes", model= "190", year= "1995") #Adding an instance to a class
print(car1.brand)
car1.brand = "BMW" #Values of an instance can be changed
print(car1.brand)
print(car1.__dict__)
Car.cars_number += 22
print(Car.cars_number)

#car1 = ["Brand: Mercedes", "Model: 190", "Fuel: Diesel", "Year: 1995"]
#car2 = ["Brand: BMW", "Model: 323ix", "Fuel: Petrol", "Year: 1998"]