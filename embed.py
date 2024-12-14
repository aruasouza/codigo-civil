from sentence_transformers import SentenceTransformer
import torch
import numpy as np
import json
import ast

torch.cuda.set_device(0)

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

with open('perguntas.json','r',encoding='utf-8') as f:
    data = json.load(f)

for i,point in enumerate(data):
    eval_dict = ast.literal_eval(point['perguntas'])
    perguntas = list(eval_dict.values())
    embeddings = model.encode(perguntas)
    data[i]['embeddings'] = {f'embedding{j + 1}':embeddings[j].tolist() for j in range(3)}
    data[i]['perguntas'] = eval_dict

with open('embeddings.json','w',encoding='utf-8') as f:
    json.dump(data,f)


