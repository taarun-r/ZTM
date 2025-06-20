# Dictionary 2

mixed_dict = {
    "name": "Alice",       # String
    "age": 30,             # Integer
    "is_student": False,   # Boolean
    "scores": [85, 90, 78], # List
    "details": {           # Nested Dictionary
        "height": 5.7,
        "weight": 65
    }
}

# print("name" in mixed_dict)  # Check if 85 is in the list of scores

# Keys - Simply checkes the keys in the dictionary
# print(mixed_dict.keys())  # Returns a view object displaying a list of all the keys
# Values - Simply checkes the values in the dictionary
# print(mixed_dict.values())  # Returns a view object displaying a list of all the values
# Items - Simply checkes the items in the dictionary
# print(mixed_dict.items())  # Returns a view object displaying a list of all the key-value pairs
# Clear - Clears the dictionary
# mixed_dict.clear()  # Removes all items from the dictionary
# Copy - Creates a shallow copy of the dictionary
# copied_dict = mixed_dict.copy()  # Returns a shallow copy of the dictionary
# Pop - Removes the specified key and returns its value
# removed_value = mixed_dict.pop("age")  # Removes the key "age" and returns its value
# print(removed_value)  # Prints the value of the removed key
# popitem - Removes and returns the last inserted key-value pair
# last_item = mixed_dict.popitem()  # Removes and returns the last inserted key-value pair
# print(last_item)  # Prints the last inserted key-value pair
# Update - Updates the dictionary with the specified key-value pairs
# mixed_dict.update({"city": "New York", "is_student": True})  # Adds new key-value pairs or updates existing ones
# print(mixed_dict)  # Prints the updated dictionary