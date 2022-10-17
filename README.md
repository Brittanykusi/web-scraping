# web-scraping

##Initial steps
#### Import Packages
- https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L2-L4
#### Get website
- https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L7-L8
#### Create beautiful soup project
- https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L11
## Pull tags and create table
#### Inpect page
- right click + inspect
- you will scroll through the page's code and inspect to find which information you would like to extract
## Pull html tag and code 
- https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L11 | this is one example. 
- you will use the find_all command from beautiful soup and call on the tag and class of the information you would like to scrape
## Create list
- create an empty list | https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L20
- fill and append list |  https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L21-L23
## Convert list to csv file
- create lists | https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L49-L50
- create dictionary | https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L53
- call df | https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L56
- convert to csv | https://github.com/Brittanykusi/web-scraping/blob/341a82e1af40f7cd4b4090650fe8d386f7875ef6/data_gov.py#L59

