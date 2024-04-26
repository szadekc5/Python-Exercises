#Write a Python program to get the largest number from a list.
def largest_number(list):
    for i in list:
        largestNum = max(list) 
        return largestNum
    
print(largest_number([1,7,6,8,19]))