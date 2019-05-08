from bs4 import BeautifulSoup
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
tweet = content.findAll('div', attrs ={"class":"tweetcontainer"})

for t in tweet:
    tObject = {
        "author":t.find('h2', attrs={"class":"author"}).text.encode('utf-8'),
        "tweet": t.find('p', attrs ={"class":"content"}).text.encode('utf-8')
    }
    print(tObject)
