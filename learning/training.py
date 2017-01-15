import pandas as pd
import re
from nltk.corpus import stopwords

def article_to_words( article ):
    letters_only = re.sub("[^a-zA-Z0-9]", " ", article)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return( " ".join( meaningful_words ))


train = pd.read_json("training-data.json")

num_titles = train["title"].size
clean_train_titles = []


for i in xrange( 0, num_titles ):
    clean_train_titles.append( article_to_words( train["title"][i] ) )

from sklearn.feature_extraction.text import TfidfVectorizer #TfidfVectorizer


vectorizer = TfidfVectorizer(ngram_range=(1, 3),
                             lowercase=True,
                             stop_words='english',
                             strip_accents='unicode',
                             min_df=2,
                             norm='l2')

train_data_features = vectorizer.fit_transform(clean_train_titles)
train_data_features = train_data_features.toarray()

#from sklearn.ensemble import RandomForestClassifier
#from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import MultinomialNB

#forest = RandomForestClassifier(n_estimators = 100)
#forest = forest.fit( train_data_features, train["clickbait"] )

forest = MultinomialNB()
forest = forest.fit( train_data_features, train["clickbait"] )

from sklearn.externals import joblib
joblib.dump(forest, 'learned.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


# TESTING
