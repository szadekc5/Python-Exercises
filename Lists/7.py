#Write a Python program to remove duplicates from a list.
def remove_duplicates(items):
    return list(set(items))

print(remove_duplicates([2,2,6,4,6,7,1]))
