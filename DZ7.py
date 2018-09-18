
# coding: utf-8

# In[80]:


import json
from pprint import pprint
from collections import Counter

x = []
rez = []

def sortByLength(inputStr):
        return len(inputStr)
    
    
with open('newsafr.json') as newsafr_file:
    news = json.load(newsafr_file)
    news = dict(news)

for dicts in news['rss']['channel']['items']:
    x += dicts['description'].split()
    x.sort(key=sortByLength, reverse=True)

for title in x:
    if len(title) > 5:
        rez.append(title)
       
rez = Counter(rez)
print('Задание 1')
print(rez.most_common(10))
print('--------------------')



##########################################################################


import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
titles = []
res = []
root = tree.getroot()
xml_title = root.find("channel/title")
xml_items = root.findall("channel/item")

for item in xml_items:
    title = item.find("description")
    titles += title.text.split(" ")

    
def sortByLength(inputStr):
        return len(inputStr)
   

titles.sort(key=sortByLength, reverse=True)

for title in titles:
    if len(title) > 5:
        res.append(title)

res = Counter(res)
print('Задание 2')
print(res.most_common(10))

