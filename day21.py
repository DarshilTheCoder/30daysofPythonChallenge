#Today I am learning web scraping one of the amazing topic I consider. Here I learned how to grab any tag or something from website or a real website using get method, as well as store that thing into my text file.
from bs4 import BeautifulSoup
import requests

class FileHandler:
    def __init__(self,file_name,mode) -> None:
        self.file = file_name
        self.mode = mode
    
    def  __enter__(self):
        return open(self.file,self.mode)

    def __exit__(self,exc_type, exc_value, traceback):
        print(f"{self.file} is Closed!")

html_text = requests.get('https://www.nytimes.com/section/technology').text
soup =  BeautifulSoup(html_text,'lxml')
news_headlines = soup.find_all('a',class_='css-1u3p7j1')
print('The headlines of New York Times are: ')
news_list = []
for news in news_headlines:
    news_list.append(news.text)
    print(news.text)

with FileHandler('news_list.txt','a') as f:
    i=0
    for news in news_list:
        i+=1
        f.write(f"{i})  {news} \n")

        

# with FileHandler(file_name='index.html',mode='r') as f:
#     content = f.read()
    
#     soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)
    # course_cards = soup.find_all('div',class_='card')
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price = course.a.text.split()[-1]
    #     print(F"{course_name} starts at price {course_price}")