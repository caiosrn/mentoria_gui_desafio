import requests
import json

todas_as_vagas = []

def buscar_vagas_gupy(vaga: str):
  if not isinstance(vaga, str):
    return print('Não há vagas!')
  
  print('Buscando vagas na Gupy...')

  total = 10
  offset = 0

  for _ in range(0, total, 10):
    url = f'https://portal.api.gupy.io/api/job?name={vaga}&offset={offset}&limit=10'
    print(url)
    resposta = requests.get(url)
    if resposta.status_code == 200:
      dados = resposta.json()
      for item in dados.get('data', []):
        todas_as_vagas.append(item)

      offset += 10

    else:
      print(f'Erro ao buscar vagas: {resposta.status_code}')
      break

    with open(f'./data/vagas_gupy_{vaga}.json', 'w', encoding='utf-8') as gupy:
      json.dump(todas_as_vagas, gupy, ensure_ascii=False, indent=2)
    print('Vagas salvas com sucesso em vagas_gupy_{}.json'.format(vaga))
