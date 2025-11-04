# 1. Create a dictionary with person details (name, age, city)

person_details ={
    "name":"Abdullah",
    "age":22,
    "city":"FSD"
}
# print(person_details)

# 2. Access values from a dictionary using keys
print(person_details["name"])
print(person_details["city"])
print(person_details["city"])
# print(person_details.get("name"))

# 3. Add a new key-value pair to a dictionary

person_details.update({
    "country":"Pakistan"
})

# 4. Update the value of an existing key
person_details["city"] = "Multan"

# 5. Remove a key-value pair  `pop()`

person_details.pop("country")
print(person_details)


# 6. Check if a key exists in a dictionary

person_details = {
    "name": "Abdullah",
    "age": 20,
    "city": "Faisalabad"
}

# Check if a key exists
if "age" in person_details:
    print("Key 'age' exists in the dictionary.")
else:
    print("Key 'age' does not exist.")


# Second Example 

if "country" not in person_details:
    print("Key 'country' does not exist.")
    

# 7. Get all keys, values, and items from a dictionary

print(person_details.keys())
print(person_details.values())
print(person_details.items())

# 8. Iterate through a dictionary using for loops

# 🔹 Iterate over keys
for i in person_details.keys():
    print(i)

# 🔹 Iterate over values
for i in person_details.values():
    print(i)

# 🔹 Iterate over key–value pairs
for i in person_details.items():
    print(i)
    
# 10. Merge two dictionaries using `update()`


my_dict2 = {
    "name":"abdullah",
    "age":22,
    "roll_number":1234
}
copy_dict = {
    "semster":"5th",
    "project_name":"Voen Clothing Store"
}
my_dict2.update(copy_dict)
print(my_dict2)

