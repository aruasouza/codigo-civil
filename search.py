from sentence_transformers import SentenceTransformer
import json
from sklearn.neighbors import NearestNeighbors
import numpy as np
import re

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

def clean(pergunta):
    return re.sub(r'[^a-z0-9\sáéíóúâêôãõàç-]','',pergunta.lower()).replace('-',' ')

def ask(pergunta):
    if not pergunta:
        return []
    enc = embed([clean(pergunta)])
    distances,indices = nbrs.kneighbors(enc)
    trechos = [data[i // 3]['artigo'] for i in indices[0]]
    return trechos