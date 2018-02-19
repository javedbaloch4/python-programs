#!C:/python/python
print ("Content-type: text/html\n\n")


year = 2020

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{0} is a leap year". format(year))
else:
    print("{0} is not leap year". format(year) )