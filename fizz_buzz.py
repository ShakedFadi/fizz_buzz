__author__ = 'knedlus'

import os

def clear():
    os.system("clear")
    if os.name == "nt":
        os.system("cls")

clear()
print "Welcome to Fizz Buzz"
while True:
    try:
        user_input = int(raw_input("""\n
Please choose a number in range 1-100: """))

    except ValueError:
        clear()
        print "Please type an integer!"
        continue


    if user_input < 1 or user_input > 100:
        clear()
        print "Please choose your number within the given range!"
        continue

    else:
        clear()
        print "Entered number: %i\n" %(user_input)
        for i in range(1,user_input+1):
            if i % 3 == 0 and i % 5 == 0:
                print "fizzbuzz"
            elif i % 5 == 0:
                print "buzz"
            elif i % 3 == 0:
                print "fizz"
            else:
                print i
    break