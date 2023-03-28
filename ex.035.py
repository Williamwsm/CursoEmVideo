total = cont = baixoValor =0
produtoBarato =''
produto = str(input(print('Informe o produto que vc comprou: '))).strip()
valor = float(input(print('Informe o valor deste produto:')))
baixoValor = valor
while True:
    total+= valor
    if valor < baixoValor:
        produtoBarato = produto
    if valor > 1000:
        cont+=1
    opcao = str(input(print('Deseja continuar? [S/N]'))).strip().upper()
    if opcao == 'N':
        break
    produto = str(input(print('Informe o produto que vc comprou: '))).strip()
    valor = float(input(print('Informe o valor deste produto:')))
print(f'O valor total dos produtos foi: {total:.2f} reais \nO produto mais barato foi o: {produtoBarato}')
print(f'O numero de produtos que custaram acima de R$ 1000,00 foi de: {cont} produtos')