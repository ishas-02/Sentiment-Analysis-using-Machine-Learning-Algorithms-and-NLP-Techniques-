import re
import spacy
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

STOPWORDS = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

URL_RE = re.compile(r"http\S+|www\S+|https\S+")
MENTION_RE = re.compile(r"@\w+")
HASHTAG_RE = re.compile(r"#(\w+)")
NON_ALPHA_RE = re.compile(r"[^a-zA-Z\s]")

def clean_text(text):
    text = str(text)
    text = URL_RE.sub(" ", text)
    text = MENTION_RE.sub(" ", text)
    text = HASHTAG_RE.sub(r"\1", text)       
    text = NON_ALPHA_RE.sub(" ", text)
    text = text.lower().strip()
    return text

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([t.lemma_ for t in doc if t.text not in STOPWORDS and t.lemma_.strip()])

def preprocess_pipeline(text):
    return lemmatize_text(clean_text(text))
