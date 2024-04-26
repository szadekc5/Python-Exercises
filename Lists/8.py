#Write a Python program to check if a list is empty or not.
def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False

# Example usage:
my_list = []  # An empty list
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
