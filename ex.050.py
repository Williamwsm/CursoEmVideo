numeros = [[],[]]
for x in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(numeros)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros impares sao {numeros[1]}'
      f'')
print(f'Os numeros pares sao {numeros[0]}')