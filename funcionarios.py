from funcoes import ler, escrever, validar, data_atual, print_verde, input_verde, print_vermelho, verificar_cnpj, verificar_cpf, print_azul
from colorama import Fore, Style, init
init(autoreset=True)
import json

def menu_funcionarios():
    dados = ler()
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    while True:
        try:
            print("")
            cnpj = int(input(estilo + "CNPJ: "))
            cnpj = str(cnpj)
            if len(cnpj) == 3 and verificar_cnpj(cnpj) == True:
                for contas in dados.keys():
                    if cnpj in contas:
                        while True:
                            operacao = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + """
=================================================
    Escolha a operação desejada:                
                                                                                    
    1. Cadastrar funcionário                                  
    2. Remover funcionário
    3. Listar funcionários
    4. Pagar funcionários
    5. Sair 
=================================================
""")
                            if operacao == "1":
                                cadastro_funcionario(cnpj)
                            if operacao == "2":
                                apaga_funcionario()
                            if operacao == "3":
                                print("Operação 3 selecionada.")
                            if operacao == "4":
                                print("Operação 4 selecionada.")
                            if operacao == "5":
                                break  # Sair do loop interno
                        break  # Sair do loop externo
                break
        except ValueError:
            print_vermelho("CNPJ inválido")
            break


def cadastro_funcionario(cnpj):
    dados = ler()
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    while(True):
        try:
            print("")
            cpf = int(input(estilo + "CPF: "))
            cpf = str(cpf)
            validacao_cpf = True
            if len(cpf) == 3:      # aqui faz a comparação para saber o tamanho do cpf, caso seja 14, está liberado para continuar as proximas etapas
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
            print_vermelho("CPF invalido")
        
    
        

    nome = input("Nome: ")

    saldo = None
            
    while(True):
        try:
            salario = float(input(f"{estilo}Informe o salário de {nome}: "))
            break
        except ValueError:
            print_vermelho("Valor inválido, tente novamente!")

    dados[cnpj]["funcionarios"][cpf] = {
            "nome": nome,
            "saldo" : saldo,
            "salario": salario,
            "transacoes": [],
        }       # esse é o modelo do dicionario que consta no arquivo .json
        
    escrever(dados) # com esse comando, esse dicionario é escrito no json dessa maneira
    print()
    print_verde(f"O funcionário {nome} foi cadastrado com sucesso!")

def apaga_funcionario():
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    dados = ler()
    print()
    cnpj = int(input(estilo + "CNPJ: "))
    cnpj = str(cnpj)
    
    if verificar_cnpj(cnpj):
        cpf = int(input(estilo + "CPF: "))
        cpf = str(cpf)
        
        if verificar_cpf(cpf, cnpj):
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