from users import *

def validar(cnpj):
    tentativa = 0
    chaves = users.keys()
    while(True):
        if cnpj in chaves: # Caso o cnpj seja correto a próxima validação é a senha            
            senha = input("Digite sua senha: ")
            tentativa += 1
            if tentativa == 3:
                print("Reinicie o programa e tente novamente.")
                break
            if senha in users[cnpj]:  # O programa valida se a senha é compátivel com o cnpj e permite o acesso ao usuário
                return True
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
    valores = [] #cria uma lista com os valores da chave do user
    
    razao_social = input("Informe sua razão social: ")
    valores.append(razao_social) #adiciona a razao social à lista "valores"
    
    tipo_conta = input("Qual o seu tipo de conta? (comum/plus): ").lower()
    while tipo_conta != "comum" and tipo_conta != "plus":
        tipo_conta = input("Por favor insira uma opção correta do seu tipo de conta: ")
    valores.append(tipo_conta)  #verifica o tipo da conta do usuario, e depois adiciona à lista "valores"
    
    while(True):
        try:
            valor_inicial = float(input("Informe o saldo inicial de sua conta: "))
            break
        except ValueError:
            print("Valor inválido")
    valores.append(valor_inicial) # pede ao usuario um input com o valor inicial de sua conta, caso o valor seja inválido, o except constata o erro e mostra ao user
        
    while(True):
        try:
            cnpj = int(input("Informe SOMENTE os números do seu cnpj: "))
            break
        except ValueError:
            print("Seu cnpj é inválido, tente inserir novamente apenas com os números: ") # pede ao usuário o cnpj, caso o valor seja invalido, o except constata o erro e o mostra ao user
    
    senha = input("Crie uma senha com pelo menos 6 dígitos: ")
    
    while(True):
        if len(senha) < 6:
            senha = input("Crie uma senha com pelo menos 6 dígitos: ")
        else:
            break # pede a senha ao usuario com no minimo 6 digitos, caso seja menor, o programa faz ele responder de novo, ate informar uma senha válida

    valores.append(senha)

    if cnpj not in users:
        valores = valores
        users[cnpj] = valores
        print("User cadastrado com sucesso, muito obrigado por fazer parte do nosso banco!")
        print(users)
        return users
    else:
        print("Usuário ja cadastrado") # com o valor da tupla, o programa verifica se o usuario ainda nao existe no sistema, caso se confirme, um novo user é criado

def apaga_cliente():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:  # O programa valida cnpj e a senha, caso estejam corretos, a conta será deletada
        del users[cnpj]
    else:
        print("Usuario não cadastrado")

def listar_clientes():
    cnpj = int(input("Digite o seu CNPJ: "))    
    if validar(cnpj) == True:      
        for chave in users.keys():
            print("")       # O programa busca no dicionário os respectivos valores e mostra ao cliente
            print("Portador do cnpj: ", chave)
            print("Razão social: ", users[chave][1])
            print("Valor: ", users[chave][2])
            print("Senha: R$ ", users[chave][3])
            print("")
    else:
        print("Usuario não cadastrado")

def debito():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:
        while(True):
            try:
                valor = float(input("Digite o valor que será debitado: "))  # Pede ao usuário o valor que será debitado
                break
            except ValueError:      
                print("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
        for chave in users.keys():
            if chave == cnpj:
                users[cnpj][2] -= valor     # O programa debita da conta do usuário e retorna ao programa o valor já ajustado
                return users
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





