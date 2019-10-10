def policz(tekst, litera):
    suma = 0
    for i in tekst:
        if i == litera:
            suma = suma + 1
    return suma

tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
imie = 'Piotr'
nazwisko = 'Praszkiewicz'
litera_1 = imie[2]
litera_2 = nazwisko[3]
print('W tekście jest %i liter %s oraz %i liter %s' % (policz(tekst, litera_1), litera_1, policz(tekst, litera_2), litera_2))