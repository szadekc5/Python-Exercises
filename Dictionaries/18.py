#Write a Python program to replace dictionary values with their sums.
def replace_with_sum(d):
    for key, value in d.items():
        if isinstance(value, list):
            d[key] = sum(value)
    return d

sample_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'string'}

modified_dict = replace_with_sum(sample_dict)
print("Modified Dictionary with sums:")
print(modified_dict)
