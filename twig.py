#! usr/bin/env python3
#counts the instances 'nodded' in Twig 1.1

import requests
from bs4 import BeautifulSoup
#from selenium import webdriver


url = 'https://twigserial.wordpress.com/2014/12/24/taking-root-1-1/'
body = requests.get(url)
soup = BeautifulSoup(body.text, "lxml")

count = 0
divtag = soup.find('div', {'class': 'entry-content'})#do i need div class=...
for p in divtag:
    for element in p: #gives you the stuff inside the <p></p>
        if 'nodded' in element:
            count += 1
print (count)

#browse = webdriver.Firefox()

