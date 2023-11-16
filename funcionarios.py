from funcoes import ler, escrever, validar, data_atual, print_verde, print_vermelho, verificar_cnpj, verificar_cpf, print_azul
from colorama import Fore, Style, init
init(autoreset=True) # esse comando é para iniciar o colorama, que permite alterar o estilo das letras
import json # biblioteca utilizada para armazenar os dados 

def menu_funcionarios(): #incializa o menu funcionarios setando suas cores e condicionando suas respostas
    dados = ler()
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT # Setando estilos das cores 
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX # Setando estilo da digitação no terminal
    while True:
        try: # Validação do CNPJ para acessar o menu
            print("")
            cnpj = int(input(estilo_azul + "CNPJ: " + estilo_branco))
            cnpj = str(cnpj)
            if len(cnpj) == 14 and verificar_cnpj(cnpj) == True:
                for contas in dados.keys():
                    if cnpj in contas:
                        while True:
                            operacao = input(estilo_azul+ """

 _______________________________________________
|                                               |
|    Escolha a operação desejada:               |
|                                               |                                   
|    1. Cadastrar funcionário                   |              
|    2. Remover funcionário                     |
|    3. Listar funcionários                     |
|    4. Alterar salário                         |
|    5. Pagar funcionários                      |
|    6. Sair                                    |
|_______________________________________________| """ + estilo_branco + """

""")
                            if operacao == "1":
                                print()
                                print(estilo_azul + "Operação escolhida 1. Cadastrar funcionário")
                                cadastro_funcionario(cnpj)
                            if operacao == "2":
                                print()
                                print(estilo_azul + "Operação escolhida 2. Remover funcionário")
                                apaga_funcionario()
                            if operacao == "3":
                                print()
                                print(estilo_azul + "Operação escolhida 3. Listar funcionários")
                                listar_funcionarios()                                
                            if operacao == "4":
                                print()
                                print(estilo_azul + "Operação escolhida 4. Alterar salário")
                                alterar_salario()
                            if operacao == "5":
                                print()
                                print(estilo_azul + "Operação escolhida 5. Pagar funcionários")
                                menu_pagamento()
                            if operacao == "6":
                                print()
                                print(estilo_azul + "Operação escolhida 6. Sair")
                                break  # Sair do loop interno
                        break  # Sair do loop externo
                break
        except ValueError:
            print_vermelho("CNPJ inválido")
            break


def cadastro_funcionario(cnpj):
    dados = ler()
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT # Setando estilos das cores
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX # Setando estilo da digitação no terminal
    while(True):
        try:
            print("")
            cpf = int(input(estilo_azul + "CPF: " + estilo_branco))
            cpf = str(cpf)
            validacao_cpf = True
            if len(cpf) == 11:      # aqui faz a comparação para saber o tamanho do cpf, caso seja 11, o cliente estará liberado para continuar as proximas etapas
                for contas in dados.keys():
                    if cpf in contas:
                        validacao_cpf = False
                    else:
                        break
                if validacao_cpf == False:
                    print_vermelho("Já existe uma conta cadastrada com esse CPF, tente novamente!")
                else:
                    break
            else:
                print_vermelho("Valor inválido, tente novamente!")
        except ValueError:
            print_vermelho("CPF inválido")
        
    
        

    nome = input(estilo_azul + "Nome: " + estilo_branco)

    saldo = 0
            
    while(True): #Loop feito para cadastrar um salário valido 
        try:
            salario = float(input(f"{estilo_azul}Informe o salário de {nome}: {estilo_branco} "))
            break
        except ValueError:
            print_vermelho("Valor inválido, tente novamente!")

    dados[cnpj]["funcionarios"][cpf] = {
            "nome": nome,
            "saldo" : saldo,
            "salario": salario,
            "pagamentos": [],
        }       # esse é o modelo do dicionario que consta no arquivo .json para o cadastro dos funcionários
        
    escrever(dados) # com esse comando, esse dicionario é escrito no json dessa maneira
    print()
    print_verde(f"O funcionário {nome} foi cadastrado com sucesso!")

