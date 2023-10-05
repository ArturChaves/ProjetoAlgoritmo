from funcoes import *

while(True):
    operacao = input("""
    1. Novo cliente 
    2. Apaga cliente
    3. Listar clientes
    4. Débito
    5. Depósito
    6. Extrato
    7. Transfêrencia entre contas
    8. Operação a definir
    9. Sair
                     
    Escolha um tipo de operação: """)
    
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
        operacao_livre()
    elif operacao == "9":
        break