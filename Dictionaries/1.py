#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'jabłko': 5, 'banan': 3, 'ananas': 7, 'pomarańcza': 2}

# Sort dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by value in ascending order:")
print(sorted_dict_asc)

# Sort dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("\nSorted dictionary by value in descending order:")
print(sorted_dict_desc)

