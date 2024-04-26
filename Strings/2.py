#Write a Python program to count the number of characters (character frequency) in a string.
def char_freq(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    
    return dict

print(char_freq('Grzegrzółka')) 
