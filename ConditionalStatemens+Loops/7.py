#Write a Python program that checks whether a string represents an integer or not.
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(is_integer("123"))
print(is_integer("12.3"))
print(is_integer("abc"))
print(is_integer("-456"))
