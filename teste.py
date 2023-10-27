import json


with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

cnpj = input("CNPJ: ")
razao_social = input("Razão social: ")
saldo = float(input("saldo inicial:"))
tipo_conta = input("tipo da conta(comum/plus): ").lower()
senha = input("senha: ")

dados[cnpj] = {
        "razao_social": razao_social,
        "saldo" : saldo,
        "tipo_conta" : tipo_conta,
        "senha" : senha
    }

    
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)


