with open('zad3_cw4.txt', 'w') as plik:
    for i in range(4, 29, 4):
        plik.write(str(i)+'\n')
with open('zad3_cw4.txt', 'r') as plik:
    for linia in plik:
        print(linia.split('\n')[0], end=' ')