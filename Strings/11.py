#Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index_chars(string):
    return string[::2]

input_string = "merito"
result = remove_odd_index_chars(input_string)
print(result)
