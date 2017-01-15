import sys
import urllib
import urllib2
from urllib2 import URLError
import json
from guess_language import guessLanguage
import csv
from bs4 import BeautifulSoup

titles = []
documents = []
total = 0
for i in range(1, 200):

    # url = "http://query.nytimes.com/search/sitesearch/#/*/30days/document_type%3A%22article%22/"+ str(i) + "/allauthors/newest/"
    url = "http://query.nytimes.com/svc/add/v1/sitesearch.json?begin_date=30daysago&sort=desc&page="+str(i)+"&fq=document_type%3A%22article%22&facet=true"
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 

    # print "Reading " + url + " -------"
    try:
        response = urllib2.urlopen(req)
        # print response
        obj = json.loads(response.read())
        for i in range(len(obj['response']['docs'])):
            print obj['response']['docs'][i]['headline']['main']
            titles.append(obj)
            print "------"
            doc = {'clickbait': 0, 'title': obj['response']['docs'][i]['headline']['main']}
            documents.append(doc)
            total += 1

    
    except URLError as e:
        print "ERROR --------"
        print e.reason

# open file for dumping
with open('../data/new_nytimes.json', 'w') as fp:
    json.dump(docs, fp)
            

print "Finished with "+ str(total) + " NY Times Articles"

print "FINISHED"

