#Write a program that takes a sentence as input and extracts the substring between the 5th and 10th characters (inclusive). Print the extracted substring.
# Input sentence from the user
a = input("Enter a sentence: ")
# Check if the sentence has at least 10 characters
if len(a) >= 10:
    substring = a[4:10]
    print("Extracted substring:",substring)
else:
    print("Sentence is too short Type Again")
