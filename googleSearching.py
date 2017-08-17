#! python3

import requests, sys, webbrowser, bs4

print('Google Searching....')

req = requests.get('https://www.google.com.tw/search?q=' +  ' '.join(sys.argv[1:]))
req.raise_for_status()
#sys.argv[] 用來接收cmd line的參數


soup = bs4.BeautifulSoup(req.text, "html.parser")

#find CSS type is "r", elements are "<a>"
linkElements = soup.select('.r a')

#if search results less than 3, store the numbers of results
#then set the range
tabsOpen = min(3, len(linkElements))
for i in range(tabsOpen):
    webbrowser.open('https://www.google.com' + linkElements[i].get('href'))
