import urllib.request
import os
import sys

def consultarCEP():
    os.system('clear')
    cep = input('CEP: ')
    url = 'https://viacep.com.br/ws/%s/json/' % cep
    headers = {'User-Agent': 'Autociencia/1.0'}
    requisição = urllib.request.Request(url, headers=headers, method='GET')
    cliente = urllib.request.urlopen(requisição)
    conteudo = cliente.read().decode('utf-8')
    cliente.close()
    print('{}'.format(conteudo).replace('"', ""))

consultarCEP()


