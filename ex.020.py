maiorPeso = 0
menorPeso = 0
for x in range (0,5):
    peso= float(input(print('Informe o seu peso:')))
    if x == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso> maiorPeso:
         maiorPeso = peso

        if peso< menorPeso:
         menorPeso = peso
print('Maior peso dentre as pessoas é: {}\nMenor peso dentre as pessoas é: {}'.format(maiorPeso,menorPeso))