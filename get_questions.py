from openai import OpenAI
import json

KEY = '####################################'
client = OpenAI(api_key=KEY)

prompt = (
    "Quero fazer um buscador que busque artigos do código civil brasileiro com base em perguntas do usuário. "
    "Para isso preciso de perguntas de exemplo que possam ser respondidas por cada artigo. "
    "Faça três perguntas simples que possam ser respondidas por esse artigo.")

def get_questions(artigo):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": prompt
            },
            {
                "role": "user", 
                "content": artigo
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "email_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "pergunta1": {
                            "description": "Primeira pergunta",
                            "type": "string"
                        },
                        "pergunta2": {
                            "description": "Segunda pergunta",
                            "type": "string"
                        },
                        "pergunta3": {
                            "description": "Terceira pergunta",
                            "type": "string"
                        },
                        "additionalProperties": False
                    }
                }
            }
        }
    )
    return response.choices[0].message.content

with open('artigos.json','r',encoding='utf-8') as f:
    artigos = json.load(f)

perguntas = []
i = 0

while i < len(artigos):
    artigo = artigos[i]
    try:
        perguntas.append({'artigo':artigo,'perguntas':get_questions(artigo)})
        i += 1
        print(f'Artigos: {i}',end = '\r')
    except Exception as e:
        print(e)
        break

with open('perguntas.json','w',encoding='utf-8') as f:
    json.dump(perguntas,f)


