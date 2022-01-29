# bartender.py

# import random module from Python library
import random

# define function 'age()' to collect and validate user's age
def age():
    print("age() has been called") ### Debugging prompt - delete in final code
    # assign user input to variable 'age'
    age_input = input("Please enter your age, in years:\n> ")
    
    print(f">>> {age_input}")  ### Debugging prompt - delete in final code
    
    # use try...except block to vailidate user input
    try:
        # tests to see if the 'age' value can be converted to an integer
        int(age_input) 
        # assigns True to variable 'it_is' if conversion is successful
        it_is = True
    except ValueError:
        # assigns False to variable 'it_is' if conversion returns an error (user did not enter a number)
        it_is = False

    print(it_is)  ### debugging prompt - delete in final code
    
    # if-statement to confirm validity of user input for 'age'
    if it_is == True:
        # print string to confirm user entered a number when prompted
        print("You have entered a valid age.")
        # create global variable 'age_num' for use in other functions
        global age_num
        # convert 'age_value' to integer and assign to 'age'
        age_num = int(age_input)
        print(f"---{age_num}")
        return age_num
        
    else:
        # print string to prompt user to re-enter age
        print("You did not enter a valid age.  Please try again.")
        # call age() function again to loop user back to 'age' input()
        age()


# define start() function that will be called to begin the game
def start():
    print("start has been called") ### Debugging prompt - delete in final code
    # call 'age()' function
    age () 
    
    # if-statement to confirm validity of user input for 'age'
    if age_num <= 0:
        # print string to confirm user entered a number when prompted
        print(f"I'm sorry, {name}. It's hard to play a game when you haven't even been born yet!")
    elif age_num > 0 and age_num < 15:
        print(f"I'm sorrry, {name}.  You are a little young to be drinking.  Try again when you're older...")
    else:
        # print string 
        print("next step...")
        # call start() function again to loop user back to 'age' input()
        

    print("<<<< exit start()")  ### Debugging prompt - delete in final code
   #### find out why variable has multiple values if start() loops

### Game's main code block ###

# 1. Greeting
# assign user input to variable 'name'
name = input("What is your name?\n> ")
# print greeting string (contains prompt for age)
print(f"Hi, {name}. Welcome!  I will be your bartender this evening.")


# Num. Begin game
# call start() function to begin the game   
start()

