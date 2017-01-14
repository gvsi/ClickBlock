from flask import Flask, request, url_for
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/verifybait', methods=['POST', 'GET'])
def verify():
    #print request.form.get('title')
    print request.form.get('link')

    # do computation with title and link
    result = "not bait"

    # send a post request to extention
#    r = requests.post('http://extentionhere.com', data = {'result': result})
    url = "https://explaintome.herokuapp.com/api/v1.0/summary"
    headers = {'Content-Type': "application/json", 'Accept': '*/*'}
    data = {
        "url": request.form.get('link'),
        "max_sent": 1,
        "lang": "en"
    }
    
    r = requests.post(url, headers=headers, data=json.dumps(data))
    d = json.loads(r.text)
    print "Title:", d["meta"]["opengraph"]["description"]
    print "Summary:", d["summary"][0]

    return 'verified\n'
