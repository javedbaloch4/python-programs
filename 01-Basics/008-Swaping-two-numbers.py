#!C:/python/python
print ("Content-type: text/html\n\n")


x = 5
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x: {}'.format(x))
print('The value of y: {}'.format(y))