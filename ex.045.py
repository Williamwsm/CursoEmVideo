n = []
for x in range (0,5):
    num = int(input('Digite um numero: '))
    if x == 0 or num > n[-1]:
        n.append(num)
    else:
        pos = 0
        while pos < len(n):
            if num <= n[pos]:
                n.insert(pos , num)
                break
            pos += 1

print(f'Os numeros que voce digitou foram {n}')