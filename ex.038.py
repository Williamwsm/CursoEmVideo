times = ('corinthians', 'palmeniras', 'santos' , 'gremio', 'cruzeiro', 'flamengo', 'vasco', 'chapecoense'
     , 'atletico', 'botafogo', 'atletico-pr','bahia', 'sao paulo' , 'fluminense', 'sport recife', 'ec vitoria'
    ,'coritiba', 'avaí', 'ponte preta', 'atletico-go')

print(f'Os 5 primeiros colocados sao: {times[0:5]}')
print(f'\nOs ultimoos 4 colocados sao: {times [-4:]} ')
print(f'\nEm ordem alfabetica: {sorted(times)}')
print(f'\nA chapecoense ficou na posiçao : {times.index("chapecoense")+1}')

