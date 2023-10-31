import datetime
import json

def validar(cnpj):
    tentativa = 0
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    while(True):
        if str(cnpj) in dados:  # Verifica se o CNPJ está no dicionário
            senha = input("Digite sua senha: ")
            if senha == dados[str(cnpj)]["senha"]:  # Verifica se a senha corresponde ao CNPJ
                return True
            tentativa += 1
            if tentativa == 3:
                print("Reinicie o programa e tente novamente.")
                break
        else:
            return False

def login():
    while(True):
        login = input("""
===================================================
        Bem vindo ao Banco QuemPoupaTem PJ
===================================================
    1. Login
    2. Registrar

    Escolha a operação desejada:
===================================================
 """)
    
        if login == '1':
            cnpj = int(input("Digite o seu CNPJ: "))
            if validar(cnpj) == True:
                break
            else:
                print("Usuário não cadastrado, tente novamente.")
            
        if login == '2':
            novo_cliente()
            break
            


def novo_cliente():
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

    tipo_conta = input("Tipo da conta(comum/plus): ").capitalize()
    while tipo_conta != "Comum" and tipo_conta != "Plus":
        tipo_conta = input("Por favor insira uma opção correta do seu tipo de conta: ")

    senha = input("Senha: ")
    while(True):
            if len(senha) < 6:
                senha = input("Crie uma senha com pelo menos 6 dígitos: ")
            else:
                break

    dados[cnpj] = {
            "razao_social": razao_social,
            "saldo" : saldo,
            "tipo_conta" : tipo_conta,
            "senha" : senha,
            "transacoes": []
        }
        
    with open("dados.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def apaga_cliente():

    cnpj = int(input("Digite o seu CNPJ: "))

    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    if str(cnpj) in dados:
        del dados[str(cnpj)]

        with open("dados.json", "w") as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print("Cliente removido com sucesso!")
    else:
        print("CNPJ não encontrado, tente novamente com um valor válido!")

def listar_clientes():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)
    print("="*40)
    print("Clientes:")
    print()
    for cnpj, users in dados.items():
        print("="*40)
        print("Razão social:", users["razao_social"])
        print("CNPJ:", cnpj)
        print("Saldo:", users["saldo"])
        print("Tipo da conta:", users["tipo_conta"])
        print("Senha:", users["senha"])
        print("="*40)


def debito():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)
    
    cnpj = input("Digite o seu CNPJ: ")
    
    if cnpj in dados:            
        try:
            valor = float(input("Digite o valor que será debitado: "))  # Pede ao usuário o valor que será debitado
            if valor <= dados[cnpj]["saldo"]:
                dados[cnpj]["saldo"] -= valor
                historico = data_atual()
                lista = ["Debito", valor, dados[cnpj]["saldo"],historico]
                dados[cnpj]["transacoes"].append(lista)
                with open("dados.json", "w") as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print("Valor debitado com sucesso, o seu saldo atual é de:", dados[cnpj]["saldo"])
            else:
                print("O seu saldo é menor que o desejado para debitar")
        except ValueError:      
                print("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
    else:
        print("Não foi possível encontrar o CNPJ. ")
       
        

def deposito():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    cnpj = input("Digite o seu CNPJ: ")
    
    if cnpj in dados:            
        try:
            valor = float(input("Digite o valor que será depositado: "))  # Pede ao usuário o valor que será debitado
            dados[cnpj]["saldo"] += valor
            historico = data_atual()
            lista = ["Deposito", valor, dados[cnpj]["saldo"], historico]
            dados[cnpj]["transacoes"].append(lista)
            with open("dados.json", "w") as arquivo_json:
                json.dump(dados, arquivo_json, indent=4)
            print("Valor depositado com sucesso, o seu saldo atual é de:", dados[cnpj]["saldo"])
        except ValueError:      
                print("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
    else:
        print("Não foi possível encontrar o CNPJ. ")


def transferencia_entre_contas():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    cnpj = input("Digite o seu CNPJ: ")
    if validar(cnpj) == True:   # O programa valida o cnpj e a senha do usuário, e caso estejam corretos, permitem continuar a função
        destino = input("Digite o cnpj do destinatário: ")
        valor = float(input("Digite o valor da transfêrencia: "))
        if valor < dados[cnpj]["saldo"]:
            dados[cnpj]["saldo"] -= valor     # O valor é debitado da conta do remetente e adicionado à conta do destinatário
            historico = data_atual()
            lista = ["Transferencia", valor, dados[cnpj]["saldo"], historico]
            lista_destino = ["Transferencia", -valor, dados[destino]["saldo"], historico]
            dados[cnpj]["transacoes"].append(lista)
            dados[destino]["transacoes"].append(lista_destino)
            with open("dados.json", "w") as arquivo_json:
                json.dump(dados, arquivo_json, indent=4) 
        else:
            print("Você não tem o saldo suficiente para essa transação.")
        dados[destino]["saldo"] += valor
       
        

def extrato():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    print("Aqui será mostrado o extrato do cliente")

def operacao_livre():
    print("Essa função será decidida no futuro")


def data_atual():
    data_atual = datetime.datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_atual