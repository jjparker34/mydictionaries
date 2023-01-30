person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# the name of the second child
print(person.get('children')[1])


# name of the cat
print(person['pets']['cat'])


# use for loop to list each child
for i in person['children']:
    print(i)

for i, j in person ['pets'].items():
    print(f'Type of pet:{i} name of pet: {j}')


# print out the pets in this format;
#'type of pet: dog name of pet: fido'

