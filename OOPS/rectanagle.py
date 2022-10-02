class Rectangle:
    def __init__(self,length, breadth, unit_cost):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_Perimeter(self):
        return 2*(self.length  + self.breadth)
    
    def get_Area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_Area
        return area*self.unit_cost

r=Rectangle(160,120,7000)
# print("Area of rectangle", r.get_Area)
# print("perimeter of rectange", r.get_Perimeter)
# print("calculate cost of rectangle", r.calculate_cost)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))