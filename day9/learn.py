# Dictionaries

dictionary = {
    "Name": "John",
    "Age": 25,
    "City": "Sydney",
    "Our Code": 124,
    "ap_2": 1,
    2: 234
}

print(dictionary)
print(dictionary.get("Name"))
print(dictionary["Age"])
print(dictionary["Our Code"])

dictionary["Alias"] = "J J"

print(dictionary)

for key in dictionary:
    print(f"key = {key}, value = {dictionary[key]}")

dictionary = {}
print(dictionary)

nested_dictionary = {
    "Name": "John",
    "address": {
        "city": "Sydney",
        "zipcode": "122222"
    },
    "alias": ["JJ"]
}

print(nested_dictionary)