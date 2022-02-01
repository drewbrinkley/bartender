# bartender.py

# import random module from Python library
import random


### create variables ###

# create global variable 'drink_count' for use in other functions
#global drink_count
# assign 0 to variable 'drink_count', which will track the number of consumed drinks
#drink_count = 0


### create lists ###

# create list of drink choices, with additional to include options for the different categories
drinks_list = ['beer', 'liquor', 'wine']
beer_type = ['lager', 'IPA', 'stout', 'pilsner', '$1 draft']
liquor_type = ['bourbon', 'scotch', 'tequila', 'vodka', 'gin']
wine_type = ['red', 'white', 'Merlot', 'Pinot Noir', 'Pinot Grigio', 'Riesling', 'Cabernet Sauvignon', 'Syrah', 'White Zinfandel', 'Chardonnay', 'Sauvignon Blanc']

# create empty list to hold drinks selected by user
drink_selections = []

# create list with initial entry of 0 to hold drinks selected by user
drink_count = [0]

# create empty list to hold failed attempts
attempts = []

### define functions ###

def age():
    """This function is called to prompt the user to enter his/her age via input().  
    Validate that the entry is a number, and if so convert it to integer, assign to a global variable, and return for use in other functions.
    Invalid entries are added to a list that maintains their running total.
    A while loop will terminate the game when the maximum invalid entries is reached.
    """
    print("age() has been called") ### Debugging prompt - delete in final code
    # assign 0 to variable 'i', which will track user's invalid inputs
    i = 0
    # while loop created to run code as long as max failed inputs has not been reached
    # while will continue to loop as long as the sum of values in list 'attempts' is less than 4
    while sum(attempts) < 4:    
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
            print(attempts[:])  ### debugging string
            print(sum(attempts)) ### debugging string
            return age_num #, fails
        # else-statement that will run when 'age_input' fails conversion to integer     
        else:
            # print string to prompt user to re-enter age
            print("You did not enter a valid age.  Please try again.")
            # assigns value of 1 to 'i' to record invalid input
            i = 1
            # updates list 'attempts' to add another value of 1
            attempts.append(i)
            print(i) ### debugging string - delete in final code

    # call function 'end()' to exit game based upon maximum failed inputs
    end(f"""You appear to be having problems communicating, which may mean you have had too much to drink.
I'm not able to serve you any more drinks now, {name}.""")
    

def have_drinks():
    """When called, this function will prompt the user to choose if and where to have drinks via input().  
    Validate that the entry is a number, and if so convert it to integer, assign to a global variable, and return for use in other functions.
    Invalid entries are added to a list that maintains their running total.
    A while loop will terminate the game when the maximum invalid entries is reached.
    """
    print("have_drinks() has been called") ### Debugging prompt - delete in final code
    # assign 0 to variable 'i', which will track user's invalid inputs
    i = 0

    # while loop created to run code as long as max failed inputs has not been reached
    # while will continue to loop as long as the sum of values in list 'attempts' is less than 4
    while sum(attempts) < 4:   
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
            print("# failed attempts")  ### debugging
            print(sum(attempts))  ### debugging
            return choice
        # else will run when user input was invalid (not a number or not in range)    
        else:
            # print string to prompt user to re-enter selection
            print("You did not enter a valid selection.  Please try again.")
            # assigns value of 1 to 'i' to record invalid input
            i = 1
            # updates list 'attempts' to add another value of 1
            attempts.append(i)
    
    # call function 'end()' to exit game based upon maximum failed inputs
    end(f"""You appear to be having problems communicating, which may mean you have had too much to drink.
I'm not able to serve you any more drinks now, {name}.""")


