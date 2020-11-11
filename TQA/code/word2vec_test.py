# -*- coding: utf-8 -*-


from gensim.models import Word2Vec

word2vec_path = "../../word2vec/GoogleNews-vectors-negative300.bin.gz"
model = Word2Vec.load_word2vec_format(word2vec_path, binary=True)