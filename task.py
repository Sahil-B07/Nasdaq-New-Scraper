import requests, redis
import getopt,sys
from bs4 import BeautifulSoup

r = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)
r.flushall()
ticker = 'msft'

cmd_ = sys.argv[1:]
opts, args = getopt.getopt(cmd_, 't:')

for opt, arg in opts:
    if opt in ['-t']:
        ticker = arg

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

URL = "https://www.nasdaq.com/feed/rssoutbound?symbol=" + ticker.upper()
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "xml")
key = soup.find_all('title')[0].string.split(" ")[0]
items = soup.find_all('item')


for i,item in enumerate(items,1):
    headline = item.title.string
    date = item.pubDate.string.replace(',','')
    value = headline +" "+ date
    r.rpush(key, value)

print(r.lrange(ticker.upper(),0,-1))