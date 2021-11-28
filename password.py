# Create a program that check if password is valid
# the password is valid if all the criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*+ etc)
# input: P@ssw0rd+P@ssw0rd
# output: Valid

displayIntro = print("Welcome to Registration! You are about to create your own account. Please sign up for your Username and Password.")
askUsername = input("Username: ")
askPassword = input("Password: ")
capLet = False 
numberChar = False
specialChar = False

if len(askPassword) >= 15: #if-else (a. Greater than 15 letters)
    for char in askPassword: #loop statement
        if char.isalpha(): 
            if char.isupper(): # (b. Have at least one capital letter)
                capLet = True
        elif char.isnumeric(): # (c. Have at least one number)
            numberChar = True
        else:
            specialChar = True # (d. Have at least one special char)
    if capLet == True and numberChar == True and specialChar == True:
        result = "Valid"
    else:
        result = "Invalid"
else: 
    result = "Invalid"
print(result)