import json

with open("dados.json", "a") as arquivo_json:
    if arquivo_json.tell() > 0:
        arquivo_json.write("\n")

    cnpj = input("CNPJ: ")
    razao_social = input("Razão social: ")
    saldo = float(input("saldo inicial:"))
    tipo_conta = input("tipo da conta(comum/plus): ").lower()
    senha = input("senha: ")

    dados = {
        cnpj: {
        "razao_social": razao_social,
        "saldo" : saldo,
        "tipo_conta" : tipo_conta,
        "senha" : senha
    }
    }

    json.dump(dados, arquivo_json, indent=4)


