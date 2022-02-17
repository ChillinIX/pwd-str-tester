# imports
import string
from random import *
from getpass import getpass
from datetime import datetime

#Title
print("-----------------------------------")
print("Password Strength tester")
print("-----------------------------------")

# Declared Variables
userPass = getpass("Please enter Your Password: ")
password = string.ascii_lowercase + string.digits + string.ascii_uppercase
answer = ""
count = 0
startTime = datetime.now()

# While loop for trying different random combinations of passwords
while (answer != userPass):
    answer = ""
    count += 1
    for letter in range (len(userPass)):
        guessLetter = password[randint(0,61)]
        answer = str(guessLetter) + str(answer)
# To show the combinations of passwords used against the program remove the # below
    print(count, "Attempts:", answer)



# Printing of the cracked password
print("-----------------------------------")
print("Your password is:", answer)
print(" ")
print("Time to crack password:",datetime.now() - startTime)
print("Completed in", count, "password attempts")
print("-----------------------------------")