class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = float(ilosc)
        self.jednostka_miary = jednostka_miary
        self.cena_jed = float(cena_jed)
    def wyswietl_produkt(self):
        print('nazwa produktu: '+str(self.nazwa_produktu))
        print('ilość produktu: '+str(self.ilosc))
        print('jednostka miary: '+str(self.jednostka_miary))
        print('cena jednostkowa: '+str(self.cena_jed))
    def ile_produktu(self):
        return str(self.ilosc)+' '+str(self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

obiekt = NaZakupy('Grzyb Tue',3,'szt', 75)
obiekt.wyswietl_produkt()
print('ilosc: '+obiekt.ile_produktu())
print('koszt: '+str(obiekt.ile_kosztuje())+' PLN')