from flask import Flask, request, url_for
from flask_jsonpify import jsonify
import requests
import json
app = Flask(__name__)

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
        "max_sent": 1,
        "lang": "en"
    }

    print '-----------'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print r.status_code
    print '----------'
    print r.json()
    d = json.loads(r.text)

    newtitle = d["meta"]["opengraph"]["description"].encode('ascii', 'ignore')
    summary = d["summary"][0].encode('ascii', 'ignore')

    print "Title:", newtitle
    print "Summary:", summary

    print '\n'
    print d

    result = {'title': newtitle, 'summary':summary, 'clickbait': 1}
    return jsonify(**result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)