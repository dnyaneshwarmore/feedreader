from bs4 import BeautifulSoup
import bs4
url = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
# url = "http://feeds.feedburner.com/ndtvnews-world-news"   
import re
import requests
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
items = soup.find_all('item')
data = []
for item in items:
    #  print (re.sub('\<\>', '', item.title.string))
   img = item.find("a")
    
   data.append({
     "title" : item.title.get_text(),
     "img_src": item.find('media:thumbnail').get('url') if item.find('media:thumbnail')  else img,
     "description": item.find("description").get_text(),
     "link": item.link.text          
   })

print(data[0])

     