import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.coincarp.com/currencies/solana/richlist/"

res = requests.get(url)

soup = BeautifulSoup(res.content, 'lxml')

table1 = soup.find('table', id='richlist-datatable')

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

df = df.iloc[:,0:4]
df.rename(columns = {'#':'Rank', 'Quantity':'Balance'}, inplace = True)

df_json = df.to_json(orient='records')

print(df_json)