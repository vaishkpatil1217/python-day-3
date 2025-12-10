x = {10, 20, 30, 40, 50}
y = {30, 40, 50, 60, 70}
print(x)
print(y)

z=x.difference(y)               #difference of x (method 1)
print("difference of x",z)

z=x-y                           #difference of x (method 2)
print("difference of x",z)

z=y.difference(x)               #difference of y (method 1)
print("difference of y",z)

z=y-x                           #difference of y (method 2)
print("difference of y",z)