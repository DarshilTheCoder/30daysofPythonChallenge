#Today I learn about how to open a file first using .open() then understand different modes of open method like 'r', 'w','a', 'rb','wb'. I understand how to read a file using .read(), also one read multiple lines using readlines() in which you limit till which line you want data. I understand about .write(), that helps to write something inside file and understand with 'a' append mode we cannot lost the previous written data. 

# read_file = open('day7.txt','r')
# read_file = open('day7.txt','a')
# for data in read_file:
#     print(data)
# print(read_file.readlines()) # this function readlines() return a list of lines and to run this function your file needs to open in 'r' mode only
# read_file.write('\nwritten from code')  #to run write function file need to open in 'w' or 'a' mode. 

import re
word_counter = {}

with open('day7.txt') as read_file:
    text = read_file.read().lower()
    word_list = re.findall(r'\b\w+\b',text)
    for word in word_list:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word]+=1

for key,value in word_counter.items():
    print(f'{key} : {value}')
            
        