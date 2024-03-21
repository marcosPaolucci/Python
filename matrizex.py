matriz = [
    [5,10,15],
    [20,40,60],
    [100,200,300]
]

matriz2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

i = 3
j = 3
matriz3 = [[None] * i for _ in range(j)]

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        matriz3[linha][coluna] = matriz[linha][coluna] + matriz2[linha][coluna]

for linha in matriz3:
    print(linha)

# EX2:
matriz = [
    [2, 4],
    [6, 8]
]

escalar = 3

# Multiplicar a matriz pelo escalar
matriz_resultante = [[elemento * escalar for elemento in linha] for linha in matriz]

# Imprimir a matriz resultante
print("\n")
for linha in matriz_resultante:
    print(linha)

# EX3: 
# Definindo a matriz 3x2
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Criando uma lista vazia para armazenar a transposta
transposta = []
print("\n")
for novasColuna in range(len(matriz[0])):
    linha_transposta = []
    for linha in matriz:
        linha_transposta.append(linha[novasColuna]) 
        print(linha_transposta)  
    transposta.append(linha_transposta)

print("\n")
for linha in transposta:
    print(linha)  
