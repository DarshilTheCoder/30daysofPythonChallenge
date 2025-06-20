#Today's topic covered is mainly about function, there go through about block of code / positional arguments and named arguments / bydefault value of argument if parameter is not passed into the function / documentation strings is a multi line which tells what function is doing. 

#Today's  🎯 Challenge
#- Write a function that computes the sum and average of a list of numbers


user_list = []

def sum(num_list,user_choice=sum):
    total = 0
    i=0
    for num in num_list:
        i=i+1
        total=total+num
    if user_choice.lower()=='sum':
        return total
    elif user_choice.lower()=='avg' or user_choice.lower() == 'average':
        return total/i
    else:
        print('enter proper user choice')
        exit()

user_input = int(input('Enter how many number do you want to do? = '))
for i in range(1,user_input+1):
    number_input = int(input(f'enter the nubmer {i} here = '))
    user_list.append(number_input)
user_choice = input('What calculation you want to perform sum or avg? \n Write it here = ')

user_input_list_total = sum(user_list,user_choice)
if user_input_list_total !=None:
    print(f'{user_choice} of list {user_list} is  = {user_input_list_total}')



