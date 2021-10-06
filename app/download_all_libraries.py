import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

res =  requests.get('https://pypi.org/simple/')

if res.status_code == 200:
    soup = bs(res.text,'html.parser')

    (pd.DataFrame(soup.find_all('a'), columns=['libraries'])).to_csv('libraries.csv', index=False)
else:
    print("Erro no download das libraries")
