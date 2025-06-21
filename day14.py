
#Challenge of the day is to find a factorial of any number using recursive method. 

def factorial(n):
    if n ==1 :
        return 1
    return n*factorial(n-1)

user_input = int(input('Kindly enter the number of whose you want to find factorial = '))
answer = factorial(user_input)
print(answer)