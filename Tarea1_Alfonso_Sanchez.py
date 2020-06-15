# Lista
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tamanio = 0
#Tamaño de lista
for i in lista:
    tamanio = tamanio + 1

#ordenamiento de menor a mayor de la lista
linferior = 0
for i in range (tamanio-1):
    for indice in range(tamanio -1,linferior,-1):
        if lista[indice] < lista[indice -1]:
            lista[indice], lista[indice -1] = lista[indice - 1], lista[indice]
    linferior = linferior + 1
    print(lista)
