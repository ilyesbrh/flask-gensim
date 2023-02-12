from gensim.models import Word2Vec
from flask import Flask, jsonify, request

app = Flask(__name__)

model = Word2Vec.load("model_2022.bin")

@app.route('/')
def word2vec():
    w = request.args.get('word')
    
    # return jsonify(model.wv.index_to_key)
    return jsonify(model.wv.most_similar(positive=[w], topn=10))

if __name__ == '__main__':
    app.run(debug=True)
