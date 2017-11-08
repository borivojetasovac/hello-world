#! /usr/bin/python3
import threading, requests, os, bs4, sys

os.makedirs('xkcd', exist_ok = True)     # store comics in ./xkcd, prevents the function from throwing an exception if this folder already exists

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com%s...' % (urlNumber))
        response = requests.get('http://xkcd.com%s' % (urlNumber))
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'lxml')

        # Find the comic image URL.
        comicElem = soup.select('#comic img')
        if len(comicElem) == 0:
            print('Could not find comic image!')
        else:
            comicUrl = comicElem[0].get('src')

            # Download the comic image.
            try:
                print('Downloading image %s...' % (comicUrl))
                response = requests.get(comicUrl)
                response.raise_for_status()

                # Save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in response.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except Exception as exc:
                print('Wrong comic image URL: ' + str(exc))

downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target = downloadXkcd, args = (i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()   # block until that thread has finished (only than will return)
print('Done.')
