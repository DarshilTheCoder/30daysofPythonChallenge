# Things I learned is about modules and functions, go through three different ways of importing functions first one is directly import function_name second if exist in any another folder not in same where you writing code then folder_name.functions and last one if module exist somewhere else only, then use sys.path.append('path'). Go through different modules like math / calendar etc.

# 🎯 Challenge
# - Generate a random 8-character password

import string, random
def generate_password(password_length):
    character_choice = string.ascii_letters +string.digits +string.punctuation
    password=""
    for i in range(password_length):
        password += "".join( random.choice(character_choice))
    return password

number_of_unique_password = int(input('How many unique password you want = '))

for i in range(1,number_of_unique_password+1):
    user_input = int(input(f'Kindly enter the length of password {i} you want = '))
    password = generate_password(user_input)
    print(password)
    
