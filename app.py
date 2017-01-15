from flask import Flask, request, url_for
from flask_jsonpify import jsonify
import requests
# from nltk.corpus import stopwords
from sklearn.externals import joblib
import re
import json

app = Flask(__name__)

def article_to_words( article ):
    letters_only = re.sub("[^a-zA-Z0-9]", " ", article)
    words = letters_only.lower().split()
    # stops = set(stopwords.words("english"))
    # meaningful_words = [w for w in words if not w in stops]
    return( " ".join( words ))


@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/verifybait', methods=['POST', 'GET'])
def verify():

    link = request.args.get('link')
    # title = request.args.get('title')

    print link
    # do computation with title and link
    # clickbait = 0 or 1

    # send a post request to extention
#    r = requests.post('http://extentionhere.com', data = {'result': result})
    url = "https://explaintome.herokuapp.com/api/v1.0/summary"
    headers = {'Content-Type': "application/json", 'Accept': 'application/json'}
    data = {
        "url": link,
        "max_sent": 10,
        "lang": "en"
    }

    print '-----------'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print r.status_code
    print '----------'
    print r.json()
    d = json.loads(r.text)

    title = d["meta"]["opengraph"]["title"]
    newtitle = d["meta"]["opengraph"]["description"].encode('ascii', 'ignore')
    summary = d["summary"][0].encode('ascii', 'ignore')
    longsummary = "<br><br>".join(d["summary"]).encode('ascii', 'ignore')

    # clickbaitProb = 1;
    vectorizer = joblib.load('learning/vectorizer.pkl')
    clean_test_titles = [article_to_words( title )]
    test_data_features = vectorizer.transform(clean_test_titles).toarray()

    classifier = joblib.load('learning/learned.pkl')
    clickbait_probs = classifier.predict_proba(test_data_features)[0]

    print "Title:", newtitle
    print "Summary:", summary
    print "isClickbait", clickbait_probs
    print "Long Summary:"

    print longsummary
    print '\n'

    result = {'title': newtitle, 'summary':summary, 'clickbait': clickbait_probs[1], 'long_summary': longsummary}
    return jsonify(**result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
