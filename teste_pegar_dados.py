import json

def procurar_dados():

    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)
    
    cnpj = input("Informe seu cnpj: ")

    if cnpj in dados: 
        conta = dados[cnpj]
        razao_social = conta["razao_social"]
        saldo = conta["saldo"]
        tipo_conta = conta["tipo_conta"]
        senha = conta["senha"]
        
        print("CNPJ:", cnpj)
        print("Razão Social:", razao_social)
        print("Saldo:", saldo)
        print("Tipo de Conta:", tipo_conta)
        print("Senha:", senha)

procurar_dados()