sample = {
    "name": "Kelly",                # Keys to remove
    "age": 25,                      #keys = ["name", "salary"]
    "salary": 8000,
    "city": "New york"

}

sample.pop("salary")
sample.pop("name")

print(sample)