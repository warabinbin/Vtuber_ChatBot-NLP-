from gensim.models import word2vec

model_file = 'Vtuber_w2v_model.model'

model = word2vec.Word2Vec.load('../src/' + model_file)
words = ['配信','絵', '描く']
for word in words:
    similar_words = model.most_similar(positive=[word])
    print(word,':',[w[0] for w in similar_words])