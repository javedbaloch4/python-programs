# Program to find the area of a Triangle

a = 5
b = 6
c = 7

# Calculate the semi perimeter
s = (a + b + c ) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("The are of a Triangle is %0.2f" %area)
