from bs4 import BeautifulSoup
import bs4
# url = "http://feeds.bbci.co.uk/news/rss.xml"
# url = "http://feeds.feedburner.com/ndtvnews-world-news"   
import re
import requests
    
def get_data(url):
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
    return data
# print(data[0])

     