def apaga_funcionario():
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX
    dados = ler()
    print()
    cnpj = int(input(estilo_azul + "CNPJ: " + estilo_branco))
    cnpj = str(cnpj)
    
    if verificar_cnpj(cnpj): #Caso o CNPJ for valido, então o programa pergunta o CPF do funcionário no qual será removido
        cpf = int(input(estilo_azul + "CPF: " + estilo_branco))
        cpf = str(cpf)
        
        if verificar_cpf(cpf, cnpj): #Se a verificação for verdadeira, então o funcionário é deletado
            del dados[cnpj]["funcionarios"][cpf]
            escrever(dados)
            print()
            print_verde(f"O funcionário portador do CPF: {cpf} foi deletado com sucesso")
        else:
            print()
            print_vermelho("Não existe funcionário com esse CPF para este CNPJ")
    else:
        print()
        print_vermelho("CNPJ não encontrado")

def listar_funcionarios():
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX
    dados = ler()
    try:
        cnpj = input(estilo_azul + "Informe o CNPJ: " + estilo_branco)
        if cnpj in dados:
            funcionarios = dados[cnpj]["funcionarios"]
            print_azul("="*40)
            print()
            print_azul(Style.BRIGHT + "Funcionários:")
            print() 
            for cpf, dados_funcionario in funcionarios.items(): # faz a iteração sobre os dados dos funcionários
                print_azul("="*40)
                print()
                print(f'{estilo_azul} Nome: {estilo_branco}{dados_funcionario["nome"]}')
                print(f'{estilo_azul} CPF: {estilo_branco} {cpf}')
                print(f'{estilo_azul} Saldo: {estilo_branco} {dados_funcionario["saldo"]}')
                print(f'{estilo_azul} Salário: {estilo_branco} {dados_funcionario["salario"]}')
                print()
            return cnpj
        else:
            print_vermelho(Style.BRIGHT + "CNPJ invalido, favor inserir novamente")
    except ValueError:
        print_vermelho("Coloque um valor válido para o CNPJ")


def alterar_salario():
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX
    dados = ler()
    cnpj = listar_funcionarios()  # os funcionarios sao listados para um acesso mais e facil e rapido dos dados
    if cnpj == None:
        return
    funcionarios = dados[cnpj]["funcionarios"]
    while(True):
        cpf = input(estilo_azul + "Informe o cpf do colaborador para alterar seu salário: " + estilo_branco)
        if cpf in funcionarios.keys():
            try:
                novo_salario = float(input(estilo_azul + "Informe o novo salário do colaborador: " + estilo_branco))
                funcionarios[cpf]["salario"] = novo_salario 
                escrever(dados)
                print_verde("Salário alterado com sucesso")
                break

            except ValueError:
                print_vermelho("Valor invalido de salario, tente novamente.") 
        else:
            print_vermelho("Funcionario não encontrado, favor tentar novamente")
            
def menu_pagamento():
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX
    dados = ler()
    
    cnpj = input(estilo_azul + "Digite o CNPJ: " + estilo_branco)
    if validar(cnpj) == True:
        while(True):
            operacao_pagamento = input(estilo_azul + """

 _______________________________________________
|                                               |
|    Informe a operação:                        |
|                                               |                                   
|    1. Pagar funcionarios                      |            
|    2. Extrato dos pagamentos                  |
|    3. Sair                                    |
|_______________________________________________| """ + estilo_branco + """

""")
            if operacao_pagamento == "1":
                print()
                print(estilo_azul + "Operação escolhida 1. Pagar funcionários")
                pagar_funcionarios(cnpj)
            if operacao_pagamento == "2":
                print()
                print(estilo_azul + "Operação escolhida 2. Extrato dos pagamentos")
                extrato_pagamentos(cnpj)
            if operacao_pagamento == "3":
                print()
                print(estilo_azul + "Operação escolhida 3. Sair")
                break
    else:
        print("")
        print_vermelho("Usuário não cadastrado, tente novamente.")

