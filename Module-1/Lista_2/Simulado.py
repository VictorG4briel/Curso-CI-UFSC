#1. Crie um programa que leia as notas (0 a 10) de 15 alunos de uma turma.
""" a. Armazenar as notas em uma lista.
b. Calcular e mostrar:
c. A maior nota.
d. A menor nota.
e. A média da turma.
f. A quantidade de alunos acima da média.
"""

notas_turma=[]
for i in range(15):
    nota_aluno=float(input("Digite a sua nota:"))
    notas_turma.append(nota_aluno)

media_turma=sum(notas_turma)/len(notas_turma)
nota_max=max(notas_turma)
nota_min=min(notas_turma)
notas_acima_m=[]

for notas in notas_turma:
    if (notas>7):
        notas_acima_m.append(notas)

print(f"Maior nota:{nota_max}")
print(f"Menor nota:{nota_min}")
print(f"Media da turma:{media_turma}")
print(f"Notas acima da media:{notas_acima_m}")

#2. Crie um programa que possua uma função chamada classificar_imc que receba
# dois parâmetros: nome (texto) e imc (float).
""" a. Abaixo de 18.5: "nome está abaixo do peso."
b. De 18.5 a 24.9: "nome está com peso normal."
c. De 25.0 a 29.9: "nome está com sobrepeso."0,
d. 30.0 ou mais: "nome está obeso."
e. No programa principal, solicite o nome e o IMC de várias pessoas e mostre a
classificação. O programa deve continuar até o usuário informar "sair" como
nome."""
def classificar_imc(nome,imc):
            if (imc< 18.5):
                print(f"{nome} está abaixo do peso")
            elif(18.5<=imc<=24.9):
                print(f"{nome} está com o peso normal")
            elif(25<=imc<=29.9):
                print(f"{nome} está com o sobrepeso")
            else:
                print(f"{nome} está obeso")
while True:
    nome=input("Digite seu nome(ou 'sair' para encerrar):")
    if (nome.lower() == "sair"):
        print("Programa encerrado")
        break
    imc=float(input("Digite seu imc:"))
    classificar_imc(nome,imc)

#3. Crie um programa para analisar salários de funcionários.
""" O programa deve ter uma função chamada analisar_salarios que receba uma lista com
os valores dos salários.
A função deve retornar:
a. O total de funcionários.
b. O maior salário.
c. O menor salário.
d. A quantidade de funcionários que ganham acima de R$ 3.000,00.
e. A média dos salários.
f. O programa deve:
g. Ler os salários até o usuário digitar -1.
h. Chamar a função e exibir os resultados."""

def analisar_salarios(salarios):
    total_funcionarios=len(funcionarios)
    max_salario=max(salarios)
    min_salario=min(salarios)
    salarios_acima=[]
    for sal in salarios:
        if (sal>3000):
            salarios_acima.append(sal)
    media=sum(salarios)/len(salarios)
    print(f"Total de funcionarios: {total_funcionarios}")
    print(f"Maior salario: R${max_salario}")
    print(f"Menor salario: R${min_salario}")
    print(f"Funcionarios com salario acima de R$3.000,00: {len(salarios_acima)}")
    print(f"Media de salario: R${media}")

funcionarios=[]
salarios=[]
while True:
    funcionario=input("Digite seu nome(ou -1 para sair):")
    if (funcionario == "-1"):
        print("Programa encerrado")
        break
    salario=float(input("Digite seu salario:"))
    funcionarios.append(funcionario)
    salarios.append(salario)
if salarios:
    analisar_salarios(salarios)