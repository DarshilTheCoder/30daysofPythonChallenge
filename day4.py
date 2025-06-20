# prime_numbers = [2,3,5,7]

user_input = int(input('Enter the number of your choice, system will tell whether it the given number is prime or not. \n Kindly enter your number here = '))

i=2
is_prime = True

# while i<user_input:
#     print(i)
#     if user_input%i==0:
#         is_prime=False
#         break
#     i=i+1

for i in range(2,user_input):
    # print(i)
    if user_input%i==0:
        is_prime=False
        break
    

if is_prime is True:
    print('number is prime')
else:
    print('number is not prime')

