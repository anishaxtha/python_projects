# class MyNewClass:
#     ''' This is the docstrings. I have created the new class'''
    
# print(MyNewClass.__doc__)






# class student:
#     ''' I am new to this class and i am here to
#      explore the technology in depth'''
#     age = 10 
#     ef greet(self):
#         print("Helloo world!")


# # creating the new object of class student 
# anna = student()
# print(student.age)
# print(student.greet)
# print(student.__doc__)
# anna.greet()


# class shark:
#     animal_type ="fish"
#     location = "ocean"
#     followers = 10

# new_shark = shark()
# print(new_shark.animal_type)
# print(new_shark.location)
# print(new_shark.followers)





class Shark:
    def __init__(self,name, age):
        self.name = name
        self.age = age
new_shark = Shark("jesica", 10)
print(new_shark.name)
print(new_shark.age)


steave = Shark("steave", 9)
print(steave.name)
print(steave.age)