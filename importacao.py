import json
import os

ARQUIVO = 'tarefas.json'

def carregar():
    if os.path.isfile(ARQUIVO):
        with open(ARQUIVO, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

def salvar(lista):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(lista, arquivo, indent=4)
