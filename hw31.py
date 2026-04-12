class McLaren():
    def fueltype(self):
        print("The fuel type of a McLaren is gasoline.")
    def maxspeed(self):
        print("The max speed of a McLaren is 341 km/h.")
    def mileage(self):
        print("The mileage of a McLaren is 418 miles.")

class Mercedes():
    def fueltype(self):
        print("The fuel type of a Mercedes is also gasoline.")
    def maxspeed(self):
        print("The max speed of a Mercedes is 352 km/h.")
    def mileage(self):
        print("The mileage of a Mercedes is 390 miles.")

mclaren = McLaren()
mercedes = Mercedes()

for car in (mclaren, mercedes):
    car.fueltype()
    car.maxspeed()
    car.mileage()