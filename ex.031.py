soma = cont = 0
while True:
    print('Digite [ 999 ] para sair')
    n = int(input(print('Digite um numero: ')))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma total dos numeros foi {soma}, e o total de numeros digitados foi {cont}')
