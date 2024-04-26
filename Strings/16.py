#Write a Python program to remove a newline in Python
def remove_newline(text):
    return text.replace('\n', '')

input_text = "Hello\nWorld\n"
result = remove_newline(input_text)
print(input_text)
print("String after removing newlines:", result)
