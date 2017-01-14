import sys
import urllib
import urllib2
from urllib2 import URLError
import json
from guess_language import guessLanguage
import csv
from bs4 import BeautifulSoup

def get_buzzfeed_docs():
    """ 
    doc example: {title, summary, clickbait}
    """
    total = 0

    docs = []

    # loop over days for January
    for i in range(1, 18):
        date = "2017/1/"+str(i)
        url = "https://www.buzzfeed.com/archive/"+date
        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        print "Reading " + url
        try:
            response = urllib2.urlopen(req)
            page = response.read()
            soup = BeautifulSoup(page, "html.parser")
            
            lis = soup.find_all('ul', {'class': 'flow'})
            lis = lis[0].contents
            li_content = []
            
            # Extract string from the NavigableString object
            for i, item in enumerate(lis):
                if(item.string != '\n'):
                    lang = guessLanguage(item.string)
                    print lang+" : "+item.string
                    if lang == "en":
                        li_content.append(item.string)
                        doc = {}
                        doc['clickbait'] = 1
                        doc['title'] = item.string.encode('ascii', 'ignore')
                        docs.append(doc)

            total += len(li_content)

        except URLError as e:
            print "ERROR ----------"
            print e.reason

    
    print "END OF LOOP -------------------------"
    
    # open file for dumping
    with open('../data/buzzfeed.json', 'w') as fp:
        json.dump(docs, fp)
            

    print "Finished with "+ str(total) + " English Articles"

if __name__ == "__main__":
    get_buzzfeed_docs()
