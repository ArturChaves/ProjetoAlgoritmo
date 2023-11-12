from funcoes import *
from funcionarios import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

login()

estilo_azul = Style.RESET_ALL + Fore.CYAN + Style.BRIGHT
estilo_branco = Style.RESET_ALL + Fore.LIGHTWHITE_EX

while(True):
    operacao = input( estilo_azul + """
 _________________________________________________
|                                                 |
|   Escolha a operação desejada:                  |
|_________________________________________________| 
|                                                 | 
|    1. Novo cliente                              |   
|    2. Apaga cliente                             |  
|    3. Listar clientes                           |    
|    4. Débito                                    |     
|    5. Depósito                                  |     
|    6. Extrato                                   |    
|    7. Transfêrencia entre contas                |    
|    8. Gerenciar Funcionários                    |        
|    9. Sair                                      |   
|_________________________________________________|                                                  

    """ + estilo_branco)
    
    if operacao == "1":
        print()
        print(estilo_azul + "Operação escolhida: 1. Novo cliente")
        novo_cliente()
    elif operacao == "2":
        print()
        print(estilo_azul + "Operação escolhida: 2. Apaga cliente")
        apaga_cliente()
    elif operacao == "3":
        print()
        print(estilo_azul + "Operação escolhida: 3. Listar clientes")
        listar_clientes()
    elif operacao == "4":
        print()
        print(estilo_azul + "Operação escolhida: 4. Débito")
        debito()
    elif operacao == "5":
        print()
        print(estilo_azul + "Operação escolhida: 5. Depósito")
        deposito()
    elif operacao == "6":
        print()
        print(estilo_azul + "Operação escolhida: 6. Extrato")
        extrato()
    elif operacao == "7":
        print()
        print(estilo_azul + "Operação escolhida: 7. Transfêrencia entre contas")
        transferencia_entre_contas()
    elif operacao == "8":
        print()
        print(estilo_azul + "Operação escolhida: 8. Gerenciar Funcionários")
        menu_funcionarios()
    elif operacao == "9":
        print()
        print(estilo_azul + "Operação escolhida: 9. Sair ")
        break