#Today on day 11, I am resuming my journey again for 30dayofPythonChallenge. I am learning date,time module, which is very userful from a data science perspective, because to take out the insight of perticular day or month or year of any product or country at that time such modules are very usefull. 

from datetime import date, datetime, time

today_date = date.today()
#Here one more important concept I learned is about attributes and methods. I know that method is a function and they perform some kind of actions, whereas attribute is something like a variable, which store the value automatically whenever an instance of class is defined.
print(today_date)
print(today_date.day)
print(today_date.month)
print(today_date.year)

#Another usefull method is to use strftime(), here everything is passed as a string so we can make changes into a statement of printing line to make grammartically correct.
print(today_date.strftime('%A, %dth of %m %Y')) #like here how I added th then comma and all. 

next_year_date = today_date.replace(year=today_date.year+1)
print(next_year_date)
#like this it will be helpfull to take the difference in date which is another usefull concept in data science or analytics
difference_date = abs(next_year_date-today_date)
print(difference_date)

#datetime object, return date and time both
now = datetime.now()
print(now)
print("today's date is {}".format(now.day)) #this one more way to print the statement in a proper way using .format()
print("today's day is {}".format(now.strftime('%A')))

my_time = time(11,13,44)
another_my_time = time.fromisoformat('11:13:14')
print(my_time)
print(another_my_time)


#Challenge is to calculate the days between two dates.
date_1 = date(2025, 6, 15)
birthday_date = date(2026,4,11)
number_of_days_remaining = abs(date_1-birthday_date)
print('This below statement is related to challenge')
print("{} this many days are yet remaining".format(number_of_days_remaining))