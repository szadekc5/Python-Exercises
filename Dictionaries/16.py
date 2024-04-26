#Write a Python program to check if multiple keys exist in a dictionary.
def check_keys_exist(d, keys):
    return all(key in d for key in keys)

sample_dict = {'a': 1, 'b': 2, 'c': 3}

keys_to_check = ['a', 'b', 'd']

if check_keys_exist(sample_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
