lista = []
n = -15
while (n < 0):
    lista.append(n)
    n += 1
print(lista)

print("ejercicio 2 :")
#otro ej
lis1 = ['run','fly','sleep']
lis2 = ['correr','volar','dormir']
lisz = zip(lis1, lis2)
    print(type(lisz))
    print(list(lisz))