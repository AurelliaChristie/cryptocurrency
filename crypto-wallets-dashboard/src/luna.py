import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://lunarichlist.com/"

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }

res = se.get(url)

soup = BeautifulSoup(res.content, 'lxml')

table1 = soup.find('table', id ='richlist')

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

#Split the string on blank characters
List = soup.find('div').text.replace('\n',"").split()

#for each element in the list, if it starts with 'm' then print it
for s in List:
    if s.startswith('Supply'):
        a = s

b = ','.join(re.findall("\d+", a))

#Add percentage amount
df["Total Balance"]= df["Total Balance"].replace(',', '',regex=True)
df["Total Balance"] = pd.to_numeric(df["Total Balance"]) 

df["Supply Amount"] = b
df["Supply Amount"] = df["Supply Amount"].replace(',', '',regex=True)
df["Supply Amount"] = pd.to_numeric(df["Supply Amount"])

df["Percentage"] = round(df["Total Balance"]/df["Supply Amount"]*100,4)

df = df[['Rank', 'Account', 'Total Balance', 'Percentage']]
df.columns = ['Rank', 'Address', 'Balance', 'Percentage']

df_json = df.to_json(orient='records')

print(df_json)