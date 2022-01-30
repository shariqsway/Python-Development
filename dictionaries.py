# Dictionaries - Key/Value Pairs.

customer = {
    "name": "Mohammad Shariq",
    "age": 31,
    "is_verified": True
}

# Accessing dictionary
print(customer["name"])

# Updating the value
customer["name"] = "Mohammad Shariq Siddiqui"

# Accessing dictionary - Better approach
print(customer.get("name"))

# Accessing dictionary - Better approach (Provide default value)
print(customer.get("birthday", "March 9, 1990"))
