#Write a Python program to count the frequency of a dictionary.
# Import the 'Counter' class from the 'collections' module.
from collections import Counter

# Define a function 'test' that takes a dictionary 'dictt' as an argument.
def test(dictt):
    # Use the 'Counter' class to count the frequency of values in the dictionary.
    result = Counter(dictt.values())
    
    # Return the result as a Counter object.
    return result

# Create a dictionary 'dictt' where the keys represent grades ('V', 'VI', etc.) and the values are integers.
dictt = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}

# Print a message indicating the start of the code section and display the original dictionary.
print("\nOriginal Dictionary:")
print(dictt)

# Print a message indicating the purpose and generate a frequency count of values in the 'dictt' dictionary using the 'test' function.
print("\nCount the frequency of the said dictionary:")
print(test(dictt)) 
