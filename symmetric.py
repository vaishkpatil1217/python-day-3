x = {10, 20, 30, 40, 50}
y= {30, 40, 50, 60, 70}

print(x)
print(y)

z=x^y                                #symmetric(method 1)
print("semetric difference",z)

z=x.symmetric_difference(y)              #symmetric(method 2)
print("semetric difference",z)

