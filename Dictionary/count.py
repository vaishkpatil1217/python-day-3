string1 = "vaishnavi"
count={}
for char in string1:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)
    
