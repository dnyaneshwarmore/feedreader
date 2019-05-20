from bs4 import BeautifulSoup
import bs4
# url = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
# url = "http://feeds.feedburner.com/ndtvnews-world-news"   
# url = "https://www.thehindu.com/opinion/open-page/feeder/default.rss"
url= "http://feeds.bbci.co.uk/news/rss.xml#"
import requests
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
# print(soup)
# items = soup.find_all('item')
data = []
items = soup.findAll('item')

for i in items:
    # print(i.string)
    date = None
    if i.find("pubDate"):
        date = i.find("pubDate").text
    if (i.find("pubdate")):
         date = i.find("pubdate").text
    print(date) 
    print("***********************************************************************")
# for item in items:
    #  print (re.sub('\<\>', '', item.title.string))
#    img = item.find("a")
    # 
#    data.append({
    #  "title" : item.title.get_text(),
    #  "img_src": item.find('media:thumbnail').get('url') if item.find('media:thumbnail')  else img,
    #  "description": item.find("description").get_text(),
    #  "link": item.link.text          
#    })

# print(data[0])

     