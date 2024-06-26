import string
import sys

def ispangram(str1, alphabet=string.ascii_lowercase):
    
    alphaset = set(alphabet)
    
    
    str_set = set(str1.lower())
    
    
    return alphaset <= str_set


print(ispangram('The quick brown fox jumps over the lazy dog')) 
