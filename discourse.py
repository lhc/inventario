#!/usr/bin/python

import time
import requests
import os
from bs4 import BeautifulSoup

API_KEY = 'gere uma API key na interface do discourse e edite aqui!'

def gera_inventario(id):
  print(f'Criando item {id}')

  caminho = os.path.join('docs', '%04d' % id)
  
  assets = {}

  conteudo = open(os.path.join(caminho, 'index.html')).read()
  for asset, upload in assets.items():
    conteudo = conteudo.replace(f'\"assets/{asset}\"', upload['url'])
  soup = BeautifulSoup(conteudo, features='html5lib')
  
  h1 = soup.find('h1').text
  h2 = soup.find('h2').text

  if h2.startswith('Nenhum item'):
    title = f'Item de inventário #{id:04}'
    body = 'Descreva teste item no inventário e faça upload de fotos, manuais, etc'
  else:
    title = f'{h1}: {h2}'
    while title.endswith('.'):
      title = title[:-1]
    body = ''.join(str(s).strip() for s in soup.find('h2').next_siblings) + "\n\n\n"

  asset_dir = os.path.join(caminho, 'assets')
  for asset in os.listdir(asset_dir):
    if asset == 'item.jpg' or asset == 'item.jpeg':
      continue

    print(f'   Upload: {asset}')

    r = requests.post('https://discourse.lhc.net.br/uploads.json',
      files = {
        'files[]': (asset, open(os.path.join(asset_dir, asset), 'rb'), 'image/jpeg'),
      },
      data = {
        'type': 'image',
        'synchronous': True,
      },
      headers = {
        'Api-Key': API_KEY,
        'Api-Username': 'system',
      }
    )

    if r.status_code != 200:
      if 'rate_limit' in str(r.content):
        print('Esperando o servidor liberar')
        time.sleep(20)
        return gera_inventario(id)
    
    j = r.json()
    body += f"\n![image|{j['width']}x{j['height']}]({j['short_url']})\n"
  
  print(f'    Criando topico: {title}')
  r = requests.post('https://discourse.lhc.net.br/posts.json',
      json = {
        'title': title,
        'category': '25',
        'raw': body,
        'archetype': 'wiki',
     },
      headers = {
        'Api-Key': API_KEY,
        'Api-Username': 'system',
      }
  )
  if r.status_code != 200:
    if 'rate_limit' in str(r.content):
      print('Esperando o servidor liberar')
      time.sleep(20)
      return gera_inventario(id)
  
    print(r.content)
    r.raise_for_status()

  with open(os.path.join(caminho, 'index.html'), 'w') as index:
    j = r.json()
    index.write(f'''<meta http-equiv="refresh" content="0; url=https://discourse.lhc.net.br/t/{j['topic_id']}">
    <a href="https://discourse.lhc.net.br/t/{j['topic_id']}">Seguir</a>
    <script>window.top.location.href = 'https://discourse.lhc.net.br/t/{j['topic_id']}';</script>''')

for id in range(1, 101):
  gera_inventario(id)
