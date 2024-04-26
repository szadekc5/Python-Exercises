#Write a Python program to multiply all the items in a list.
def multiply_list(items):
    product = 1
    for x in items:
        product *= x
    return product

print(multiply_list([1, 2, 3, 4]))
