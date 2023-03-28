nome = str(input(print('Informe o seu nome: '))).strip().upper()
print('A primeira letra A apareceu {} vezes'.format(nome.count("A")))
print('A letra A apareceu na posicao {}'.format(nome.find("A")+1))
print('A letra A apareceu por ultimo na posiçao {}'.format(nome.rfind("A")+1))