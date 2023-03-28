saque = int(input(print('Informe quanto voce deseja sacar: ')))
cont50 = cont20 = cont10 = cont1 = 0
while saque > 0:
    if saque >= 50:
        cont50 += 1
        saque -= 50
    elif saque < 50 and saque >= 20:
        cont20 += 1
        saque -= 20
    elif saque < 20 and saque >= 10:
        cont10 += 1
        saque -= 10
    else:
        cont1 += 1
        saque -= 1
print(f'Foram usadas {cont50} cedulas de R$ 50 reais \nForam usadas {cont20} cedulas de R$ 20 reais'
      f'\nForam usadas {cont10} cedulas de R$ 10 reais \nForam usadas {cont1} cedulas de 1 real')