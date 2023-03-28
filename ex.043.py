n = list()
maiorValor = menorValor = 0

for x in range (0,5):
    n.append(int(input('Digite um numero: ')))
    if x == 0:
        maiorValor = n[0]
        menorValor = n[0]
    else:
        if maiorValor < n[x]:
            maiorValor = n[x]
        if menorValor > n[x]:
            menorValor = n[x]


print(f' Os valores que voce digitou foram {n}')
print(f'O maior valor foi {maiorValor} na posiçao ', end='')
for i, x in enumerate (n):
    if x == maiorValor:
        print(f'{i}...', end='')

print(f'\nO menor valor foi {menorValor} na posicao ', end= '')
for i, x in enumerate(n):
    if x == menorValor:
        print(f'{i}...', end='')




