#Write a Python program to remove the nth index character from a nonempty string.
def remove_nth_char(string, n):
    return string[:n] + string[n+1:]

inputString = "merito"
indexToRemove = 1
result = remove_nth_char(inputString, indexToRemove)
print("String after removing the character at index", indexToRemove, ":", result)
