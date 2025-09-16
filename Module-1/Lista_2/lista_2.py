#1. Faça um Programa que peça dois números e imprima o maior deles.
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

max=max(num1,num2)
print(f"O maior número é: {max}")

#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num=float(input("Digite um número: "))
if num>=0:
    print("O número é positivo.")   
else:
    print("O número é negativo.")

#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

sexo= input("Digite o sexo (F/M): ").upper()
if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")

#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante
vogais = ['a', 'e', 'i', 'o', 'u']
letra = input("Digite uma letra: ").lower()
if letra in vogais:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
notas = []
for i in range(2):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media_aluno = sum(notas) / len(notas)
print(f"A média do aluno é: {media_aluno}")
if media_aluno == 10.0:
    print("Aprovado com Distinção")
elif 7.0<=  media_aluno < 10.0:
    print("Aprovado")
else:
    print("Reprovado")
#6. Faça um Programa que leia três números e mostre o maior deles

numeros=[]
for i in range(3):
    numero=float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior_numero=max(numeros)
print(f"O maior número é: {maior_numero}")

#7  Faça um Programa que leia três números e mostre o maior e o menor deles
numeros=[]
for i in range(3):
    numero=float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior_numero=max(numeros)
menor_numero=min(numeros)
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")

#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
#decisão é sempre pelo mais barato
produtos=[]

for i in range(3):
    preco=float(input(f"Digite o preço do produto: "))
    produtos.append(preco)

mais_barato=min(produtos)
print(f"O produto mais barato custa: {mais_barato}")

#9. Faça um Programa que leia três números e mostre-os em ordem decrescente

numeros=[]
for i in range(3):
    numero=float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
descrescente=sorted(numeros, reverse=True)
print(f"Números em ordem decrescente: {descrescente}")

#10.numeros=[]
for i in range(3):
    numero=float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
turno = input("Em que turno você estuda? (M/V/N): ").upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Turno inválido!")
