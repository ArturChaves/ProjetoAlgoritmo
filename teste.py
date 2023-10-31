import json


with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)


while(True):
    cnpj = int(input("CNPJ: "))
    cnpj = str(cnpj)
    validacao_cnpj = True
    if len(cnpj) == 3:
        for contas in dados.keys():
            if cnpj in contas:
                validacao_cnpj = False
            else:
                break
        if validacao_cnpj == False:
            print("Valor inválido, tente novamente!")
        else:
            break
    else:
        print("Valor inválido, tente novamente!")
        
    
        

razao_social = input("Razão social: ")

while(True):
    try:
        saldo = float(input("Informe o saldo inicial de sua conta: "))
        break
    except ValueError:
        print("Valor inválido, tente novamente!")

tipo_conta = input("tipo da conta(comum/plus): ").capitalize()
while tipo_conta != "Comum" and tipo_conta != "Plus":
    tipo_conta = input("Por favor insira uma opção correta do seu tipo de conta: ")

senha = input("senha: ")
while(True):
        if len(senha) < 6:
            senha = input("Crie uma senha com pelo menos 6 dígitos: ")
        else:
            break

dados[cnpj] = {
        "razao_social": razao_social,
        "saldo" : saldo,
        "tipo_conta" : tipo_conta,
        "senha" : senha
    }
    
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)


