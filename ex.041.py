produtos =('Lapis',1.75,
           'Borracha',2,
           'Caderno',15.90,
           'Estojo', 25,
           'Transferidor',4.20,
           'Compasso',9.99,
           'Mochila',120.32,
           'Canetas',22.30,
           'Livro', 34.90)
for item in range(0, len(produtos)):
    if item %2 ==0 :
        print(f'{produtos[item]:.<30} R$ ', end='')

    else:
        print(f'{produtos[item]:.2f}')
