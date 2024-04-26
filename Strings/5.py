#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_first_two_chars(str1, str2):
    
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    
    
    result = new_str1 + ' ' + new_str2
    return result


string1 = ("Warszawa")
string2 = ("Merito")

result_string = swap_first_two_chars(string1, string2)
print("Result:", result_string)

