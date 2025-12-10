x = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print("original dictionary",x)

del x['profession']
print("Updated dictionary after removing 'profession':",x)


print("printing all key value in pair:")
for i in x:
 print(i,":",x[i])
 
 
keys1="age"             #age exist or not
if keys1 in x:
     print("Key exist :",keys1)
else :
    print("Key not exist :",keys1)

