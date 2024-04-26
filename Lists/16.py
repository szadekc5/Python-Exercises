#Write a Python program to flatten a shallow list.

import itertools

original_list = [[2, 5, 1], [7, 5, 6], [3], [2, 9, 0]]

new_merged_list = list(itertools.chain(*original_list))

print(new_merged_list)


