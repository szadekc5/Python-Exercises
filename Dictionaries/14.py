#Write a Python program to get the key, value and item in a dictionary.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over the dictionary:")
for key, value in sample_dict.items():
    print("Key:", key)
    print("Value:", value)
    print("Item (key-value pair):", (key, value))

