while True:
    n = int(input(print('voce deseja saber a tabuada de qual valor? ')))
    if n < 0:
        print('Encerrando o programa')
        break
    for cont in range(0, 11, +1):
        print(f' {n} X {cont} = {n*cont}')
