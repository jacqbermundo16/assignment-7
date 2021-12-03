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
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    capCount = 0
    if countPass > 15:
        for c in password_:
            for d in capital:
                if c == d:
                    capCount = capCount + 1
                    if capCount >= 1:
                        print('capital letter is present')
                    else: 
                        print('add a capital letter to your password')
                    
                    
    else:
        print('please add more characters')
# check if the characters are greater than 15
# check if it contains a capital letter
# check if it contains a number
# check if it contains special character
# print the result

password = askPassword()
count(password)