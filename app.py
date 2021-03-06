from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    text1 = request.form['text1'].lower()
    
    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])
    
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text=text1)
    compound = round((1 + score['compound'])/2, 2)
    pos = round(score['pos'],2) *100
    neu = round(score['neu'],2) *100
    neg = round(score['neg'],2) *100
    if neu>pos and neu>neg and neu>0.80:
       mes = "Neutral"
    elif pos>neg and pos>neu:
       mes = "Positive"
    elif neg>pos and neg>neu:
       mes = "Negative"
    
    return render_template('index.html', final=compound, text1=text1, negative=neg, positive=pos, neutral=neu, message=mes)
    

def score(text1):
    sia = SentimentIntensityAnalyzer()
    sc = sia.polarity_scores(text1)
    compound = round((1 + sc['compound'])/2, 2)
    pos = round(sc['pos'],2)
    neu = round(sc['neu'],2)
    neg = round(sc['neg'],2)
    if neu>pos and neu>neg and neu>0.80:
         Neu = print("Neutral")
         return Neu
    elif pos>neu and pos>neg:
         Pos = print("Positive")
         return Pos
    elif neg>pos and neg>neu:
         Neg = print("Negative")
         return Neg

if __name__ == "__name__":
    app.run(debug=True, host="127.0.0.1", port=5000, threaded=True)