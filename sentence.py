# Create a program that ask for a sentence as input.
# Display the number of words, vowels, and consonants in the input.
# ex. input: Bahala kayo dyan
# words: 3
# vowels: 6
# consonants: 8


# Step 1: ask for a sentence as input:
askSentence = input("Type any sentence you want: ")
sentence = askSentence.lower() # no need to write the uppercase vowels so i used .lower to convert uppercased letters to lower.

wordsCount = 0
vowelsCount = 0
consonantsCount = 0
vowels = ["a","e","i","o","u"]

for char in sentence: # loop
    if char == " ": # if-else statements
        wordsCount = wordsCount + 1
    
    if char in vowels:
        vowelsCount = vowelsCount + 1

    if char not in vowels and char.isalpha():  # if char.isalpha(): checks if it char is an alphabet but vowels are not included so it equates to consonants only.
        consonantsCount = consonantsCount + 1


wordsCount = wordsCount + 1

# Step 2: Display the numbers of words, vowels, and consonants in the input.
print("input:",sentence)
print("words:", wordsCount)
print("vowels:", vowelsCount)
print("consonants:", consonantsCount)