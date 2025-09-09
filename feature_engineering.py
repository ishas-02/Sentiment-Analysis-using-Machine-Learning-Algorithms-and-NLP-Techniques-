# src/feature_engineering.py
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def tfidf_features(corpus, max_features=5000, ngram_range=(1,2)):
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
    return vectorizer.fit_transform(corpus), vectorizer

def word2vec_features(corpus, vector_size=100, window=5, min_count=2):
    try:
        from gensim.models import Word2Vec
    except Exception as e:
        raise ImportError(
        ) from e

    tokenized = [str(doc).split() for doc in corpus]
    w2v_model = Word2Vec(sentences=tokenized, vector_size=vector_size, window=window, min_count=min_count)
    vectors = [
        np.mean([w2v_model.wv[w] for w in words if w in w2v_model.wv] or [np.zeros(vector_size)], axis=0)
        for words in tokenized
    ]
    return np.array(vectors), w2v_model
