# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def exchange_first_last(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

inputString = "merito"
result = exchange_first_last(inputString)
print(result)
