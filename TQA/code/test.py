# -*- coding: utf-8 -*-

import string
from nltk.stem import WordNetLemmatizer

print(string.punctuation)

query = "I love you. Do you love me? Yes, I do."
query_string = query.translate(None, string.punctuation)
print(query_string)

lemmatizer = WordNetLemmatizer()
word = "interested"
word = lemmatizer.lemmatize(word)

print(word)
