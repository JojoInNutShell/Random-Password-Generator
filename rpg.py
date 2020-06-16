"""
A Random Password Generator v1.1 by JojoInNutShell
You may use it for your personal purpose wether to learn how does a password generator works,to make a generate a password for your personal use
Everything related to personal use,you may also share it
This password generator is not a really advanced password generator :) but I hope you like it
I'm sorry if my way of writing this source code is bad
I will keep trying do my best to make this code better
I also apologize if there is a grammatical error in this source code wether in the variable naming or even this comments
"""

from random import randint #To shuffle number an make that number as index to get an character
uppercase_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #List of upper case alphabet letters
lowercase_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #List of lower case alphabet letters
symbols = ["!","@","#","$","%","^","&","*","(",")","?","<",">"] #List of symbols
number = ["1","2","3","4","5","6","7","8","9","0"] #List of numbers
all_char = uppercase_alphabets + lowercase_alphabets + symbols + number #Combining all characters to make a wholw list of characters and later to get a random index number of it (I thought,I was making every each list to make easier for adding features later on)
temp_char = "" #To save the random characters that have been picked from 
generated_pass = [] #A list for later joining all characters that have been chosen randomly
pass_length_now = 0 #A counter for the while loop in the make_the_password function
def how_long_is_da_pass(): #To check wether the password lengths that the use request is more than 6 characters
    global pass_length #To make this variable accessible by another function
    pass_length = input("How long you want your password to be?") #Prompts user to ask how long his/her password wants to be
    if pass_length != "": #To check wether user input something or not,I don't know how to make it 
        pass_length = int(pass_length)
        if pass_length < 6: #To check wether the password length that the user asks to is less than 6
            print("Na na na,gud password need to be more than 6 characters long")
            how_long_is_da_pass() #Asks user again to put a better password length
        elif pass_length >= 6: #To check wether the password length that the user asks to is more than 6
            make_the_password() #Generate the password if the password length that user asks to is valid length
    else:
        how_long_is_da_pass() #To asks the user again a valid password length

def make_the_password(): #Start generating password after a valid password length from the user request does exist
    global pass_length_now
    global generated_pass
    global all_char
    while pass_length != pass_length_now: #This keep turning to be true if pass_length_now has not reached the password length that the user wanted to
        temp_char = all_char[randint(0, 74)] #Make a random index number to take a random character from all_char list which contains all characters like upper lower case letters,numbers,and symbols
        generated_pass.append(temp_char) #To append the random character that has been chosen from the all_char list into an empty list which will be joined later by .join() function
        pass_length_now += 1 #Increment the pass_length_now to indicates how long has the generator generated the password
    generated_real_pass = "".join(generated_pass) #Joining all the random characters in the list
    print(f"The password that we have already generated for you is {generated_real_pass}") #To show to user the random generated password

how_long_is_da_pass() #Start prompting user for random password length
