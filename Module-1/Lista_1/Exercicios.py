#1. Criar um algoritmo para ler os lados de um triângulo e identificar se é equilátero.
#2. Adapte o exemplo anterior para identificar um triângulo isósceles (2 lados iguais).
#3. Adapte o algoritmo anterior para identificar o maior lado de um triângulo escaleno

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))
#1 e 2 
if ((lado1 > 0) and (lado2 > 0) and (lado3 > 0) and (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)):
    if (lado1 == lado2 == lado3):
        print("O triângulo é equilátero.")
    elif ((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
        #3
        maior_lado = max(lado1, lado2, lado3)
        print(f"O maior lado do triângulo escaleno é: {maior_lado}")
else:
    print("Os valores informados não formam um triângulo.")


#4. Faça um algoritmo que calcule a área de um Triângulo (os valores da base e altura devem ser lidos do teclado).
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = (base * altura) / 2
print(f"A área do triângulo é: {area}")

#5. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 25% de desconto
produto = float(input("Digite o preço do produto: "))

desconto = produto * 0.25
novo_preco = produto - desconto
print(f"O novo preço do produto com 25% de desconto é: {novo_preco}")

#6. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa em dias. Considerar ano com 365 dias e mês com 30 dias

anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))
total_dias = (anos * 365) + (meses * 30) + dias
print(f"A idade dessa pessoa em dias é: {total_dias} dias")

#7. Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
#a. Seu programa deve verificar se a soma de brancos, nulos e válidos equivalem a 100% do número de eleitores que votaram.

while True:
    total_eleitores = int(input("Digite o número total de eleitores: "))
    votos_brancos = int(input("Digite o número de votos brancos: "))
    votos_nulos = int(input("Digite o número de votos nulos: "))
    votos_validos = int(input("Digite o número de votos válidos: "))
    if (votos_brancos + votos_nulos + votos_validos) == total_eleitores:
        break
    else:
        print("A soma de votos brancos, nulos e válidos não equivale ao total de eleitores. Por favor, insira os votos corretamente.")
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100
print(f"Percentual de votos brancos: {percentual_brancos:}%")
print(f"Percentual de votos nulos: {percentual_nulos:}%")
print(f"Percentual de votos válidos: {percentual_validos:}%")