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
# check if the characters are greater than 15
# check if it contains a capital letter
# check if it contains a number
# check if it contains special character
# print the result

password = askPassword()
print(password)