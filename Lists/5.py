#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def match_words(words):
    return sum(1 for word in words if len(word) > 1 and word[0] == word[-1])

print(match_words(['abc', 'xyz', 'aba', '1221']))
