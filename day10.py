#Today's Learning is all about excepting handling, where I learned about try except catch block and learn how one handle the exception carefully and will not stop the code from its execution

#In Today's challenge I revised some of the previous topics like taking user_input , then creating a dictionary and printing a dictionary, opening a file for read and to write it. Also use try except block to handle the error and created a dictionary
import os


try:
    with open('day10.txt',mode='r') as file:
        word_dict = {}
        for word in file:
            word.strip() #this strip method uses to remove the trailing and leading whitespaces
            try:
                checking_number = float(word)
                print(f"{word.strip()} is a number")
                if checking_number is not None:
                    word_dict[word.strip()] = 'number'
            except ValueError:
                print(f"{word.strip()} is not a number")
                word_dict[word.strip()] = 'not a number'
        user_input = input('Want to see the dictionary ? write yes = ')
        if user_input.lower() == 'yes':
            for key in word_dict:
                print(f"{key}:{word_dict[key]}")
except FileNotFoundError as e:
    print(f"File Not Found. So I created a file for you. Kindly add the data for checking a number or not a number")
    open('day10.txt',mode='w')

with open('day10.txt',mode='a') as file:
    user_input = input('What do yo want to add in the file? Kindly write it here = ')
    if os.stat('day10.txt').st_size == 0:
        file.write(user_input)
    else:
        file.write("\n" + user_input)

