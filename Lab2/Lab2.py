import gensim
word2vec = gensim.models.KeyedVectors.load_word2vec_format("cbow.txt", binary=False)
pos=["портик_NOUN", "аркада_NOUN","зарисовка_NOUN"]
neg=["фриз_NOUN"]
dist = word2vec.most_similar(positive=pos, negative=neg)
for i in dist:
  print(i)
