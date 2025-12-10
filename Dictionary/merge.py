x = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
y = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print("originl dictionary",x)
print("originl dictionary",y)
z = {**x,**y}
print("x & y merge dictionary",z)
