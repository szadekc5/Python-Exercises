#Write a Python program to remove spaces from dictionary keys.
def remove_spaces_from_keys(d):
    return {key.replace(' ', ''): value for key, value in d.items()}

sample_dict = {'sernik': 10, 'jabłecznik': 20, 'drożdżówka z serem': 30}

result = remove_spaces_from_keys(sample_dict)
print("Dictionary after removing spaces from keys:")
print(result)
