from car import Car

car_1 = Car("ford","blue", 2022, 60)
print(car_1.model)
print(car_1.color)
print(car_1.year)
print(car_1.speed_limit)

car_2 = Car("Tesla", "white",2022,80)
print(car_2.model)
print(car_2.color)
print(car_2.year)
print(car_2.speed_limit)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()
car_1.accelerate()