def pagar_funcionarios(cnpj):
    dados = ler()
    funcionarios = dados[cnpj]["funcionarios"] 
    pagamento_total = 0 #Inicializa uma variavel com a finalidade de contar o valor total do pagamento dos funcionários

    for salario in funcionarios.values():
        pagamento_total += salario["salario"] #Conatabiliza os salários do cnpj dentro de pagamento total

    if dados[cnpj]["tipo_conta"] == "Plus": #Verifica o tipo de conta do CNPJ para identificar seu limite de crédito
        saldo_pagador = dados[cnpj]["saldo"] + 5000 #O saldo total do CNPJ é somado com seu limite de crédito caso seja necessário utilizar do crédito para realizar o pagamento
        if saldo_pagador > pagamento_total:
            pagar(cnpj)
            print_azul("Pagamento realizado com sucesso")
        else: #Se o valor ultrapassar o saldo limite do pagador, não é possivel realizar o pagamento
            print_vermelho("Não é possivel realziar pagamento. O valor ultrapassa seu saldo")
 
    elif dados[cnpj]["tipo_conta"] == "Comum": #Verifica o tipo de conta do CNPJ para identificar seu limite de crédito
        saldo_pagador = dados[cnpj]["saldo"] + 1000 #O saldo total do CNPJ é somado com seu limite de crédito caso seja necessário utilizar do crédito para realizar o pagamento
        if saldo_pagador > pagamento_total:
            pagar()
            print_azul("Pagamento realizado com sucesso")
        else: #Se o valor ultrapassar o saldo limite do pagador, não é possivel realizar o pagamento
            print_vermelho("Não é possivel realziar pagamento. O valor ultrapassa seu saldo")
        
def pagar(cnpj):
    dados = ler()
    funcionarios = dados[cnpj]["funcionarios"] #Seta uma variavel para melhor manipulção dos dados
    for salario in funcionarios.values(): #Verifica o salário de cada funcionário 
        dados[cnpj]["saldo"] -= salario["salario"] #O valor do salário é feito por um débito no CNPJ 
        salario["saldo"] += salario["salario"] #O saldo recebe o valor debitado do CNPJ 
        historico = data_atual()
        lista = ["Pagamento", -salario["salario"], dados[cnpj]["saldo"], historico] #Estruturando os dados do cnpj para serem devolvidos em "dados.json" após alteração
        lista_destino = ["Recebimento", salario["salario"], salario["saldo"], historico] #Estruturando os dados do funcionário para serem devolvidos em "dados.json" após alteração
        dados[cnpj]["transacoes"].append(lista) 
        salario["pagamentos"].append(lista_destino) 
        escrever(dados) # Devolve esses valores escrevendo os mesmos dentro do nosso arquivo JSON

def extrato_pagamentos(cnpj):
    estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
    estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX
    dados = ler()
    funcionarios = dados[cnpj]["funcionarios"] #Seta uma variavel para melhor manipulção dos dados
    
    for funcionario_cpf, funcionario in funcionarios.items(): #Um laço é feito para verificar o conteudo de cada funcionário cadastrado
        print(f"{estilo_azul}Extrato de pagamentos para o  {funcionario['nome']} - {funcionario_cpf}: {estilo_branco}")
        for pagamento in funcionario["pagamentos"]:
            tipo, valor, saldo, data = pagamento
            print("")
            print(f"{estilo_azul}Tipo: {estilo_branco}{tipo} | {estilo_azul} Valor: R$ {estilo_branco} {valor} |{estilo_azul} Saldo atual: R$ {estilo_branco} {saldo} |{estilo_azul} Data:{estilo_branco} {data}")
            print("")
        print("___________________________________________________________________________")



