from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {
    "User-Agent": "WikiDataProject/1.0 (contact: your_email@example.com)"
}

page = requests.get(url, headers=headers)
time.sleep(1)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[0]

world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns=world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

print(df)

df.to_csv('Companies.csv', index=False)
print("Saved to Companies.csv")