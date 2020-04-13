# zadanie 1
# Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne
# każdego typu a następnie wyświetl te zmienne
def zadanie_1():
    int_1 = 5
	float_1, float_2 = 7.8,3.3456
    complex_1 = 2+5j
    complex_2 = 7-45j
    string_1 = 'jakis tekscior xD'
    print('int: ', int_1)
    print('float: ', float_1, float_2)
    print('complex: ', complex_1, complex_2)
    print('string: ', string_1)

# zadanie 2
# Stwórz skrypt kalkulator, wktórym wykorzystać 
# wszystkie podstawowe działania arytmetyczne
def zadanie_2():
    a=5
    b=4
    print('dodawanie:', a, '+', b, '=', a+b)
    print('odejmowanie:', a, '-', b, '=', a-b)
    print('mnożenie:', a, '*', b, '=', a*b)
    print('dzielenie:', a, '/', b, '=', a/b)
    print('dzielenie calkowite:', a, '//', b, '=', a//b)
    print('reszta z dzielenia:', a, '%', b, '=', a%b)
    print('potegowanie:', a, 'do potegi', b, '=', a**b)
    print('potegowanie:', a, 'do potegi', b, '=', pow(a,b))

# zadanie 3
# Napisz skrypt, w którym stworzysz 
# operatory przyrostkowe dla operacji: +, -, *, /, **, %
def zadanie_3():
    print('a = 15')
    a = 5
    a += 7
    print('a += 9:', a)
    a = 5
    a -= 7
    print('a -= 55:', a)
    a = 5
    a *= 7
    print('a *= 12:', a)
    a = 5
    a /= 7
    print('a /= 7:', a)
    a = 5
    a **= 7
    print('a **= 7:', a)
    a = 5
    a %= 7
    print('a %= 7:', a)

# zadanie 4
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
from math import *

def zadanie_4():
    print('e do potegi 10 = ', pow(e, 10))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow( log(5 + pow(sin(8), 2)), 1/6))
    print('⌊3,55⌋ = ', floor(3.55))
    print('⌈4,80⌉ = ', ceil(4.80))

# zadanie 5
# Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, 
# że pierwsza litera jest wielka a pozostałe małe.(trzeba użyć metody capitalize)
def zadanie_5():
    imie = 'Paweł'
    nazwisko = 'Tracz'
    print(str.capitalize(imie), str.capitalize(nazwisko))

# zadanie 6
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu 
# piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji,
# która zliczy występowanie słowa „la”. (trzeba użyć metody count)
def zadanie_6():
    piosenka = 'eb eb eb eb eb eb'
    print('eb powtarza sie', piosenka.count('eb'), 'razy')

# zadanie 7
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
def zadanie_7():
    napis = 'przykladowy tekscior'
    print('napis =', napis)
    print('napis[1] =', napis[1])
    print('napis[1] =', napis[-1])

# zadanie 8
# Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6
# i spróbuj ją podzielić na poszczególne wyrazy.(trzeba użyć metody split)
def zadanie_8():
    piosenka = 'eb eb eb eb eb eb'
    print(str.split(piosenka))

zadanie_8()