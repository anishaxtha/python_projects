# excersise faulty calculator
print("Enter the first number:")
num1= int(input())
print("Enter the second number:")
num2 = int(input())
print("So what you want?" +'+,-,*,/')
num3 = input()

if num1==44 and num2==5 and num3 =='*':
 print('555')
elif num1==55 and num2==7 and num3 =='+':
 print('44')
elif num1==77 and num2==4 and num3 =='/':
 print('9')
elif num3=='*':
    multiply = num1+num2
    print(num3)
elif num3 =='+':
    add = num1+num2
    print(add)
elif num3 =='/':
    divide = num1/num2
    print(divide)
elif num3 =='-':
    substract = num1-num2
    print(substract)
elif num3 =='%':
    percent = num1%num2
    print(percent)
else:
    print("Error! please check your input")




