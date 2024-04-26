#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sort_list_tuples(tuples):
    return sorted(tuples, key=lambda x: x[-1])

print(sort_list_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
