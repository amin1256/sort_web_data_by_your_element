import requests
from bs4 import BeautifulSoup
import re
import csv

x = requests.get('https://divar.ir/s/tehran')

soup = BeautifulSoup(x.text , "html.parser")

result = soup.find_all('div' , {"class":"kt-post-card__description"})

finall_result = re.sub('<.*?>' , '\n'  ,str(result))


print(finall_result)

