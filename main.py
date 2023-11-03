from funcoes import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

login()

while(True):
    operacao = input( Fore.LIGHTGREEN_EX + Style.BRIGHT +"""
=================================================
    Escolha a operação desejada:                
                                                   
    1. Novo cliente                                  
    2. Apaga cliente                                
    3. Listar clientes                                
    4. Débito                                         
    5. Depósito                                       
    6. Extrato                                        
    7. Transfêrencia entre contas                     
    8. Operação a definir                             
    9. Sair                                          
                                                     
=================================================
    """)
    
    if operacao == "1":
        novo_cliente()
    elif operacao == "2":
        apaga_cliente()
    elif operacao == "3":
        listar_clientes()
    elif operacao == "4":
        debito()
    elif operacao == "5":
        deposito()
    elif operacao == "6":
        extrato()
    elif operacao == "7":
        transferencia_entre_contas()
    elif operacao == "8":
        gerenciar_funcionarios()
    elif operacao == "9":
        break