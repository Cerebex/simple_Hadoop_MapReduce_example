#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import text
stops = set(text.ENGLISH_STOP_WORDS)
# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace, lower case letters, remove punctuation 
    line = line.strip().lower().translate(None, string.punctuation)    
    # split the line into words; splits on any whitespace
    words = line.split()
    # output tuples (word, 1) in tab-delimited format if is stopword from nltk 
    # english_stop_words
    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
