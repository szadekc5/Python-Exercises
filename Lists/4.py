#Write a Python program to get the smallest number from a list.
def smallest_number(list):
    for i in list:
        largestNum = min(list) 
        return largestNum
    
print(smallest_number([1,7,6,8,19]))