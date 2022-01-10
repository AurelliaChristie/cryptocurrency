import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://avascan.info/stats/richlist"

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }

res = se.get(url)

soup = BeautifulSoup(res.content, 'lxml')

table1 = soup.find('table')

headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)

df = pd.DataFrame(columns = headers)

for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(df)
 df.loc[length] = row

df = df.replace(r'\s+|\\n', ' ', regex=True) 

df.columns = ['Rank', 'Chain','Address', 'Balance','MUSD', 'Percentage']

df = df[['Rank', 'Chain','Address', 'Balance', 'Percentage']]

df_json = df.to_json(orient='records')

print(df_json)