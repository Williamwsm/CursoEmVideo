sexo = ''
contM = 0
contF = 0
while sexo != 'Z':
    print('Para sair digite "Z"')
    sexo = str(input(print('Informe o seu sexo: [M/F]'))).upper().strip()
    if sexo == 'M':
        contM += 1

    elif sexo == 'F':
        contF += 1

    elif sexo != 'F' or sexo != 'M' or sexo != 'Z':
         print('A opçao digitada esta incorreta, tenta novamente!')

    else:
        print('encerrando o programa')
print('O  numero de homens foi de: {}\nO numero de mulheres foi de: {}'.format(contM, contF))
