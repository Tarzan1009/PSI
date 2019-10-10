lista = []
for i in range(10):
    nr = 150000+i
    krotka = ('Jan Kowalski'+str(i), nr)
    lista.append(krotka)

print(lista)
print(len(lista))

slownik = {}
for i in range(len(lista)):
    slownik[lista[i][0]] = lista[i][1]

print(slownik.keys())
print(slownik.values())

for i in range(len(lista)):
    slownik[lista[i][0]+str(i)] = 1995+i

print(slownik.keys())
print(slownik.values())