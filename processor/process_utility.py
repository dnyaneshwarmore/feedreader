'''
this module contains all utility function required for extracting the data
'''

from bs4 import BeautifulSoup
import bs4
# url = "http://feeds.bbci.co.uk/news/rss.xml"
# url = "http://feeds.feedburner.com/ndtvnews-world-news"   
import requests
    
def get_data(url):
    '''
    returns all the feed data to show on web page
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.find_all('item')
    title = soup.title.text
    data = []
    for item in items:
       img = None
       data.append({
         "title" : item.title.get_text(),
         "img_src": item.find('media:thumbnail').get('url') if item.find('media:thumbnail')  else img,
         "description": item.find("description").get_text(),
         "link": item.link.text,
         "date" : get_date(item)          
       })
    return title,data


def get_date(i):
  '''
  this fuction returns the date attribute value 
  '''

  date = None
  if i.find("pubDate"):
        date = i.find("pubDate").text
  if (i.find("pubdate")):
         date = i.find("pubdate").text
  return date
     