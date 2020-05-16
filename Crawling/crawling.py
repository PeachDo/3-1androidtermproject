#!/usr/bin/env python3
# Anchor extraction from HTML document
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
while 1:
    context = ssl._create_unverified_context()

    baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    plusUrl = input('Please enter your keyword to search : ')

    url = baseUrl + quote_plus(plusUrl)
    html = urlopen(url, context=context)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='_img')

    n = 1
    for i in img:
        imgUrl = i['data-source']
        with urlopen(imgUrl, context=context) as f:
            with open('/Users/jiwon/AndroidTermProject3-1/crawling/female/dog/' + plusUrl + str(n)+'.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
    print('download complete')
