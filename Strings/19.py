#Write a Python program to display a number with a comma separator.
def format_with_commas(number):
    return "{:,}".format(number)

number = 90000000000
formatted_number = format_with_commas(number)
print("Number with comma separator:", formatted_number)
