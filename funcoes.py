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
    1. Login
    2. Registrar

    Escolha a operação desejada: """)
    
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
            "transacoes": {}
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
    print("Clientes:")
    print()
    for cnpj, users in dados.items():
        print("Razão social:", users["razao_social"])
        print("CNPJ:", cnpj)
        print("Saldo:", users["saldo"])
        print("Tipo da conta:", users["tipo_conta"])
        print("Senha:", users["senha"])
        print()


def debito():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    cnpj = int(input("Digite o seu CNPJ: "))
    while(True):
        try:
            valor = float(input("Digite o valor que será debitado: "))  # Pede ao usuário o valor que será debitado
            break
        except ValueError:      
            print("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
        for cnpj, user in dados.items():
            if cnpj == dados[cnpj]:
                dados[cnpj]["saldo"] -= valor     # O programa debita da conta do usuário e retorna ao programa o valor já ajustado
                with open("dados.json", "w") as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print("Valor debitado com sucesso, o seu saldo atual é de:", dados[cnpj]["saldo"])
                break
            else:
                print("Usuário inválido, tente novamente")
        

def deposito():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:
        while(True):
            try:
                valor = float(input("Digite o valor que será depositado: "))    # assim como na função debito(), é requisitado do usuário o valor a ser depositado
                break
            except ValueError:
                print("Tipo de saldo inválido, tente novamente apenas com números.")
        for chave in users.keys():
            if chave == cnpj:
                users[cnpj][2] += valor # O programa deposita na conta do usuário e retorna ao programa o valor já ajustado
                print(users)
                return users
    else:
        print("Usuário inválido, tente novamente")

def transferencia_entre_contas():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:   # O programa valida o cnpj e a senha do usuário, e caso estejam corretos, permitem continuar a função
        destino = int(input("Digite o cnpj do destinatário: "))
        valor = float(input("Digite o valor da transfêrencia: "))
        users[cnpj][2] -= valor     # O valor é debitado da conta do remetente e adicionado à conta do destinatário
        users[destino][2] += valor
        print(users)
        return users
def extrato():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    print("Aqui será mostrado o extrato do cliente")

def operacao_livre():
    print("Essa função será decidida no futuro")





