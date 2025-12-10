employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

post=dict.fromkeys(employees,defaults)

print(post)