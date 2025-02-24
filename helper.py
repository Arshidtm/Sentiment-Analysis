import pickle as pkl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import SnowballStemmer
from gensim.utils import simple_preprocess
import numpy as np

# stemming
stemmer=SnowballStemmer('english')

# word2vec model
with open('tfidf.pkl','rb') as file: 
    tfidf=pkl.load(file)

with open('model1.pkl','rb') as file: 
    model=pkl.load(file)

# basic cleaning
def clean(text): 
    text=text.lower()
    # removing charachter other than alphabets
    text=re.sub('[^a-zA-Z]',' ',text)
    token=word_tokenize(text)
    text=[stemmer.stem(word) for word in token]
    return ' '.join(text)



def predictions(text): 
    cleaned=clean(text)
    inputs=tfidf.transform([cleaned]).toarray()
    pred=model.predict(inputs)
    if pred==0:
        return 'Positive'
    elif pred==1:
        return 'Neutral'
    else: 
        return "Negative"