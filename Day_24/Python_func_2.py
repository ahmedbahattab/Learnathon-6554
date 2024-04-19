def count_word_frequency(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}
    
    # Iterate through the words in the list
    for word in words:
        # Increment the frequency count for each word in the dictionary
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq

# Example usage:
input_string = "This is a sample string. This string contains some words, and some words are repeated."
frequency_dict = count_word_frequency(input_string)
print(frequency_dict)
