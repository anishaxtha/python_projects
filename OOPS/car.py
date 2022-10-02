class Car:
    def __init__(self,model, color,year, speed_limit):
        self.model = model
        self.color = color
        self.year = year
        self.speed_limit =speed_limit 
        
    def drive(self):
        print("This car is driving ")
    def stop(self):
        print("This car is stopped")
    def accelerate(self):
        print("This car is accelerating")
    def change_gear(self):
        print("This car is changing the gear")
    