x = {"Yellow", "Orange", "Black"}
y = ["Blue", "Green", "Red"]

print("original set",x)
print("original list",y)

list2=list(x)       #converting set into list
print("converting set into list",list2)

y.extend(list2)
print("extending y into list2",y)

z=set(y)
print("converted list into set",z)