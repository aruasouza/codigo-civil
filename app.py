import streamlit as st
import json
import time
from search import ask

TITLE = 'Código Civil'

html = '''
<style>
.appview-container .main .block-container{
    padding-top: 0px;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 30px
}
.st-emotion-cache-1y4p8pa{
    max-width: 1200px;
}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.block-container {padding-top:1rem;}
.e1fqkh3o4 {padding-top:1rem;}
</style>
'''

with open('artigos.json','r',encoding = 'utf-8') as f:
    artigos = json.load(f)

st.set_page_config(page_title=TITLE, page_icon='📖')
st.markdown(html,unsafe_allow_html = True)

st.markdown(f'''<h1 style='text-align: center; font-family: "times-new-roman"'>{TITLE}</h1>''', unsafe_allow_html=True)
tabquest,tabbook = st.tabs(['Buscar','Todos os artigos'])
prompt = tabquest.chat_input("Busque no Código Civil")
contquest = tabquest.container()
def word_generator(string):
    def gen():
        for word in string.split():
            yield word + " "
            time.sleep(0.02)
    return gen
if prompt:
    contquest.write(f'**{prompt}**')
    with st.spinner('Buscando...'):
        respostas = ask(prompt)
    for resp in respostas:
        contquest.write_stream(word_generator(resp))

contbook = tabbook.container()
for art in artigos:
    contbook.write(art)