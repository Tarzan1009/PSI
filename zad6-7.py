lista = list(range(1,11))
print(lista)

lista2 = lista[5:]
lista = lista[:5]

print(lista)
print(lista2)

lista = lista + lista2
print(lista)

lista.insert(0, 0)
print(lista)
lista_kopia = lista
lista_kopia.sort(reverse=True)
print(lista_kopia)