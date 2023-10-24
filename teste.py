dados = {
    'pessoa1': {
        'nome': 'Alice',
        'idade': 30
    },
    'pessoa2': {
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
        arquivo.write(f'Pessoa: {pessoa}\n')
        # Percorra as chaves e valores dos dicionários internos (nome e idade)
        for chave, valor in info.items():
            arquivo.write(f'{chave}: {valor}\n')
        arquivo.write('\n')  # Adicione uma linha em branco entre cada pessoa
        
with open('dados.txt', 'r') as arquivo:
    # Leia o arquivo linha por linha
    for linha in arquivo:
        # Divida a linha em palavras separadas por dois pontos (':')
        partes = linha.strip().split(': ')
        # Verifique se a primeira parte da linha é "nome" e a segunda parte é "Bob"
        if len(partes) == 2 and partes[0] == 'nome' and partes[1] == 'Bob':
            # Quando encontrar o nome "Bob", leia a próxima linha (idade)
            idade = next(arquivo).strip()
            print(f'A idade de Bob é: {idade}')
            break  # Pare a busca após encontrar a informação desejada