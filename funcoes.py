def novo_cliente():
    razao_social = input("Digite a sua razão social: ")
    cnpj = input("Digite o seu CNPJ: ")
    tipo_conta = input("Qual o seu tipo de conta? (comum/plus): ")
    valor_inicial = float(input("Digite o seu valor inicial: "))
    senha_usuario = input("Digite sua senha: ")
    print("Razão social:", razao_social)
    print("CNPJ:", cnpj)
    print("Tipo da conta: ",tipo_conta)
    print("Valor inicial:", valor_inicial)
    print("Senha:", senha_usuario)

def apaga_cliente():
    cnpj = input("Digite o seu CNPJ: ")
    print(cnpj)

def debito():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    valor = float(input("Digite o valor que será debitado: "))
    print(cnpj)
    print(senha)
    print(valor)

def deposito():
    cnpj = input("Digite o seu CNPJ: ")
    valor = float(input("Digite o valor que será debitado: "))
    print(cnpj)
    print(valor)

def extrato():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    print("Aqui será mostrado o extrato do cliente")

def listar_clientes():
    print("Aqui serão mostradas as informações dos clientes")

def operacao_livre():
    print("Essa função será decidida no futuro")

def transferencia_entre_contas():
    cnpj = input("Digite o seu CNPJ: ")
    senha = input("Digite sua senha: ")
    cnpj_destino = input("Digite o CNPJ de destino: ")
    valor = float(input("Digite o valor: "))
    print(cnpj)
    print(senha)
    print(cnpj_destino)
    print(valor)
