#! python3

import requests, os, bs4

url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):

    #Download page.
    print('Downloading %s...' % url)
    req = requests.get(url)
    req.raise_for_status()

    soup = bs4.BeautifulSoup(req.text, "html.parser")

    #Find URL of comic img
    comicElement = soup.select('#comic img')
    if comicElement == []:
        print('Could not find comic img.')
    else:
        try:
            comicUrl = 'http:' + comicElement[0].get('src')
            #Download image
            print('Downloading image %s...' % comicUrl)
            req = requests.get(comicUrl)
            req.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue


        #Save img
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in req.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get prev button
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')    
