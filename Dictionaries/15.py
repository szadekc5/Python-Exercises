#Write a Python program to print a dictionary line by line.
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Printing the dictionary line by line:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
