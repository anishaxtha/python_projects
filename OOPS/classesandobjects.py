class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    
blu =Parrot("Blu",15)
woo = Parrot("Woo",10)

# access the class attribute 
print("Blu is a {}".format(blu.__class__.species))
print("woo is a {}".format(woo.__class__.species))

# access the instances attribute
print("{} is {} years old.".format(blu.name,blu.age))
print("{} is {} years old.".format(woo.name,woo.age))
