#1. Criar um algoritmo para ler os lados de um triângulo e identificar se é equilátero.

lado1 =int(input("Digite o  primeiro lado do triagulo:"))
lado2 = int(input("Digite o segundo lado do triagulo:"))
lado3 = int(input("Digite o terceiro lado do triagulo:"))


if (lado1> lado2 and lado1>lado3 and lado2>lado3):
    print("O triangulo é escaleno")
elif(lado1> lado2 and lado1>lado3 and lado2==lado3 or lado1==lado2):
    print("O triangulo é isóceles")
else:
    print("O triangulo é equilatero")