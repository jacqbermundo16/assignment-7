# Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

#steps
# ask for input
def askPassword():
    _password = input('Input password: ')
    return _password
# create a function that counts the length of the password
def count(password_):
    countPass = len(password_)
    return countPass
  
# check if it has a capital letter
def checkCaps(passwordq):
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    capCount = 0
    for c in passwordq:
        for d in char:
            if c == d:
                capCount = capCount + 1
    return capCount
           
# check if there is a number
def checkNum(passwordw):
    char = '0123456789'
    numCount = 0
    for e in passwordw:
        for f in char:
            if e == f:
                numCount = numCount +1
    return numCount 
# check if it contains special character
def checkSpec(passworde):
    char = '~!@#$%^&*()_+=-\/.,<>:;'
    specCount = 0
    for g in passworde:
        for h in char:
            if g == h:
                specCount = specCount + 1
    return specCount
# print the result

password = askPassword()
length = count(password)
caps = checkCaps(password)
nums = checkNum(password)
specs = checkSpec(password)
print(length, caps, nums, specs)