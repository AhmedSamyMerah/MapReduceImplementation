import time
import re
from collections import Counter
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

data = open("test.txt", "r")

def clean_word(word):
    return re.sub(r'[^\w\s]','',word).lower()
def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()