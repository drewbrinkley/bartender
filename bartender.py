# bartender.py

# import random module from Python library
import random

# define function 'age()' to collect and validate user's age
def age():
    print("age() has been called") ### Debugging prompt - delete in final code
    # assign user input to variable 'age_input'
    age_input = input("Please enter your age, in years:\n> ")
    
    print(f">>> {age_input}")  ### Debugging prompt - delete in final code
    
    # use try...except block to vailidate that user input is a number
    try:
        # tests to see if the 'age_input' value can be converted to an integer
        int(age_input) 
        # assigns True to variable 'it_is' if conversion is successful
        it_is = True
    except ValueError:
        # assigns False to variable 'it_is' if conversion returns an error (user did not enter a number)
        it_is = False

    print(it_is)  ### debugging prompt - delete in final code
    
    # if-statement to confirm validity of user input for 'age_input'
    # if executes associated code block when 'age_input' succesfully converted to integer
    if it_is == True:
        # print string to confirm user entered a number when prompted
        print("Thank you for entering your age.")
        # create global variable 'age_num' for use in other functions
        global age_num
        # convert 'age_value' to integer and assign to 'age_num'
        age_num = int(age_input)
        print(f"---{age_num}")  ### debugging statement - deleted in final code
        # return value of 'age_num' for use elsewhere
        return age_num
    # else-statement that will run when 'age_input' fails conversion to integer     
    else:
        # print string to prompt user to re-enter age
        print("You did not enter a valid age.  Please try again.")
        # call age() function again to loop user back to 'age' input()
        age()


# define function 'have_drinks()' to get user input on initial drink decision
def have_drinks():
    print("have_drinks() has been called") ### Debugging prompt - delete in final code
    # assign user input to variable 'choice_input'
    choice_input = input(f"""Type one of the following numbers to tell me what you would like to do:
        1 - Stay home and have some drinks
        2 - Go to a bar for some drinks
        3 - I don't feel like drinking today
        > """)
        
    print(f">>> {choice_input}")  ### Debugging prompt - delete in final code
    
    # use try...except block to vailidate user input
    try:
        # tests to see if the 'choice_input' value can be converted to an integer
        int(choice_input)
        # assigns True to variable 'it_is' if conversion is successful
        it_is = True
    except ValueError:
        # assigns False to variable 'it_is' if conversion returns an error (user did not enter a number)
        it_is = False

    print(it_is)  ### debugging prompt - delete in final code
    
    # if-statement to confirm validity of user input for 'choice_input'
    # code for if will run when user input a 1, 2, or 3
    if it_is == True and (0 < int(choice_input) < 4):
        # ----- print string to debug - delete in final code
        print("pass.")
        # create global variable 'choice' for use in other functions
        global choice 
        # convert 'choice_input' to integer and assign to 'choice'
        choice = int(choice_input)
        print(f"---{choice}") #### debugging print - delete in final code
        # return value for 'choice' to use elsewhere
        return choice
    # else will run when user input was invalid (not a number or not in range)    
    else:
        # print string to prompt user to re-enter selection
        print("You did not enter a valid selection.  Please try again.")
        # call have_drinks() function again to loop user back to try again
        have_drinks()
    
    print("exit have_drinks()")


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
        have_drinks()

        if choice == 1:
            print("call home()")
        elif choice == 2:
            print("call bar()")
        else:
            print("call hangover()")
        
        

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

