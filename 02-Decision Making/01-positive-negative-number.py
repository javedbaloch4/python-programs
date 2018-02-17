#!C:/python/python
print ("Content-type: text/html\n\n")

number = -12

if number > 0:
    print("%3.0f is a positive number" %number)
elif number == 0:
    print("%3.0f is zero" %number)
else:
    print("%3.0f is a negative number" %number)