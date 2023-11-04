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
    4. Alterar Salario
    5. Pagar funcionários
    6. Sair 
=================================================

""")
                            if operacao == "1":
                                cadastro_funcionario(cnpj)
                            if operacao == "2":
                                apaga_funcionario()
                            if operacao == "3":
                                listar_funcionarios()                                
                            if operacao == "4":
                                alterar_salario()
                            if operacao == "5":
                                print("Operação 4 selecionada.")
                            if operacao == "6":
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

def listar_funcionarios():
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    dados = ler()
    cnpj = input(estilo + "Informe o CNPJ: ")
    if cnpj in dados:
        funcionarios = dados[cnpj]["funcionarios"]
        print_verde("="*40)
        print()
        print_azul(Style.BRIGHT + "Clientes:")
        print()
        for cpf, dados_funcionario in funcionarios.items():
            print_azul("="*40)
            print()
            print(estilo + "Nome:", dados_funcionario["nome"])
            print(estilo + "CPF:", cpf)
            print(estilo + "Saldo:", dados_funcionario["saldo"])
            print(estilo + "Tipo da conta:", dados_funcionario["salario"])
            print()
        return cnpj
    else:
        print_vermelho(Style.BRIGHT + "CNPJ invalido, favor inserir novamente")


def alterar_salario():
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    dados = ler()
    cnpj = listar_funcionarios()
    funcionarios = dados[cnpj]["funcionarios"]
    while(True):
        cpf = input(estilo + "Informe o cpf do colaborador para alterar seu salário: ").capitalize()
        if cpf in funcionarios.keys():
            try:
                novo_salario = float(input(estilo + "Informe o novo salário do colaborador: "))
                funcionarios[cpf]["salario"] = novo_salario
                escrever(dados)
                print_verde("Salário alterado com sucesso")

            except ValueError:
                print_vermelho("Valor invalido de salario, tente novamente.")
        else:
            print_vermelho("Funcionario não encontrado, favor tentar novamente")
def pagar_funcionarios():
    estilo = Fore.LIGHTBLUE_EX + Style.BRIGHT
    dados = ler()