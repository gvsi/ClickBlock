import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.externals import joblib

def article_to_words( article ):
    letters_only = re.sub("[^a-zA-Z0-9]", " ", article)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return( " ".join( meaningful_words ))


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load('vectorizer.pkl')

test = pd.read_json("test-data.json")

num_titles = len(test["title"])
clean_test_titles = []

for i in xrange(0,num_titles):
    clean_test_titles.append( article_to_words( test["title"][i] ) )

test_data_features = vectorizer.transform(clean_test_titles)
test_data_features = test_data_features.toarray()


forest = joblib.load('learned.pkl')

result = forest.predict_proba(test_data_features)
print result[:,1]

# wrong = 0
# total = 0
#
# for i in xrange(0,num_titles):
#     if test["clickbait"][i] != result[i] :
#         wrong+=1
#
#     total+=1
#
#
# print (float((total-wrong))/total)*100
