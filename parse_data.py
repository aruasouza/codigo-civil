from bs4 import BeautifulSoup
import re
import json

def clean(text):
    return re.sub(r'\s+', ' ', text).strip()

with open('L10406compilada.htm') as f:
    html = f.read()
    
soup = BeautifulSoup(html)
grupos = soup.find_all(id="art2")
artigos = []

for grupo in grupos:
    art = ''
    paragrafos = grupo.find_all('p')
    for par in paragrafos:
        cl = clean(par.text)
        if cl[:4] == 'Art.':
            artigos.append(art)
            art = cl
            continue
        art += f'\n{cl}'
    artigos.append(art)

artigos = [art for art in artigos if art]

with open('artigos.json','w',encoding='utf-8') as f:
    json.dump(artigos,f)