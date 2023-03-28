n = (int (input('Digite um numero: ')),int (input('Digite um numero: ')),int (input('Digite um numero: ')),int (input('Digite um numero: ')))
print(f'O numero "9" apareceu {n.count(9)} vezes ')
if 3 in n:
    print(f'O valor "3" apareceu primeiro na posicao {n.index(3)}')
else:
    print('O numero "3" nao apareceu na lista ')
print('Os numeros pares digitados sao:', end= '')
for num in  n:
    if num %2 == 0:
        print(f' {num}', end= '')
