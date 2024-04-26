# Write a Python script to check whether a given key already exists in a dictionary.

# Sample dictionary
my_dict = {'jabłko': 5, 'gruszka': 3, 'ananas': 7, 'kokos': 2}

# Given key to check
key_to_check = 'kokos'

# Using the 'in' operator
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")


