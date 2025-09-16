# Aula 02/09
#Tema: Loops, if

#If
#numbers = [3, 6, 2, 7, 9]
#for i in numbers:
#    print(i)
#    numbers.sort()
#    print(numbers)

#Loops
#MAXIMO = 10
#i=0
#while (i < 10):



#Declarações
alunos= []
notas=[]
MEDIA = 6.0
MINIMO= 3


while True:
#entradas
    aluno = input("Digite o nome do aluno ou '-1' para encerrar:")
    if(aluno == "-1"):
        break
    nota = float(input("Digite a nota do aluno:"))
    
    alunos.append(aluno)
    notas.append(nota)
    
    if(nota >= MEDIA):
        print(f"O aluno foi APROVADO com nota {nota}")
    elif(nota >= MINIMO):
        print(f"O aluno esta de RECUPERAÇÃO com nota {nota}")
    else:
        print(f"O aluno foi REPROVADO com nota {nota}")

print(alunos)
print(notas)