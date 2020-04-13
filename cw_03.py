def zadanie_1():
    A = [1/x for x in range (1, 11, 1)]
    B=[2**x for x in range(10)]
    C=[x for x in B if x % 4 == 0]
    print(A)
    print(B)
    print(C)

import random

def zadanie_2():
    macierz = [[random.randint(0, 9) for i in range (0, 4, 1)] for j in range (0, 4, 1)]
    przekatna = [macierz[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]
    print(macierz)
    print(macierz[0])
    print('Przekątna: ',przekatna)

def zadanie_3():
    produkt_jednostka = {
        'owoce': 'kg',
        'chipsy': 'paczka',
        'sok': 'litr',
    }
    jednostka_produkt = {value: key for key, value in produkt_jednostka.items()}
    print('Oryginalny słownik:')
    print(produkt_jednostka)
    print('Odwrócony słownik:')
    print(jednostka_produkt)

def monotonicznosc(a):
    if(a>0):
        return 'Jest rosnąca'
    if(a<0):
        return 'Jest malejąca'
    if(a==0):
        return 'Jest stała'
def zadanie_4():
    print('y = ax + b')
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print('Funkcja y = '+str(a)+'x + '+str(b)+' jest '+str(monotonicznosc(a)))       

def proste_czy_rownolegle(a1, a2):
    if(a1 == a2):
        return 'równoległe'
    if(a1*a2 == -1):
        return 'prostopadłe'
    else:
        return 'ani równoległe ani prostopadłe'
def zadanie_5():
    print('y = ax + b')
    a1 = float(input('Podaj a1: '))
    b1 = float(input('Podaj b1: '))
    a2 = float(input('Podaj a2: '))
    b2 = float(input('Podaj b2: '))
    print('y1 = '+str(a1)+'x + '+str(b1))
    print('y2 = '+str(a2)+'x + '+str(b2))
    print('Proste y1 i y2 są '+str(proste_czy_rownolegle(a1, a2)))  

def okrag(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2 + (y-b)**2)**0.5

def zadanie_6():
    print('Współrzędne środka okręgu to (a,b)')
    a = input('Podaj współrzędną a: ')
    b = input('Podaj współrzędną b: ')
    print('Do okręgu należy punkt o współrzędnych (x,y)')
    x = input('Podaj współrzędną x: ')
    y = input('Podaj współrzędną y: ')
    print('Promień okręgu ma długość równą:',okrag(float(a), float(b), float(x), float(y)))

def pitagoras(a = 0, b = 0):
    return (a**2 + b**2)**0.5

def zadanie_7():
    a = float(input('Podaj dłguość pierwszej przyprostokątnej: '))
    b = float(input('Podaj dłguość drugiej przyprostokątnej: '))
    print('Długość przeciwprostokątnej wynosi: '+str(pitagoras(a,b)))

def ciag_suma(a1 = 1, r = 1, ile = 10):
    return ile * ((2*a1) + (ile-1)*r) / 2

def zadanie_8():
    a1 = float(input('Podaj a1: '))
    r = float(input('Podaj r: '))
    ile = int(input('Podaj ile: '))
    print('suma = ',str(ciag_suma(a1, r, ile)))

def ilosc_produnktow(**lista_zakupow):
    suma = 0.0
    for i in lista_zakupow:
        suma = suma + float(lista_zakupow[i])
    return suma

def zadanie_10():
    print('liczba wszystkich produktów:', ilosc_produnktow(soczek=1,olowek=2,
          plyta_cd=5))
zadanie_10()   

