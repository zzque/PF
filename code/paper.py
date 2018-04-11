import requests
from bs4 import BeautifulSoup
result = requests.get("http://swb.socionet.ru/dtypes/russian/paper.xml")
c = result.content
soup = BeautifulSoup(c,'html.parser')
samples = soup.find_all('title', limit=1)
print(samples)
