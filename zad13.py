lista = []
for i in range(4):
    slownik = {}
    for j in range(5):
        slownik[j*13+3] = i*23+2
    print(slownik)
    lista.append(slownik)

tekst = ''
for i in range(len(lista)):
    for j in lista[i].keys():
        tekst = tekst + str(j) + ': ' + str(lista[i][j]) + ', '
    tekst = tekst + 'koniec slownika %i! ' % (i)

print(tekst)