n = soma = cont = 0
print('Digite [999] para finalizar ')
n = int(input(print('Informe um numero: ')))
while n != 999:
    cont+=1
    n = int(input(print('Informe um numero: ')))
    soma += n
    if n == 999:
        soma -= 999
print('A soma total é: {}, o total de numero digitados é {}'.format(soma, cont))