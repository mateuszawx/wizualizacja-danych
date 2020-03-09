# Zad. 1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie
# (użyj instrukcji input)
import sys


def zadanie_1():
    print("Przykladowy tekst xD")
    tekst = sys.stdin.readline()
    print('W zdaniu spacja pojawia sie:', tekst.count(' '))


def zadanie_2():
    print("Podaj pierwsza liczbe")
    liczba_1 = sys.stdin.readline()
    print("Podaj druga liczbe")
    liczba_2 = sys.stdin.readline()
    sys.stdout.write(str(float(liczba_1)*float(liczba_2)))

def zadanie_4():
    liczba = input("Podaj liczbe byku: ")
    liczba = int(liczba)
    if liczba <= 0:
        print('|', liczba, '|=', liczba*(-1))
    else:
        print('|', liczba, '|=', liczba)

def zadanie_5():
    a = input("Podaj liczbe a: ")
    b = input("Podaj liczbe b: ")
    c = input("Podaj liczbe c: ")
    a = int(a)
    b = int(b)
    c = int(c)
    if a > 0 and a <= 10:
        print("a jest z przedzialu (0,10>")
    if a > b or b > c:
        print ("Warunek a > b lub b > c jest spelniony")
    else:
        print("Warunek a > b lub b > c NIE jest spelniony")

def zadanie_6():
    for dzielniki in range (0, 201, 5):
        print(str(dzielniki), end=" ")

def zadanie_7():
    lista = []
    for licznik in range (0, 3, 1):
        liczba = input("Podaj liczbe: ")
        lista.append(int(liczba))
    for licznik in range (0, 3, 1):
        print(str(lista[licznik])+'^2 = '+str(lista[licznik]**2))

def zadanie_8():
    lista = []
    i = 0
    while i < 3:
        liczba = input("Podaj liczbe: ")
        lista.append(int(liczba))
        i+=1
    print(lista)

def zadanie_9():
    liczba = int(input("Podaj liczbe byku: "))
    suma = 0
    while(liczba != 0):
        suma = suma + liczba % 10
        liczba = liczba // 10
    print("Suma cyfr: " +str(suma))     

zadanie_9()

