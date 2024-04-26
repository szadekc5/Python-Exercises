#Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
def sorted_distinct_words(sequence):
    words = sequence.split(",")
    distinct_words = sorted(set(words))
    return distinct_words

input_sequence = input("Enter a comma-separated sequence of words: ")
result = sorted_distinct_words(input_sequence)
print("Distinct words in sorted form:", ", ".join(result))
