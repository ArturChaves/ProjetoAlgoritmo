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
            if senha in users[cnpj]: # Caso a senha seja correta o usuario é deletado com sucesso  
                return True
        else:
            print("Usuario não cadastrado")
            return False


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
        return users
    else:
        print("Usuário ja cadastrado") # com o valor da tupla, o programa verifica se o usuario ainda nao existe no sistema, caso se confirme, um novo user é criado

def apaga_cliente():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:
        del users[cnpj]

def debito():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    valor = float(input("Digite o valor que será debitado: "))
    print(cnpj)
    print(senha)
    print(valor)

def deposito():
    cnpj = input("Digite o seu CNPJ: ")
    valor = float(input("Digite o valor que será debitado: "))
    print(cnpj)
    print(valor)

def extrato():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    print("Aqui será mostrado o extrato do cliente")

def listar_clientes():
    cnpj = int(input("Digite o seu CNPJ: "))
    if validar(cnpj) == True:
        for chave, valores in users.items():
            print("Portador do cnpj: ", chave)
            for valores in users[cnpj]:
                print(valores)
            

def operacao_livre():
    print("Essa função será decidida no futuro")

def transferencia_entre_contas():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    cnpj_destino = input("Digite o CNPJ de destino: ")
    valor = float(input("Digite o valor: "))
    print(cnpj)
    print(senha)
    print(cnpj_destino)
    print(valor)



