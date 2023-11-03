from funcoes import ler, escrever, validar, data_atual, print_verde, input_verde, print_vermelho, verificar_cnpj
from colorama import Fore, Style


def menu_funcionarios():
    dados = ler()
    estilo = Fore.LIGHTGREEN_EX + Style.BRIGHT
    while True:
        try:
            print("")
            cnpj = int(input(estilo + "CNPJ: "))
            cnpj = str(cnpj)
            if len(cnpj) == 3:
                for contas in dados.keys():
                    if cnpj in contas:
                        while True:
                            operacao = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + """
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
                                print("Operação 1 selecionada.")
                            if operacao == "2":
                                print("Operação 2 selecionada.")
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


def cadastro_funcionario():
    dados = ler()
    estilo = Fore.LIGHTGREEN_EX + Style.BRIGHT
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

    while(True):
        try:
            saldo = float(input_verde("Informe o saldo inicial de sua conta: "))
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

    dados[cnpj]["funcionarios"][cpf] = {
            "nome": nome,
            "saldo" : saldo,
            "transacoes": [],
        }       # esse é o modelo do dicionario que consta no arquivo .json
        
    escrever(dados) # com esse comando, esse dicionario é escrito no json dessa maneira




    
