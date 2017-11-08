#!/usr/bin/python3
import sys, webbrowser, pyperclip, requests, bs4

# gets address from sys.argv or clipboard and opens it in Google Maps
if len(sys.argv) > 1:
    for i in sys.argv:
        print(i)
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address) # launches new browser to a specified URL

responseObject = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')    # download files from the Web easily
print(type(responseObject))
print(responseObject.status_code == requests.codes.ok)          # status code for 'OK' in the HTTP protocol is 200 ('Not Found' is 400)
print(len(responseObject.text))                                 # web page is stored as a string
print(responseObject.text[:250])
try:
    responseObject.raise_for_status()           # exception if there was an error downloading; nothing if the download succeeded (similar to the above)
except Exception as exc:
    print('There was a problem: %s' % (exc))    # e.g. 404 (URL doesn't exsist)

webFile = open('RomeoAndJuliet.txt', 'wb')      # write binary data
for chunk in responseObject.iter_content(100000):               # returns chunks of the content on each iteration (bytes data type - 100000 bytes each)
    webFile.write(chunk)
webFile.close()

# Beautiful Soap 4:    for parsing a string containing the HTML
bsObject = bs4.BeautifulSoup(open('bs4Example.html'), 'lxml')   # from file/web    'lxml' to avoid 'No parser was explicitly specified' warning
# retrieve a web page element from a BS object by calling the select() method and passing a string of a CSS selector for the element you are looking for(they are like reg exp for HTML)
elems = bsObject.select('#author')              # list of all the Tag elements with id="author"
print('elems[0].getText(): ' + str(elems[0].getText()))         # element's text (inner HTML - content between the opening and closing tags)
print('str(elems[0]): ' + str(elems[0]))                        # starting and closing tags with element's text
print('elems[0].attrs: ' + str(elems[0].attrs))                 # dictionary with the element's attribute 'id', and it's value ('author')
print('get(id): ' + str(elems[0].get('id')))
print(elems[0].get('some_nonexistent') == None)

elems = bsObject.select('p')                    # pulls all the <p> elements from the bs object
for elem in elems:
    print(elem.getText())

'''
<!-- This is the bs4Example.html example file. -->

<html><head><title>The Website Title</title></head>
<body>
  <p>Download my <string>Python</strong> book from <a href="http://inventwithpython.com">my website.</p>
  <p class="slogan">Learn Python the easy way!</p>
  <p>By <span id="author">Al Sweigart</span></p>
</body></html>
'''
