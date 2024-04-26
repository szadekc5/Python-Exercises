#Write a Python program to find the list of words that are longer than n from a given list of words.
def find_long_words(word_list, n):
    # Create a list to store words longer than n
    long_words = []
    
    # Iterate through each word in the word list
    for word in word_list:
        # Check if the length of the word is greater than n
        if len(word) > n:
            # If so, add the word to the list of long words
            long_words.append(word)
    
    return long_words

# Example usage:
word_list = ["Jabłko", "Agrest", "banan", "kiwi", "gruszka",]
n = 5
long_words = find_long_words(word_list, n)
print(f"Words longer than {n} characters:", long_words)

