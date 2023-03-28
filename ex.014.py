numero = int(input(print('Informe um numero pra a conversao: ')))
print('escolha uma opçao:')
opcao = int(input(print('[1] - binario\n[2] - octa\n[3] - hexadecimal')))
if opcao == 1:
    print('O numero {}, convertido para binario é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O numero {}, convertido para octadecimal é igual a {}'.format(numero, oct(numero)))

elif opcao== 3:
    print('O numero {}, convertido para hexadecimal é igual a {}'.format(numero, hex(numero)))

else:
    print('Opcao invalida!!')