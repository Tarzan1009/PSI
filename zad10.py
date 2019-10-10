lista = []

for i in range(30):
    lista.append(500000000+(i%15)*11)

print(lista)

zbior = set(lista)
print(zbior)
