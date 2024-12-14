from sentence_transformers import SentenceTransformer
import json
from sklearn.neighbors import NearestNeighbors
import numpy as np

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

with open('embeddings.json','r',encoding = 'utf-8') as f:
    data = json.load(f)

embeds = []
for point in data:
    embeds += list(point['embeddings'].values())

arr = np.array(embeds)
nbrs = NearestNeighbors(n_neighbors = 5,metric='cosine').fit(arr)

def embed(sentences):
    return model.encode(sentences)

def ask(pergunta):
    if not pergunta:
        return []
    enc = embed([pergunta])
    distances,indices = nbrs.kneighbors(enc)
    trechos = [data[i // 3]['artigo'] for i in indices[0]]
    return trechos