def home():
    """This function executes when the user chooses to have drinks at home.  Via input(), the user will make a choice to decide if and where to have a drink.
    Validate that the entry is a number, and if so convert it to integer and call the next function associated with that choice.
    Invalid entries are added to a list that maintains their running total.
    Updates a list to maintain the number of drinks consumed if the user decides to have a drink.
    A while loop will terminate the game when the maximum invalid entries is reached.
    """
    print("home() has been called") ### Debugging prompt - delete in final code
    # assign 0 to variable 'i', which will track user's invalid inputs
    i = 0
    # assign 0 to variable 'd', which will track the number of drinks consumed
    d = 0

    # while loop created to run code as long as max failed inputs has not been reached
    # while will continue to loop as long as the sum of values in list 'attempts' is less than 4
    while sum(attempts) < 4:   
        # assign user input to variable 'choice_input'
        choice_input = input(f"""Type one of the following numbers to tell me what you would like to do:
            1 - Have a drink
            2 - Go to a bar for some drinks
            3 - Call it a night
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
            # convert 'choice_input' to integer and assign to 'decision'
            decision = int(choice_input)
            print(f"---{decision}") #### debugging print - delete in final code
            print("# failed attempts")  ### debugging
            print(sum(attempts))  ### debugging
            
            # if statement to call next function based upon user's selection
            # this code chunk will run if user selected 1
            if decision == 1:
                print("start of if---")
                print(drink_count)
                # print string
                print("You have elected to have a drink.")
                # call 'order()' function to take drink order
                order()
                # print string prompting user to make another selection
                print("had a drink, what now?")
                # assigns value of 1 to 'd' to record invalid input
                d = 1
                # updates list 'drink_count' to add another value of 1
                drink_count.append(d)
                print(drink_count)
            # this code chunk will run if user selected 2
            elif decision == 2:
                # call 'leave_home()' function
                leave_home()
            # this code chunk will run if user selected 3
            else:
                # call 'hangover()' function
                hangover()
            
        # else will run when user input was invalid (not a number or not in range)    
        else:
            # print string to prompt user to re-enter selection
            print("You did not enter a valid selection.  Please try again.")
            # assigns value of 1 to 'i' to record invalid input
            i = 1
            # updates list 'attempts' to add another value of 1
            attempts.append(i)
    
    # call function 'end()' to exit game based upon maximum failed inputs
    end(f"""You appear to be having problems communicating, which may mean you have had too much to drink.
I'm not able to serve you any more drinks now, {name}.""")


def bar():
    """This function executes when the user chooses to have drinks at a bar.  Via input(), the user will make a choice to decide to have a drink or not.
    Validate that the entry is a number, and if so convert it to integer and call the next function associated with that choice.
    Invalid entries are added to a list that maintains their running total.
    Updates a list to maintain the number of drinks consumed if the user decides to have a drink.
    A while loop will terminate the game when the maximum invalid entries is reached.
    """
    print("Welcome to the Snake Pit bar!") ### Debugging prompt - delete in final code
    # assign 0 to variable 'i', which will track user's invalid inputs
    i = 0
    # assign 0 to variable 'd', which will track user's drink consumption at the bar
    d = 0

    # while loop created to run code as long as max failed inputs has not been reached
    # while will continue to loop as long as the sum of values in list 'attempts' is less than 4
    while sum(attempts) < 4:   
        # assign user input to variable 'choice_input'
        choice_input = input(f"""Type one of the following numbers to tell me what you would like to do:
            1 - Have a drink
            2 - Close tab and go home
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
        if it_is == True and (0 < int(choice_input) < 3):
            # ----- print string to debug - delete in final code
            print("pass.")
            # convert 'choice_input' to integer and assign to 'decision'
            decision = int(choice_input)
            print(f"---{decision}") #### debugging print - delete in final code
            print("# failed attempts")  ### debugging
            print(sum(attempts))  ### debugging
            
            # if statement to call next function based upon user's selection
            # this code chunk will run if user selected 1
            if decision == 1:
                print("drinks at start of bar") #### debugging - delete in final
                print(drink_count)
                # print string
                print("You have elected to have a drink.")
                # call 'order()' function to take drink order
                order()
                # print string prompting user to make another selection
                print("had a drink, what now?")
                # assigns value of 1 to 'd' to record invalid input
                d = 1
                # updates list 'drink_count' to add another value of 1
                drink_count.append(d)
                print(drink_count)
            # this code chunk will run if user selected 2
            else:
                # call 'leave()' function
                leave_bar()
            
        # else will run when user input was invalid (not a number or not in range)    
        else:
            # print string to prompt user to re-enter selection
            print("You did not enter a valid selection.  Please try again.")
            # assigns value of 1 to 'i' to record invalid input
            i = 1
            # updates list 'attempts' to add another value of 1
            attempts.append(i)
    
    # call function 'end()' to exit game based upon maximum failed inputs
    end(f"""You appear to be having problems communicating, which may mean you have had too much to drink.
I'm not able to serve you any more drinks now, {name}.""")


def order():
    """This function executes when the user chooses to have a drinks.  Via input(), the user will make a choice to place a drink order.
    Validate that the entry is on the drink list, and if so add it to the list that maintains drink selections.
    Invalid entries are added to a list that maintains their running total.
    A while loop will terminate the game when the maximum invalid entries is reached.
    """
    print("order() has been called") ### Debugging prompt - delete in final code
    # assign 0 to variable 'i', which will track user's invalid inputs
    i = 0

    # while loop created to run code as long as max failed inputs has not been reached
    # while will continue to loop as long as the sum of values in list 'attempts' is less than 4
    while sum(attempts) < 4:   
        # print string
        print("Here's what your drink choices are:")
        # print values in list 'drinks_list[]' to provide menu of choices to user
        print(drinks_list)
        # assigns user input() for selection to variable 'drink_order'
        drink_order = input("What kind of drink would you like?\n> ")
            
        print(f">>> {drink_order}")  ### Debugging prompt - delete in final code
        
        # if-statement to confirm validity of user input for 'drink_order'
        # code for if will run when user's input matched a value in list 'drinks_list[]'
        if drink_order in drinks_list:
            # ----- print string to debug - delete in final code
            print("pass.")
            # add drink order to list 'drink_selections[]'
            drink_selections.append(drink_order)
            print(drink_selections) #### debugging prompt
            # return value of 'drink_order'
            return drink_order 
        # else will run when user input was invalid (did not match options in 'drinks_list[]')    
        else:
            # print string to prompt user to re-enter selection
            print("I did not recognize your order.  Please try again.")
            # assigns value of 1 to 'i' to record invalid input
            i = 1
            # updates list 'attempts' to add another value of 1
            attempts.append(i)
    
    # call function 'end()' to exit game based upon maximum failed inputs
    end(f"""You appear to be having problems communicating, which may mean you have had too much to drink.
I'm not able to serve you any more drinks now, {name}.""")


def random_outcome():
    """When this function is called, it will generate and return a global variable 'outcome' that can be used in other functions. 
    Validate that the entry is a number, and if so convert it to integer and call the next function associated with that choice.
    The variable is based upon the number of drinks the user has consumed, as recorded in the list drink_count[].
    If the user has had 0 drinks, then 'outcome' is assigned a value of 1.
    Otherwise, 'outcome' is assigned a random value that falls between 1 and the total number of drinks consumed, inclusively.
    The maximum possible value of 'outcome' increases proportional to the number of drinks consumed.
    """
    # assign sum of values in list drink_count[] to variable 'max'
    max = sum(drink_count)
    print(max)  ### debugging print - delete in final code
    # define global variable 'outcome' for use in other functions
    global outcome
    #if-statement runs to assign outcome value of 1 if user has not consumed any drinks yet
    if max == 0:
        outcome = 1
    # else-statement assigns random number between and value of variable 'max' to variable 'outcome'
    else:
        outcome = random.randint(1, max)
    print(outcome)  ### debugging print - delete in final code
    # return value of variable 'outcome'
    return outcome


def leave_bar():
    """This function executes when the user chooses to leave the bar.  
    The function calls upon random_outcome() to generate a value for variable 'outcome' to be multiplied by to total number of drinks consumed.
    The next function called is based upon where the result of that calculation falls into the if-else if-else statement.
    There is also contains a trap to catch minors driving after they consumed alcohol.
    """
    # call random_outcome() function
    random_outcome()
    # if-statement that will trigger the next function to be called
    # if executes when the user is a minor and has consumed alcohol
    if age_num < 21 and sum(drink_count) > 0:
        end("""BUSTED!!! You got pulled over and the officer noticed you had alcohol on your breath.  
You have been arrested for an Underage DUI offense and for possessing a fake ID.""")
    # else-if executes when product of 'outcome' and sum of drink_count is less than 6
    elif sum(drink_count) * outcome < 6:
        print("You have made it to your destination")
        # call 'hangover()' function
        hangover()
    # else-if executes when product of 'outcome' and sum of drink_count is less than 20
    elif sum(drink_count) * outcome < 20:
        # call cops() function
        cops()
        # call hangover() function, unless game is ended by the result of cops()
        hangover()
    # else executes when none of the above statements are True
    else:
        # call end() function to end game
        end("You have been in a horrible car crash and have been transported to the hospital.\nDon't drink and drive!")


def leave_home():
    """This function executes when the user chooses to leave home to go to a bar.  
    The function calls upon random_outcome() to generate a value for variable 'outcome' to be multiplied by to total number of drinks consumed.
    The next function called is based upon where the result of that calculation falls into the if-else if-else statement.
    There is also contains a trap to catch minors driving after they consumed alcohol.
    """
    # call random_outcome() function
    random_outcome()
    # if-statement that will trigger the next function to be called
    # if executes when the user is a minor and has consumed alcohol
    if age_num < 21 and sum(drink_count) > 0:
        end("""BUSTED!!! You got pulled over and the officer noticed you had alcohol on your breath.  
You have been arrested for an Underage DUI offense.""")
    # else-if executes when product of 'outcome' and sum of drink_count is less than 6
    elif sum(drink_count) * outcome < 6:
        # print string
        print("You have made it to your destination")
        # call bar() function
        bar()
    # else-if executes when product of 'outcome' and sum of drink_drink count is less than 20
    elif sum(drink_count) * outcome < 20:
        # call cops() function
        cops()
        # call bar() function, if game is not ended by result of cops()
        bar()
    # else executes when none of the above statements are True
    else:
        # call end() function to end game
        end("You have been in a horrible car crash and have been transported to the hospital.\nDon't drink and drive!")


def cops():
    """This function executes when the user chooses an option that will cause him/her to drive.  
    The function calls upon random_outcome() to generate a value for variable 'outcome' to be multiplied by to total number of drinks consumed.
    The next function called is based upon where the result of that calculation falls into the if-else if-else statement.
    There is also a choice the user must make via input() to decide what to do if they are being pulled over by the police.
    """
    # create list named 'options' with 2 possible values
    options = ['flee', 'pull over']
    # print string
    print("A police officer has just turned onto the road and is following you.")
    # call random_outcome() function
    random_outcome()
    # if-statement to determine whether the user will be pulled over by the police
    # if executes when product of 'outcome' and sum of drink_count is less than 10; user will not be pulled over and game continues
    if sum(drink_count) * outcome < 10:
        # print string
        print("The officer turns on his blue lights, but then does a U-turn to chase a speeder going in the other direction.\nWhew, that way close!")
    # else executes when if is False; user is pulled over
    else:
        # print string
        print("You see blue lights behind you.  Looks like you are being pulled over.  What do you do?")
        # print values in list 'options'
        print(options)
        # assigns user input() to variable 'reaction'
        reaction = input("> ")
        # if-statement to validate user's input
        # if executes if user input 'flee'
        if reaction == 'flee':
            # call random_outcome() function
            random_outcome()
            # if-statement to determine result of police encounter
            # if executes when product of 'outcome' and sum of drink_count is less than 8; user will get away and game continues
            if sum(drink_count) * outcome < 8:
                print("Against all odds, you somehow evade the officer.  Still, this was probably not a smart decision")
            # else executes when if is False
            else:
                # call end() function to end game
                end("""You get caught and now face charges for DUI, reckless driving, evading and fleeing, and speeding.
Best case, you can expect to spend a couple thousand dollars in attorney fees.
More realistically, you are going to lose your driver's license, have to do classes, will be required to have an
interlock device in your vehicle, and be at the mercy of the court regarding jail time and fines.
You will be paying for this decision, literally and figuratively, for several years.""")
        # else-if executes when user input 'pull over'
        elif reaction == 'pull over':
            # call random_outcome() function
            random_outcome()
            # if-statement to determine outcome of encounter
            # if executes when product of 'outcome' and sum of drink_count is less than 8; user will not be arrested and game continues
            if sum(drink_count) * outcome < 8:
                # print string
                print("The officer received an emergency call while on scene and lets you got with a warning to slow down.")
            # else executes when if is False
            else:
                # call end() function to end game
                end("""You get arrested for DUI.  
Look forward to a suspension of your driver's license, alcohol classes, and having to install an interlock device in your vehicle.
Drinking and driving is a serious offense.  At least no one got hurt this time.""")
        # else excecutes when user did not enter a valid input
        else:
            # print string
            print("That was not a valid response.")
            # call end() function to end game
            end("""You panic when you see the blue lights, knowing you have alcohol in your system.
In your moment of indecision, you drift out of your lane and strike another vehicle.
Fortunately, no one is injured.  However, this is going to create some serious legal and financial issues for you.
Drinking and driving is a serious offense.""")


def hangover():
    """This function executes when the user's choices have led to the end of the game and the game has not otherwise ended as the result of another function.
    The function calls upon random_outcome() to generate a value for variable 'outcome' to be multiplied by to total number of drinks consumed.
    The next function called is based upon where the result of that calculation falls into the if-else if-else statement.
    There are also different outcomes for users who are minors vs those who are 21 or over.
    """
    # call random_outcome() function
    random_outcome()
    if sum(drink_count) * outcome <= 1:
        end("You have made a healthy choice.\nThe latest research suggests even a moderate consumption of alcohol confers some health risk.")
    elif sum(drink_count) * outcome < 8 and age_num < 21:
        end("You are too young to legally drink alcohol, but you managed to get away with it this time.")
    elif sum(drink_count) * outcome < 8:
        end("If you are going to enjoy alcohol, please continue to do so responsbily.")
    elif sum(drink_count) * outcome < 16 and age_num < 21:
        end(f"Uh oh, {name}.\nYou wake up the next day with a hangover, and your parents grounded you for drinking.\nPerhaps you should wait until you're 21.")
    elif sum(drink_count) * outcome < 16:
        end("This round of drinking did not agree with you.\nYou wake up the next day with a hangover.\nPerhaps you should scale it back next time.")
    elif age_num < 21:
        end(f"""Whoa - you really overdid it, {name}!
You passed out after your evening of drinking and forgot to set your alarm.
You then overslept and missed a midterm exam.
Maybe you should think about the consequences of your actions next time...""")
    else:
        end(f"""Whoa - you really overdid it, {name}!
You passed out after your evening of drinking and forgot to set your alarm.
You then overslept and missed an important presentation at work and will likely face disciplinary action.
Please try to enjoy your alcohol more responsibly next time.""")


def end(why):
    """The game will end when this function executes.
    This function may be called when the result of the user's choice(s) led to the end of the game, or when the user exceeds the max allowable invalid inputs.  
    The function takes variable 'why' as an argument and will print 'why' when called.
    The function uses the built-in function exit() to end the script.
    """
    # prints variable 'why' when function is called
    print(why)
    # exits program, without error message
    exit(0)


def start():
    """This function can be considered the "main" function for this script.  
    It executes when the game begins and will trigger other functions based upon the user's initial input. 
    The function contains an if-else if-else statement to end the game when users input an age that does not meet a minimum value. 
    """
    print("start has been called") ### Debugging prompt - delete in final code
        
    # call 'age()' function to prompt for user's age
    age () 
    
    print(f">from age>>>> {attempts[:]}")  ### debugging print
    # the following code block will execute based upon value return of 'age()' function
    # if-statement runs when user entered age of 0 or less
    if age_num <= 0:
        # print string when user's age is less than or equal to 0
        end(f"I'm sorry, {name}. It's hard to play a game when you haven't even been born yet!")
    # else-if-statement runs when user's age is greater than 0 and less than 15
    elif age_num > 0 and age_num < 15:
        end(f"I'm sorrry, {name}.  You are a little young to be drinking.  Try again when you're older...")
    # else-statement runs when user's age is 15 or greater
    else:
        # print string 
        print("next step...")  ### debugging prompt - delete in final code
        # call function 'have_drinks()' to prompt for user's first choice
        have_drinks()

        # the following code block will execture based upon value returned from 'have_drinks()' function
        # if-statement runs when user selected option 1
        if choice == 1:
            # call 'home()' function
            home()
        # else-if statement runs when user selected option 2
        elif choice == 2:
            # call 'bar()' function
            bar()
        # else-statement runs when user selected option 3
        else:
            # call hangover() function
            hangover()
        
        

    print("<<<< exit start()")  ### Debugging prompt - delete in final code


### ----- Game's main code block ------ ###

# 1. Greeting
# assign user input to variable 'name'
name = input("What is your name?\n> ")
# print greeting string (contains prompt for age)
print(f"Hi, {name}. Welcome!  I will be your bartender this evening.")


# Num. Begin game
# call start() function to begin the game   
start()

