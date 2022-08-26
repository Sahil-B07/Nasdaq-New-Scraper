from flask import Flask
import requests
from redis import Redis
from bs4 import BeautifulSoup

app= Flask(__name__)
r=Redis(host='redis',port=6379)

@app.route('/news/<ticker>')
def hello(ticker):
    r.flushall()

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

    return ("Success!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
