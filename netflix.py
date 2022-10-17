# import packages
import pandas as pd
import requests
from bs4 import BeautifulSoup

# get page
page = requests.get('https://top10.netflix.com/tv')
page # 200=success 

# create beautiful soup project
soup = BeautifulSoup(page.text,'html.parser')

# print in a pretty manner
print(soup.prettify())

# get titles of descriptions
top = soup.find_all('tr')


## creating a blank list that will house the values we pull
output_top = []
for i in top : # for x in y
    print (i.text)
    output_top.append(i.text)

len(output_top)
# test
output_top[10]


list1 = output_top 

# create dictionary
dictionary = {'neflix_top_ten': list1}

#for each item in p_language print text
df = pd.DataFrame(list1)

# convert df to csv
df.to_csv('./data/dnetflix.csv')