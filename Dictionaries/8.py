#Write a Python program to remove duplicates from the dictionary.
def remove_duplicates(d):
    unique_dict = {}
    for key, value in d.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict

sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

result = remove_duplicates(sample_dict)
print("Dictionary after removing duplicates:", result)
