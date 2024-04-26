#Write a Python script to add a key to a dictionary.
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

sample_dict = {0: 10, 1: 20}
new_key = 2
new_value = 30

result = add_key_to_dict(sample_dict, new_key, new_value)
print("Expected Result:", result)

