import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

count = 0
url_link = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001277151&owner=exclude&count=40&hidefilings=0"
data = []
page = urllib2.urlopen(url_link)
soup = BeautifulSoup(page,'html.parser')
for tr in soup.find_all("tr",{"class": ["None", "blueRow"]}):
    tag = tr.findAll('td')
    #for td in tr.find_all("td",text="8-K"):
        #count = count + 1
        #l = count
        #data.append(l)
        #for link in td.find_all('a',href=True):
        #l = link['href']
        #data.append(l)

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for l in data:
        writer.writerow([l])
#writer.writerow([l, datetime.now()])
