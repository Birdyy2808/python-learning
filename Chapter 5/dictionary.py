# Properties of dictionary
# 1. They are Ordered after 3.7+ version, earlier unordered
# 2. They have unique values, no duplicate
# 3. They are mutable
# 4. They are indexed meaning when we give marks["Mummy"], it directly gives value and does not search each index

d={} #Empty dictionary 

marks={
    "Harry":23,
    "Mummy":100,
    "Vaibhav":80,
    "Geeta":110
}
# To get values using keys
print(marks["Mummy"])
print(marks, type(marks))


# Methods in dictionary
# Gets he items in dict
print(marks.items())

# Get keys
print(marks.keys())

# Get values
print(marks.values())

# Update values
marks.update({"Vaibhav":90})

# print(marks.items())
# Get the value using GET method
# The below gives "none" if key doesn't exist
print(marks.get("Vaibhav"))
# The below gives "error" if key doesn't exist
# print(marks["Vaibhav1"])


# list of dictionary
identity = [
    {
        "id":1,
        "name":"Vaibhav"
    },
    {
        "id":2,
        "name":"Mummy"
    },

]
print(identity[0]["name"])
