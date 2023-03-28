expressao = str(input('Digite uma expressao: '))
lista = []
for x in expressao:
    if x == '(':
        lista.append('(')
    elif x == ')':
       if len(lista)< 0:
           lista.pop()
       else:
           lista.append(')')
           break
if len(lista) == 0:
    print('Sua expressao esta correta')
else:
    print(' Sua expressao esta incorreta')