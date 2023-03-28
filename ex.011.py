nome = str(input(print('Digite seu nome completo:'))).strip()
n = nome.split()
print('Seu primeiro nome {}'.format(n[0]))
print('Seu ultimo nome {}'.format(n[len(n)-1]))