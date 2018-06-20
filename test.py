# -*- coding: utf-8 -*-
#import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#specify url
quote_page = ["https://www.bloomberg.com/quote/SPX:IND","http://www.bloomberg.com/quote/CCMP:IND"]


#for loop to traverse array
data = []

for pg in quote_page:
# query the website and return the html to the variable page
    page = urllib2.urlopen(pg)

# parse the html using beautiful soap and store in variable soup
    soup = BeautifulSoup(page,'html.parser')

#<h1 class="name"> is unique on the page
    name_box = soup.find('h1',attrs = {'class':'name'})

#After we have the tag, we can get the data by getting its text.
    name = name_box.text.strip()  # strip() is used to remove starting and trailing
#print name

#<div class="price">2,500.23</div>
    price_box = soup.find('div',attrs = {'class':'price'})
    price = price_box.text.strip()
#print price
#save data in tuple
    data.append((name,price))

# open a csv file with append, so old data will not be erased
with open('index.csv','a') as csv_file:
 writer = csv.writer(csv_file)
 # The for loop
 for name,price in data:
  writer.writerow([name,price, datetime.now()])

print soup.title
print soup.title.name
print soup.title.string
print soup.h1.div['class']
