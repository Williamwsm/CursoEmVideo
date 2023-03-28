num = []
impar = []
pares = []
while True:
    num.append(int(input('Digite um numero')))
    opcao = str(input('Deseja continuar? [S/N]'))
    if opcao.upper() == 'N':
        break
for i, x in enumerate(num):
    if x % 2 == 0:
        pares.append(x)
    else:
        impar.append(x)
print(f'Os numeros que voce digitou foram {num}')
print(f'Os numeros da lista que sao impares sao {impar}')
print(f'Os numeoros pares da sua lista sao {pares}')