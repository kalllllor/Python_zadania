import random

lista = []

for i in range(0,50):
    x = random.randint(1,5000)
    lista.append(x)

check = sorted(lista)[::-1]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):

        if lista[i] < lista[j]:
           lista[i], lista[j] = lista[j], lista[i]

if check == lista:
    print('Udalo sie!')