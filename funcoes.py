import datetime
import json
from colorama import Fore, Back, Style

def validar(cnpj):
    tentativa = 0
    dados = ler()
    while(True):
        if str(cnpj) in dados:  # Verifica se o CNPJ está no dicionário
            senha = input("Digite sua senha: ")
            if senha == dados[str(cnpj)]["senha"]:  # Verifica se a senha corresponde ao CNPJ
                return True
            tentativa += 1
            if tentativa == 3:  # caso o user erre a senha 3 vezes, o programa precisará reiniciar
                print("Reinicie o programa e tente novamente.")
                break
        else:
            return False

def login():
    while(True):
        login = input(Fore.LIGHTGREEN_EX + Style.BRIGHT +"""
                                                   
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
            if validar(cnpj) == True:   # faz a validação por meio da função e permite o login do user
                break
            else:
                print("Usuário não cadastrado, tente novamente.")
            
        if login == '2':
            novo_cliente()
            break
            


def novo_cliente():
    dados = ler()
    while(True):
        cnpj = int(input("CNPJ: "))
        cnpj = str(cnpj)
        validacao_cnpj = True
        if len(cnpj) == 3:      # aqui faz a comparação para saber o tamanho do cnpj, caso seja 14, está liberado para continuar as proximas etapas
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
        }       # esse é o modelo do dicionario que consta no arquivo .json
        
    escrever(dados) # com esse comando, esse dicionario é escrito no json dessa maneira

def apaga_cliente():
    
    print("")
    cnpj = input("Digite o seu CNPJ: ")

    dados = ler() # o with open("dados","r") serve para fazer a leitura do dicionario, o load puxa esses dados e transforma em um dicionario que pode ser manipulado no python

    if str(cnpj) in dados:
        del dados[str(cnpj)]

        escrever(dados)
        
        print("")
        print_verde("Cliente removido com sucesso!")  # o arquivo muda os valores que se pede e reescreve o dicionario e passa ao arquivo json
        print("")
    else:
        print("")
        print_verde("CNPJ não encontrado, tente novamente com um valor válido!")
        print("")

def listar_clientes():
    dados = ler()
    print("="*40)
    print("")
    print(Style.BRIGHT + "Clientes:")
    print("")
    for cnpj, users in dados.items():
        print_verde("="*40)
        print("")
        print("Razão social:", users["razao_social"])
        print("CNPJ:", cnpj)
        print("Saldo:", users["saldo"])
        print("Tipo da conta:", users["tipo_conta"])
        print("Senha:", users["senha"])
        print("")


def debito():
    dados = ler()
    
    cnpj = input("Digite o seu CNPJ: ")
    
    if cnpj in dados:            
        try:
            valor = float(input("Digite o valor que será debitado: "))  # Pede ao usuário o valor que será debitado
            if dados[cnpj]["tipo_conta"] == "Plus":
                saldo_atual = dados[cnpj]["saldo"] - valor
                if saldo_atual >= -5000:
                    tarifa, valor = tarifar(valor, dados, cnpj)      
                    dados[cnpj]["saldo"] -= valor
                    historico = data_atual()
                    lista = ["Debito", valor, dados[cnpj]["saldo"],historico, tarifa]
                    dados[cnpj]["transacoes"].append(lista) # esse .append(lista) serve para adicionar as transações na conta do user, e será usado para fazer o extrato
                    print("")
                    print_verde("Valor debitado com sucesso, o seu saldo atual é de: R$", dados[cnpj]["saldo"])
                    print("")
                else:
                    print("")
                    print("Não foi possível completar esta ação, com esse valor, a sua conta ultrapassaria o limite negativo da sua conta")
                    print("")
                    
            elif dados[cnpj]["tipo_conta"] == "Comum":
                saldo_atual = dados[cnpj]["saldo"] - valor
                if saldo_atual >= -1000:
                    tarifa, valor = tarifar(valor, dados, cnpj)      
                    dados[cnpj]["saldo"] -= valor
                    historico = data_atual()
                    lista = ["Debito", valor, dados[cnpj]["saldo"],historico, tarifa]
                    dados[cnpj]["transacoes"].append(lista) # esse .append(lista) serve para adicionar as transações na conta do user, e será usado para fazer o extrato
                    print("")
                    print_verde("Valor debitado com sucesso, o seu saldo atual é de: R$", dados[cnpj]["saldo"])
                    print("")
                else:
                    print("")
                    print_verde("Não foi possível completar esta ação, com esse valor, a sua conta ultrapassaria o limite negativo da sua conta")
                    print("")
                          
            escrever(dados)
                
                
    
        except ValueError:
                print("")      
                print_verde("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
                print("")
    else:
        print("")
        print("Não foi possível encontrar o CNPJ. ")
        print("")
        

def deposito():
    dados = ler() # este comando segue a mesma logica da função débito, o programa lê o dicionario, passa para o python que faz as mudanças necessárias e logo após disso, o reescreve novamente em formato .json

    print("")
    cnpj = input_verde("Digite o seu CNPJ: ")
    print("")
    if cnpj in dados:            
        try:
            valor = float(input("Digite o valor que será depositado: "))  # Pede ao usuário o valor que será debitado
            dados[cnpj]["saldo"] += valor
            historico = data_atual()
            lista = ["Deposito", valor, dados[cnpj]["saldo"], historico]
            dados[cnpj]["transacoes"].append(lista)
            
            escrever(dados)

            print("Valor depositado com sucesso, o seu saldo atual é de:", dados[cnpj]["saldo"])
        except ValueError:      
                print("Tipo de saldo inválido, tente novamente apenas com números.")    # Caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
    else:
        print("")
        print_verde("Não foi possível encontrar o CNPJ. ")
        print("")


def transferencia_entre_contas():
    
    dados = ler()

    cnpj = input("Digite o seu CNPJ: ")
    if validar(cnpj) == True:   # O programa valida o cnpj e a senha do usuário, e caso estejam corretos, permitem continuar a função
        destino = input("Digite o cnpj do destinatário: ")
        valor = float(input("Digite o valor da transfêrencia: "))
        if valor < dados[cnpj]["saldo"]:
            dados[cnpj]["saldo"] -= valor     # O valor é debitado da conta do remetente e adicionado à conta do destinatário, e a transação fica salva no extrato dos dois clientes envolvidos na transferência
            dados[destino]["saldo"] += valor
            historico = data_atual()
            lista = ["Transferencia", -valor, dados[cnpj]["saldo"], historico]
            lista_destino = ["Transferencia", valor, dados[destino]["saldo"], historico]
            dados[cnpj]["transacoes"].append(lista)
            dados[destino]["transacoes"].append(lista_destino)
            escrever(dados)
        else:
            print("")
            print_verde("Você não tem o saldo suficiente para essa transação.")
            print("")
        

def extrato():

    dados = ler()

    cnpj = input("Digite o seu CNPJ: ")
    if cnpj in dados:
        for transacoes in dados[cnpj]["transacoes"]:
            if len(transacoes) == 5 :
                tipo, valor, saldo, data, tarifa = transacoes
                print("")
                print_verde(f"Tipo: {tipo} | Valor: R$ {valor} | Tarifa: R$ {tarifa} | Saldo atual: R$ {saldo} | Data: {data}")
                print("")
            else:
                tipo, valor, saldo, data = transacoes
                print("")
                print_verde(f"Tipo: {tipo} | Valor: R$ {valor} | Saldo atual: R$ {saldo} | Data: {data}")
                print("")


        
def gerenciar_funcionarios():
    while(True):
        print()
    
def verificar_cnpj():
    dados = ler()
    for tentativas in range(3):
        try:
            cnpj = int(input("Digite seu CNPJ: "))
            if cnpj in dados:
                return True
        except ValueError:
            print("CNPJ inválido, favor inserir novamente")

def data_atual():
    data_atual = datetime.datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_atual

def tarifar(valor, dados, cnpj):
    if dados[cnpj]["tipo_conta"] == "Plus":
        tarifa = valor*0.03
        valor += tarifa
    elif dados[cnpj]["tipo_conta"] == "Comum":
        tarifa = valor*0.05
        valor += tarifa 
    return tarifa, valor
        
def ler():
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)
        return dados

def escrever(dados):
    with open("dados.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
        
def print_verde(texto):
    print(Fore.LIGHTGREEN_EX + texto + Style.RESET_ALL)

def input_verde(texto):
    input(Fore.LIGHTGREEN_EX + texto + Style.RESET_ALL)