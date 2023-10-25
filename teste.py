dados = {
    'pessoa1': {
        'cnpj': '123',
        'nome': 'Alice',
        'idade': 30
    },
    'pessoa2': {
        'cnpj': '321',
        'nome': 'Bob',
        'idade': 25
    },
    'pessoa3': {
        'nome': 'Charlie',
        'idade': 35
    }
}

with open('dados.txt', 'w') as arquivo:
    # Percorra as chaves do dicionário principal (neste caso, as pessoas)
    for pessoa, info in dados.items():
        arquivo.write(f'pessoa: {pessoa}\n')
        # Percorra as chaves e valores dos dicionários internos (nome e idade)
        for chave, valor in info.items():
            arquivo.write(f'{chave}: {valor}\n')
        arquivo.write('\n')  # Adicione uma linha em branco entre cada pessoa


cnpj = input("Digite seu cnpj: ")     
with open('dados.txt', 'r') as arquivo:
    # Leia o arquivo linha por linha
    for linha in arquivo:
        partes = linha.strip().split(': ')
    
        if len(partes) == 2 and partes[0] == 'cnpj' and partes[1] == cnpj:
            if len(partes) == 2 and partes[0] == 'cnpj':
                print(partes[1])
            elif len(partes) == 2 and partes[0] == 'nome':
                print(partes[1])
            elif len(partes) == 2 and partes[0] == 'idade':
                print(partes[1])
        
            
        