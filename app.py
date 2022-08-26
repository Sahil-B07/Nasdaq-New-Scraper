from flask import Flask
import requests
from redis import Redis
import getopt,sys
from bs4 import BeautifulSoup


r=Redis(host='redis',port=6379)

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

soup = BeautifulSoup(page.content, features="xml")
key = ticker.upper()
items = soup.find_all('item')


for _,item in enumerate(items,1):
    headline = item.title.string
    date = item.pubDate.string.replace(',','')
    value = headline +" "+ date
    r.rpush(key, value)

print("success!")