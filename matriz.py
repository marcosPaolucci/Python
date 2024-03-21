matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# printar o valor da matriz na segunda linha e terceira coluna
# levando em consideração que o pyhton é indice 0
#print(matriz[1][2])

nova_linha = [10,11,12]
matriz.append(nova_linha)

#imprimindo a matriz atualizada
#for linha in matriz:
   # print(linha)

#inserou o valor 100 na linha 2 e no lugar de indice 1
matriz[2].insert(1,100)
for linha in matriz:
    print(linha)

print("\n")
del matriz[1]
for linha in matriz:
    print(linha)

print("\n")
elemento = matriz[1].pop(3)
print("\nElemento removido: ", elemento)
for linha in matriz:
    print(linha)

print("\n")
for linha in matriz:
    #iterar sobre cada elemento da linha
    for elemento in linha:
        print(elemento, end=" ")
    #Imprimir uma nolva linha para cada linha da matriz:
    print()