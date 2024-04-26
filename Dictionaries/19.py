#Write a Python program to get the total length of all values in a given dictionary with string values.
def total_length_of_values(d):
    total_length = sum(len(value) for value in d.values() if isinstance(value, str))
    return total_length

original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

total_length = total_length_of_values(original_dict)
print("Total length of all values of the dictionary with string values:", total_length)
