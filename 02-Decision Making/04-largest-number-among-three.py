num1 = 11
num2 = 25
num3 = 15

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number between", num1, ",", num2, "and", num3, "is", largest)