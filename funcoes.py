import datetime
import json
from colorama import Fore, Style  # importação das bibliotecas necessárias

def ler(): # essa função é a responsável por sempre ler o arquivo .JSON
    with open("dados.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)
        return dados

def escrever(dados): # essa função é responsável por sempre escrever o que foi alterado no python no arquivo .JSON
    with open("dados.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
        
def validar(cnpj):
    # função para validar CNPJ e senha do usuário
    tentativa = 0
    dados = ler()
    estilo_azul = Fore.LIGHTBLUE_EX + Style.BRIGHT
    estilo_branco = Fore.LIGHTWHITE_EX + Style.BRIGHT
    fim_estilo = Style.RESET_ALL

    while True:
        if str(cnpj) in dados:  # verifica se o CNPJ está no dicionário
            senha = input(estilo_azul + "Digite sua senha: " + fim_estilo + estilo_branco)
            if senha == dados[str(cnpj)]["senha"]:  # verifica se a senha corresponde ao CNPJ
                return True
            tentativa += 1
            if tentativa == 3:  # caso o usuário erre a senha 3 vezes, o programa precisa reiniciar
                print("Reinicie o programa e tente novamente.")
                break
            else:
                return False

def verificar_cpf(cpf, cnpj):
    # função para verificar o CPF do funcionário
    tentativa = 0
    dados = ler()
    while True:
        if str(cpf) in dados[cnpj]["funcionarios"]:  # verifica se o CPF está no dicionário
            return True
        else:
            return False

def login():
    # função para login ou registro de cliente
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX

    while True:
        login = input(estilo_azul + """                                                
 _________________________________________________ 
|                                                 |
|       Bem-vindo ao Banco QuemPoupaTem PJ        |
|_________________________________________________|
|                                                 |
|    1. Login                                     | 
|    2. Registrar                                 | 
|                                                 | 
|    Escolha a operação desejada:                 | 
|_________________________________________________|
                                                   
 """)
        try:
            if login == '1':
                print("")
                cnpj = int(input(estilo_azul + "Digite o seu CNPJ: "))
                if validar(cnpj) == True:  # realiza a validação usando a função e permite o login do usuário
                    break
                else:
                    print("")
                    print("Usuário não cadastrado, tente novamente.")
            
            if login == '2':
                novo_cliente()
                break
        except ValueError:
            print_vermelho("CNPJ digitado incorretamente, tente novamente!")
            


def novo_cliente():
    # função para criar um novo cliente
    dados = ler()
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    while(True):
        try:
            print("")
            cnpj = int(input(estilo + "CNPJ: "))
            cnpj = str(cnpj)
            validacao_cnpj = True
            if len(cnpj) == 14:  # verifica o tamanho do CNPJ, que deve ser 14 dígitos
                for contas in dados.keys():
                    if cnpj in contas:
                        validacao_cnpj = False
                    else:
                        break
                if validacao_cnpj == False:
                    print_vermelho("Já existe uma conta cadastrada com esse CNPJ, tente novamente!")
                else:
                    break
            else:
                print_vermelho("Valor inválido, tente novamente!")
        except ValueError:
            print_vermelho("CNPJ inválido")

    razao_social = input("Razão social: ")

    while(True):
        try:
            saldo = float(input(Style.RESET_ALL + Fore.LIGHTBLUE_EX + Style.BRIGHT +"Informe o saldo inicial de sua conta: "))
            break
        except ValueError:
            print_vermelho("Valor inválido, tente novamente!")

    tipo_conta = input("Tipo da conta(comum/plus): ").capitalize()
    while tipo_conta != "Comum" and tipo_conta != "Plus":
        tipo_conta = input("Por favor insira uma opção correta do seu tipo de conta: ").capitalize()

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
        "transacoes": [],
        "funcionarios": {}
    }  # modelo do dicionário que é salvo no arquivo .JSON

    escrever(dados)  # escreve este dicionário no arquivo .JSON

def apaga_cliente():
    # função para remover um cliente
    print("")
    cnpj = input("Digite o seu CNPJ: ")

    dados = ler()  # realiza a leitura do dicionário a partir do arquivo JSON

    if str(cnpj) in dados:
        del dados[str(cnpj)]

        escrever(dados)

        print()
        print_verde("Cliente removido com sucesso!")  # atualiza o arquivo com os valores alterados no dicionário
        print()
    else:
        print()
        print_verde("CNPJ não encontrado, tente novamente com um valor válido!")
        print()

def listar_clientes():
    # função para listar os clientes
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    dados = ler()
    print_verde("="*40)
    print()
    print_azul(Style.BRIGHT + "Clientes:")
    print()
    for cnpj, users in dados.items():
        print_azul("="*40)
        print()
        print(estilo + "Razão social:", users["razao_social"])
        print(estilo + "CNPJ:", cnpj)
        print(estilo + "Saldo:", users["saldo"])
        print(estilo + "Tipo da conta:", users["tipo_conta"])
        print(estilo + "Senha:", users["senha"])
        print()



def debito():
    dados = ler()
    
    cnpj = input("  Digite o seu CNPJ: ")
    
    if cnpj in dados:
        estilo = Fore.LIGHTGREEN_EX + Style.BRIGHT
        fim_estilo = Style.RESET_ALL         
        try:
            valor = float(input("Digite o valor que será debitado: "))  # pede ao usuário o valor que será debitado
            if dados[cnpj]["tipo_conta"] == "Plus":
                saldo_atual = dados[cnpj]["saldo"] - valor
                if saldo_atual >= -5000:
                    tarifa, valor = tarifar(valor, dados, cnpj)      
                    dados[cnpj]["saldo"] -= valor
                    historico = data_atual()
                    lista = ["Debito", valor, dados[cnpj]["saldo"],historico, tarifa]
                    dados[cnpj]["transacoes"].append(lista) # esse .append(lista) serve para adicionar as transações na conta do user, e será usado para fazer o extrato
                    print("")
                    print(estilo + "Valor debitado com sucesso, o seu saldo atual é de: " + fim_estilo + "R$", dados[cnpj]["saldo"])
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
                print_verde("Tipo de saldo inválido, tente novamente apenas com números.")    # caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
                print("")
    else:
        print("")
        print("Não foi possível encontrar o CNPJ. ")
        print("")
        

def deposito():
    dados = ler() # este comando segue a mesma logica da função débito, o programa lê o dicionario, passa para o python que faz as mudanças necessárias e logo após disso, o reescreve novamente em formato .json

    print("")
    cnpj = input("Digite o seu CNPJ: ")
    print("")
    if cnpj in dados:            
        try:
            valor = float(input("Digite o valor que será depositado: "))  # pede ao usuário o valor que será debitado
            dados[cnpj]["saldo"] += valor
            historico = data_atual()
            lista = ["Deposito", valor, dados[cnpj]["saldo"], historico]
            dados[cnpj]["transacoes"].append(lista)
            
            escrever(dados)

            print("Valor depositado com sucesso, o seu saldo atual é de:", dados[cnpj]["saldo"])
        except ValueError:      
                print("Tipo de saldo inválido, tente novamente apenas com números.")    # caso o valor esteja digitado incorretamente, o programa retorna para o usuário o erro e pede para que ele coloque novamente
    else:
        print("")
        print_verde("Não foi possível encontrar o CNPJ. ")
        print("")


def transferencia_entre_contas():
    
    dados = ler()

    cnpj = input("Digite o seu CNPJ: ")
    if validar(cnpj) == True:   # o programa valida o cnpj e a senha do usuário, e caso estejam corretos, permitem continuar a função
        destino = input("Digite o cnpj do destinatário: ")
        valor = float(input("Digite o valor da transfêrencia: "))
        if valor < dados[cnpj]["saldo"]:
            dados[cnpj]["saldo"] -= valor     # o valor é debitado da conta do remetente e adicionado à conta do destinatário, e a transação fica salva no extrato dos dois clientes envolvidos na transferência
            dados[destino]["saldo"] += valor
            historico = data_atual()
            lista = ["Transferencia", -valor, dados[cnpj]["saldo"], historico] # essa lista é a lista adicionada ao extrato
            lista_destino = ["Transferencia", valor, dados[destino]["saldo"], historico] # ^
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
                tipo, valor, saldo, data, tarifa = transacoes # aqui verifica o tamanho da lista transações e aplica a tarifa quando necessário
                print("")
                print_verde(f"Tipo: {tipo} | Valor: R$ {valor} | Tarifa: R$ {tarifa} | Saldo atual: R$ {saldo} | Data: {data}")
                print("")
            else:
                tipo, valor, saldo, data = transacoes # aqui verifica o tamanho da lista, caso não tenha uma tarifa, ele prossegue sem tarifar
                print("")
                print_verde(f"Tipo: {tipo} | Valor: R$ {valor} | Saldo atual: R$ {saldo} | Data: {data}")
                print("")

    
def verificar_cnpj(cnpj):
    dados = ler()
    for tentativas in range(3):     # o programa da 3 chances para o usuário colocar o seu cnpj correto, caso contrário, será necessário reiniciar o programa
        try:
            if cnpj in dados:
                return True
        except ValueError:
            print("CNPJ inválido, favor inserir novamente")
        else:
            return False

def data_atual():       # esta função é responsável por definir o dia e horário em que ocorreu as operações
    data_atual = datetime.datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_atual

def tarifar(valor, dados, cnpj):    # funcao responsavel por tarifar operações que necessitam de tarifas
    if dados[cnpj]["tipo_conta"] == "Plus":
        tarifa = valor*0.03
        valor += tarifa
    elif dados[cnpj]["tipo_conta"] == "Comum":
        tarifa = valor*0.05
        valor += tarifa 
    return tarifa, valor
        
        
def print_verde(texto):   # printa o texto em verde  
    print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + Style.BRIGHT + texto)
    
def print_azul(texto):    # printa o texto em azul
    print(Style.RESET_ALL + Fore.LIGHTBLUE_EX + Style.BRIGHT + texto)
    
def print_vermelho(texto): # printa o texto em vermelho
    print(Style.RESET_ALL + Fore.RED + Style.BRIGHT + texto)
    