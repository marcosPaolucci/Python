lista = [1,2,3]
nova_lista = [x * 2 for x in lista]
print(nova_lista)

strings = ["ola", "tudo","certo", "ai"]
todas_mais_de_tres = True
for palavra in strings:
    if len(palavra) <= 3:
        todas_mais_de_tres = False
        break

if todas_mais_de_tres:
    print("Todas as strings têm mais de 3 caracteres.")
else:
    print("Pelo menos uma das strings tem 3 caracteres ou menos.")

numeros = [10,5,90,45,20]
ordem = sorted(numeros)
print(ordem)
#ou tem outro jeito mudando a lista original
numeros.sort()
print(numeros)
# agora em ordem decrescente:
decrescente = sorted(numeros, reverse=True)
print(decrescente)
#outro jeito:
numeros.sort(reverse=True)
print(numeros)

paresimpares = [1, 4, 7, 14, 33, 41]
count = 0
for num in paresimpares:
    if (num % 2) == 0:
        count+=1
print(count)

lista = [2,4,8]
resultado = 1
for num in lista:
    resultado *= num
print(resultado)

#for i in range(50):
    #print(str(i+1))

#for i in range(1,51):
    #print(str(i))

i = 1
while i < 51:
    print(i)
    i += 1

frase = ["como", "vai", "voce"]
for palavra in frase:
    print(palavra)

for i in range(2,10):
   if (i% 2) <= 0:
       print(i)

resultado = 1
for num in range(1,6):
    resultado *= num
print(resultado)

# O Python aceita o else quando usarmos o while
contagem = 10
while contagem > 0 :
    print(contagem)
    contagem -= 1
else:
        print("Fogo!")

while True:
    entrada = int(input("Digite um número: "))
    if entrada % 2 == 0:
        print("Número par detectado. O programa terminou.")
        break

import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10. Você tem 3 tentativas.")

for _ in range(tentativas):
    while True:
        tentativa = int(input("Digite sua tentativa: "))
        if 1 <= tentativa <= 10:
            break
        else:
            print("Por favor, digite um número válido entre 1 e 10.")
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break
    else:
        print("Tentativa incorreta.")
else:
    print("Fim do jogo. O número secreto era:", numero_secreto)

soma = 0
while True:
    num1 = int(input("Digite o primeiro num positivo: "))
    if num1 <= 0:
        print("O numero deve ser positivo! Programa encerrado")
        break
    num2 = int(input("Digite o segundo num positivo: "))
    if num2 <= 0:
        print("O numero deve ser positivo! Programa encerrado")
        break
    soma = num1+num2
    print("A soma dos numeros é " + str(soma))
    break

numeros = 0
multiplos3 = 0
while numeros != 10:
    multiplos3 +=1
    if multiplos3 % 3 == 0:
        print(multiplos3)
        numeros += 1
    
