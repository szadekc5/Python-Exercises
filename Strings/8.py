# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def longest_word(words):
    longest = words[0]
    longest_length = len(longest)

    for word in words[1:]:
        if len(word) > longest_length:
            longest = word
            longest_length = len(word)

    return longest, longest_length

word_list = ['wolf', 'penguin', 'elephant', 'dog']
longest_word, length = longest_word(word_list)
print("Longest word:", longest_word)
print("Length of the longest word:", length)
