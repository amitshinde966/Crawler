import requests
import lxml
from bs4 import BeautifulSoup
from requests.api import head

url = "https://www.google.com/search?q=gate+cse+syllabus&oq=gate+cse+syllabus&aqs=chrome..69i57j0i512l9.4646j0j7&sourceid=chrome&ie=UTF-8"

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
#}

f = requests.get(url)

soup = BeautifulSoup(f.content, 'lxml')

links = soup.find_all('a')

for link in links:
    print(link["href"])
    if(link["href"].startswith("/url?")):
        print("go inside this url here: ")

num = 1