
class Student:
    def __init__(self, imie, nazwisko, numindesku):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numindeksu = numindesku
        self.indeks = []
    def __str__(self):
        return f"Imie: {self.imie}, Nazwisko: {self.nazwisko}, Numer albumu: {self.numindeksu}"

    def dodaj_ocene(self, nowa_ocena):
        self.indeks.append(nowa_ocena)

    def przedstaw_sie(self):
        print(f"Cześć nazwyam sie {self.imie}")

    def srednia_ocen(self):
        srednia = 0
        if self.indeks:
            srednia = sum(self.indeks)/len(self.indeks)
        print(srednia)

student1 = Student("OLA", "Wojewoda", 12334)
print(student1)

student1.dodaj_ocene(5.0)
student1.dodaj_ocene(4.0)
student1.dodaj_ocene(2.0)

student1.srednia_ocen()



# Zafanie domowe

class Pamietnik:
    def __init__(self, kolor, wlasciciel, pin_do_klodeczki, ilosc_stron):
        self.kolor = kolor
        self.wlasciciel = wlasciciel
        self.haslo = pin_do_klodeczki
        self.ilosc_stron = ilosc_stron
        self.zawartosc_stron = {strona+1: [] for strona in range(ilosc_stron)}
        self.czy_otwarty = False
        self.pin = pin_do_klodeczki

    def __str__(self):
        return f"{self.wlasciciel}, {self.kolor}"

    def otworz_pamietkni(self, pin):
        if self.czy_otwarty == False:
            if self.haslo == str(pin):
                self.czy_otwarty = True
            else:
                print("Niepoprawne haslo")
        print(f"Pamiętnik jest otwarty: {self.czy_otwarty}")

    def zamknij_pamietnik(self):
        self.czy_otwarty = False

    def dodaj_zawartosc(self, numer_strony, nowa_zawartosc):
        if self.czy_otwarty == False:
            print("Pamietnik jest zamknięty,aby dodac zawartosc musisz go otworzyc wpisujac odpowiedni pin")
        else:
            self.zawartosc_stron[numer_strony].append(nowa_zawartosc)

    def wyswietl_zawartosc_strony(self, numer_strony):
        if self.czy_otwarty == False:
            print("Pamietnik jest zamknięty,aby dodac zawartosc musisz go otworzyc wpisujac odpowiedni pin")
        else:
            print(f"Strona {numer_strony}:")
            print(self.zawartosc_stron[numer_strony])


Pamietnik1 = Pamietnik("Niebieski", "Mieszko", "1234", 5)

Pamietnik1.dodaj_zawartosc(1, "20.05.2023 Byłem w ZOO w Poznaniu i karmiłem słonia jabłkami ponieważ miał 50 urodziny ")

Pamietnik1.otworz_pamietkni(1234)

Pamietnik1.dodaj_zawartosc(1, "20.05.2023 Byłem w ZOO w Poznaniu i karmiłem słonia jabłkami ponieważ miał 50 urodziny ")

Pamietnik1.wyswietl_zawartosc_strony(1)

Pamietnik1.zamknij_pamietnik()

Pamietnik1.wyswietl_zawartosc_strony(1)

