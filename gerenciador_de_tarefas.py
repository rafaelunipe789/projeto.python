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
def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa por enquanto.")
        return

    for i, t in enumerate(tarefas, 1):
        status = "OK" if t.get('concluida') else ("Pendente")
        print(f"{i}. [{status}] {t.get('descricao')}")

def nova(tarefas):
    desc = input("Digite a descrição da nova tarefa: ").strip()
    if desc:
        tarefas.append({'descricao': desc, 'concluida': False})
        print("Tarefa adicionada!")
    else:
        print("Descrição vazia, nada foi adicionado.")

def concluir(tarefas):
    listar(tarefas)
    try:
        num = int(input("Número da tarefa para marcar como concluída: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]['concluida'] = True
            print("Tarefa marcada como feita.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")
        def apagar(tarefas):
    listar(tarefas)
    try:
        num = int(input("Número da tarefa que deseja excluir: ")) - 1
        if 0 <= num < len(tarefas):
            removida = tarefas.pop(num)
            print(f"Tarefa '{removida['descricao']}' apagada.")
        else:
            print("Número fora do intervalo.")
    except ValueError:
        print("Entrada inválida.")

def main():
    tarefas = carregar()

