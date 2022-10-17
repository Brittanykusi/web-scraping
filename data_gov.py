# import packages
import pandas as pd
import requests
from bs4 import BeautifulSoup

# get page
page = requests.get('https://catalog.data.gov/dataset')
page # 200=success 

# create beautiful soup project
soup = BeautifulSoup(page.text,'html.parser')

# print in a pretty manner
print(soup.prettify())

# get the text using find or find_all || get titles of descriptions
titles = soup.find_all('h3', class_ = 'dataset-heading')

## creating a blank list that will house the values we pull
output_titles = []
for i in titles: # for x in y
    print (i.text)
    output_titles.append(i.text)

# show how many output lines in your dataset
len(output_titles)

# test dataset has values
output_titles[1]



# get the text using find or find_all || get descriptions
descriptions = soup.find_all('p', class_ = 'dataset-organization')

## creating a blank list that will house the values we pull
output_descriptions = []
for i in descriptions: # for x in y
    print (i.text)
    output_descriptions.append(i.text)
 
# show how many output lines in your dataset    
len(output_descriptions)

# # test dataset has values
output_descriptions[1]


list1 = output_titles 
list2 = output_descriptions

# create dictionary
dictionary = {'names': list1, 'description': list2}

#for each item in p_language print text
df = pd.DataFrame({'titles':output_titles,'descriptions':output_descriptions})

# convert df to csv
df.to_csv('./data/data_catalog.csv')