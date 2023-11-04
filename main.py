from funcoes import *
from funcionarios import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

login()

while(True):
    operacao = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + """
=================================================
    Escolha a operação desejada:                
                                                   
    1. Novo cliente                                  
    2. Apaga cliente                                
    3. Listar clientes                                
    4. Débito                                         
    5. Depósito                                       
    6. Extrato                                        
    7. Transfêrencia entre contas                     
    8. Gerenciar Funcionários                             
    9. Sair                                          
                                                     
=================================================
    """)
    
    if operacao == "1":
        print("Operação escolhida: 1. Novo cliente")
        novo_cliente()
    elif operacao == "2":
        print("Operação escolhida: 2. Apaga cliente")
        apaga_cliente()
    elif operacao == "3":
        print("Operação escolhida: 3. Listar clientes")
        listar_clientes()
    elif operacao == "4":
        print("Operação escolhida: 4. Débito")
        debito()
    elif operacao == "5":
        print("Operação escolhida: 5. Depósito")
        deposito()
    elif operacao == "6":
        print("Operação escolhida: 6. Extrato")
        extrato()
    elif operacao == "7":
        print("Operação escolhida: 7. Transfêrencia entre contas")
        transferencia_entre_contas()
    elif operacao == "8":
        print("Operação escolhida: 8. Gerenciar Funcionários")
        menu_funcionarios()
    elif operacao == "9":
        print("Operação escolhida: 9. Sair ")
        break