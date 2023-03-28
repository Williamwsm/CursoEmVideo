from math import factorial
n = int(input(print('Imforme um numero:')))
f = n
total = factorial(n)
while f > 0:
    if f > 1:
        print('{} X '.format(f), end='')
    else:
        print('{} = '.format(f), end='')
    f -= 1
print('{}'.format(total),end='')

