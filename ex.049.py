opcao = ''
pessoa = []
analise = []
maiorPeso = menorPeso =0
while True:
    pessoa.append(str(input('Digite seu nome: ')))
    pessoa.append(float(input('Digite seu peso: ')))
    # recebe os maiores e menores pesos
    if len(analise) == 0:
        menorPeso = maiorPeso = pessoa[1]
    else:
        # recebe o maior peso e o nome da pessoa
        if maiorPeso < pessoa[1]:
            maiorPeso = pessoa[1]
            pMaiorPeso = pessoa[0]
        # recebe o menor peso e o nome da pessoa
        if menorPeso > pessoa[1]:
            menorPeso = pessoa[1]
            pMenorPeso = pessoa[0]
    analise.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar ? [S/N]'))
    if opcao.upper() in 'N':
        break
print(f'Voce cadastrou {len(analise)} pessoas')
print(f'O maior peso foi {maiorPeso}Kg ', end= '')
for p in analise:
    if maiorPeso == p[1]:
     print(f'[{p[0]}]',end=' ')

print(f'\nO menor peso foi {menorPeso}kg ', end= '')
for p in analise:
    if menorPeso == p[1]:
        print(f'[{p[0]}]')