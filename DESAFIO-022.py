# Um programa que mostra qual o primeiro e último nome de uma pessoas #

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer {n}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')










