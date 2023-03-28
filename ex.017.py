primeiro = int(input(print('Informe o primeiro termo: ')))
razao = int(input(print('Informe a razao:')))
decimo = primeiro+(10-1)*razao
for x in range(primeiro, decimo + razao, razao):
    print(x)
