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
# display the results

sentence = askInput()
words = count(sentence)
vowels = count2(sentence)
print(words, vowels)