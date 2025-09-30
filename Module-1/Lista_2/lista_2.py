#1. Faça um Programa que peça dois números e imprima o maior deles.
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

maximo=max(num1,num2)
print(f"O maior número é: {maximo}")

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

#10.Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turno = input("Em que turno você estuda? (M/V/N): ").upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Turno inválido!")

#11.Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
#salário atual

salario = float(input("Digite o valor do seu salario: "))
salario_reajuste=0
if (salario <=280):
    salario_reajuste += salario * 1.2
    valor_porcentagem = salario * 0.2
    print(f"Salario antes do reajuste:{salario}")
    print(f"Salario antes do reajuste:{salario_reajuste}")  
    print("reajuste de 20%")
    print(f"valor do aumento:{valor_porcentagem}")
elif (280< salario <700):
    salario_reajuste += salario * 1.15
    valor_porcentagem = salario * 0.15
    print(f"Salario antes do reajuste:{salario}")
    print(f"Salario antes do reajuste:{salario_reajuste}")
    print("reajuste de 15%")
    print(f"valor do aumento:{valor_porcentagem}")

elif (700< salario <1500):
    salario_reajuste += salario * 1.10
    valor_porcentagem = salario * 0.10
    print(f"Salario antes do reajuste:{salario}")
    print(f"Salario antes do reajuste:{salario_reajuste}")
    print("reajuste de 10%")
    print(f"valor do aumento:{valor_porcentagem}")

else:
    salario_reajuste+= salario* 1.05
    valor_porcentagem = salario * 0.05
    print(f"Salario antes do reajuste:{salario}")
    print(f"Salario antes do reajuste:{salario_reajuste}")
    print("reajuste de 5%")
    print(f"valor do aumento:{valor_porcentagem}")

""" 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. """

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês:"))
salario_bruto = valor_hora * horas_trabalhadas

if (salario_bruto < 900):
    print(f"Salario bruto({valor_hora}*{horas_trabalhadas})")
    print("IR: isento")
    print("Total de desconto: 0")
    print("Total de desconto: 0")
    print(f"Salario liquido: {salario_bruto}")
elif (900 <salario_bruto <= 1500):
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.03
    fgts= salario_bruto * 0.11
    salario_liquido = salario_bruto - (ir - inss - fgts)
    print(f"Salario bruto({valor_hora}*{horas_trabalhadas})")
    print("IR: desconto de 5%")
    print("Total de desconto: 0")
    print("Total de desconto:")
    print(f"Salario liquido: {salario_liquido}")
elif (1500 <salario_bruto <= 2500):
    ir = salario_bruto * 0.10
    inss = salario_bruto * 0.03
    fgts= salario_bruto * 0.11
    salario_liquido = salario_bruto - (ir - inss - fgts)
    print(f"Salario bruto({valor_hora}*{horas_trabalhadas})")
    print("IR: desconto de 10%")
    print("Total de desconto: 0")
    print("Total de desconto:")
    print(f"Salario liquido: {salario_liquido}")
else:
    ir = salario_bruto * 0.20
    inss = salario_bruto * 0.03
    fgts= salario_bruto * 0.11
    salario_liquido = salario_bruto - (ir - inss - fgts)
    print(f"Salario bruto({valor_hora}*{horas_trabalhadas})")
    print("IR: desconto de 20%")
    print("Total de desconto: 0")
    print("Total de desconto:")
    print(f"Salario liquido: {salario_liquido}")


#13. faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
#outro valor deve aparecer valor inválido

dias_semana =["Segunta" ,"Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
numero=int(input("Digite um número de 1 a 7: "))
if 1<= numero <=7:
    print(dias_semana[numero - 1])
else:
    print("Valor inválido")

#14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um 
#semestre, e calcule a sua média.A atribuição de conceitos obedece à tabela abaixo:
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
#conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E

notas=[]
for i in range(2):
    nota=float(input(f"Digite a nota da {i+1}º prova:"))
    notas.append(nota)
media = sum(notas)/len(notas)
if (9<media <=10):
    conceito = 'A'
elif (7.5<media<=9):
    conceito = 'B'
elif (6.0<media<=7.5):
    conceito = 'C' 
elif(4<media<=6):
    conceito = 'D' 
else:
    conceito = 'E'

status = "APROVADO" if conceito in ['A', 'B', 'C'] else "REPROVADO"
print(f"Notas: {notas[0]}, {notas[1]}")
print(f"Media:{media}")
print(f"Conceito:{conceito}")
print(f"Resultado:{status}")

#15Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
#triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))

if (lado1<lado2 + lado3)and (lado2<lado1 +lado3)and(lado3<lado1+lado2):
    print("Os valores fomam um triangulo!")
    if lado1 == lado2 == lado3:
        print("Triangulo Equilatero")
    elif (lado3==lado1) or (lado3==lado2) or (lado1==lado2):
        print("Triangulo Isóceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Os valores não fomam um triangulo")

#16.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
#pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

import math 

a=float(input("digite o valor de 'A':"))
b=float(input("digite o valor de 'B'':"))
c=float(input("digite o valor de 'C':"))

delta=b**2 - 4*a*c
if (a == 0):
    print("Essa equação não é do segundo grau")
else:
    if (delta<0):
        print("Esse equação não possui raizes reais")
    elif (delta == 0):
        x = -b/(2*a)
        print(f"Essa equação possui apenas uma raiz:{x}")
    else:
        x1=(-(b)- math.sqrt(delta))
        x2=(-(b) + math.sqrt(delta))
        print(f"As raízes da equação são: x1 = {x1}, x2 = {x2}")    