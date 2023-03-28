palavras = ('Aprender', 'Programar', 'Liguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Programador', 'Futuro')
for letras in palavras:
    print(f'\nNa palavra {letras.upper()} possui as seguintes vogais:',end='')
    for vogais in letras:
        if vogais.lower() in 'a e i o u':
            print(vogais.lower(), end=' ')