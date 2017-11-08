#!/usr/bin/python3
# opens few top searches on Google      open empty tab at Mozilla first, so it doesn't open 5 Mozillas
import sys, requests, bs4, webbrowser

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    print('What should i google for?')
    sys.exit()

responseObject = requests.get('http://www.google.com/search?as_q=' + search + '')
responseObject.raise_for_status()
bsObject = bs4.BeautifulSoup(responseObject.text, 'lxml')
elems = bsObject.select('.r a')     # all <a> elements that are within an element of the r CSS class

numOpen = min(5, len(elems))        # will open 5 or less tabs (if the result returned less than 5)
for i in range(numOpen):
    webbrowser.open('http://google.com' + elems[i].get('href'))
