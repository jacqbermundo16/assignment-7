#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8


#steps
# ask for input
def askInput():
    _sentence = input("Write a sentence: ")
    return _sentence

# create a function that counts the number of words
def count(sentencef):
    countWord = 1
    for w in sentencef:
        if w == ' ':
            countWord = countWord + 1
    return countWord

# create a function that counts the number of vowels
def count2(sentenceg):
    countVowels = 0
    char = 'aeiou'
    for v in sentenceg:
        for d in char:
            if v == d:
                countVowels = countVowels + 1
    return countVowels

# create a function that counts the number of consonants
def count3(sentenceh):
    countConsonants = 0
    char = 'bcdfghjklmnpqrstvwxyz'
    for c in sentenceh:
        for e in char:
            if c == e:
                countConsonants = countConsonants + 1
    return countConsonants

# display the results
def display(_words, _vowels, _consonants):
    print(f"words: {_words}\nvowels: {_vowels}\nconsonants: {_consonants}")

sentence = askInput()
words = count(sentence)
vowels = count2(sentence)
consonants = count3(sentence)
display(words, vowels, consonants)
