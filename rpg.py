from random import *
uppercase_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!","@","#","$","%","^","&","*","(",")","?","<",">"]
number = ["1","2","3","4","5","6","7","8","9","0"]
all_char = uppercase_alphabets + lowercase_alphabets + symbols + number
temp_char = ""
generated_pass = []
pass_length_now = 0
def how_long_is_da_pass():
    global pass_length
    pass_length = int(input("How long you want you password to be?"))
def make_the_password(length):
    global pass_length_now
    global generated_pass
    global all_char
    while length != pass_length_now:
        temp_char = all_char[randint(0, 77)]
        generated_pass.append(temp_char)
        pass_length_now += 1
    generated_real_pass = "".join(generated_pass)
    print(f"The password the that we have already generated for you is {generated_real_pass}")
how_long_is_da_pass()
if pass_length < 6:
    print("Na na na,gud password need to be more than 6 characters long")
    how_long_is_da_pass()
else:
    make_the_password(pass_length)