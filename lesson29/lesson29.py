# Lesson 29
word = input("Enter a word: ")
word2 = word
word = word.lower()

consonants = 0

for i in word:
    if i == "b" or i == "c" or i == "d" or i == "f" or i == "g" or i == "h" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z":
        consonants += 1
    else:
        continue

print(f"There are {consonants} consonants in the word \"{word2}\"")
# End of Lesson 29