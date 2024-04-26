#Write a Python program to count the number of items in a dictionary value that is a list.
def count_list_items(d):
    count = 0
    for value in d.values():
        if isinstance(value, list):
            count += len(value)
    return count

sample_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'string'}

num_list_items = count_list_items(sample_dict)
print("Number of items in dictionary values that are lists:", num_list_items)
