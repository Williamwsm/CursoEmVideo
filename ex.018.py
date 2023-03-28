n = (input('Digite uma frase:')).strip().upper()
n1 = n.split()
junto = ''.join(n1)
inverso = ''
for letra in range (len(junto) -1, -1,-1):
    inverso += junto[letra]
print('O inveso da frase {} é {}'.format(junto,inverso))
if junto == inverso:
    print('A frase {} é um palindromo'.format(junto))
else:
    print(" A frase {} nao é um palindromo".format(junto))