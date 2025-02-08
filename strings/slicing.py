import json

name = "Apple"

# print("Fruit name :", name[0])
# print("first letters :", name[0:3])

"""
INPUT -> 
PROCESS -> 
OUTPUT -> 
"""

fruits = [{"name": "Apple", "price": 100}, {"name": "banana", "price": 60}]

search_term = "ap"

for (index, fruit) in enumerate(fruits):
    fruit_name = fruit["name"]
    if (search_term in fruit_name.lower()):
        print("Index :",  index + 1)
        print("fruit :", fruit)


    print("\n\n...\n")