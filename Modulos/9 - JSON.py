import json



# 1 - String para dicionario
pessoa = '{"name": "Lorenzo", "leanguagens": ["Python", "Javascript"]}'
pessoa_dict = json.loads(pessoa)
print(pessoa_dict)
print(pessoa_dict['name'])

# 2 - Convertendo dicionario para JSON
person_json = json.dumps(pessoa_dict)
print(person_json)

