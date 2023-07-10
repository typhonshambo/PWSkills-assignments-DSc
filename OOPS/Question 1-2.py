'''
Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle.

Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity.
'''

class vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name = name_of_vehicle
        self.max_speed = max_speed
        self.avg_of_vehical = average_of_vehicle
    
class car(vehicle):
    def seating_capacity(self, capacity):
        return self.name, capacity

car = car('verna', 120, 30)
a = car.seating_capacity(4)
print(a)
