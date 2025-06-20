#Today I learned another important concept which is very useful in data analytics or in data science, that is regex which is used to find the pattern in the text or to validate something like gmail or phone number etc. I learned that how re.findall() method used to find the all given pattern, for defining the pattern first it is better to use regex101.com, from where we can make the perfect regex. 

#Today's Challenge is to validate the email

import re
pattern = '[a-zA-Z]+\d+@gmail\.[com|edu|net]+|[a-zA-Z]+\d+@hotmail\.[com|edu|net]+|[a-zA-Z]+\d+@yahoo\.[com|edu|net]+'
user_input = input('Enter the email to validate - ')
if(re.findall(pattern=pattern,string=user_input)):
    print('Perfect email')
else:
    print('Not a perfect email')