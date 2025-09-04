#Aula 26/08
#Declaração
MEDIA = 6.0
MINIMO= 3.5
alunos=input("Digite seu nome:")
notas= []

while True:
    nota=float(input("Digite sua nota ou '-1' para finalizar:"))
    if(nota == -1 ):
        break
    elif(0 <= nota <= 10):
        notas.append(nota)
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

MEDIA_ALUNO = sum(notas) / len(notas)
if(MEDIA_ALUNO >= MEDIA):
    print("O aluno foi APROVADO")
elif(MEDIA_ALUNO>=MINIMO):
    print("O aluno esta de RECUPERAÇÃO")
else:
    print("O aluno foi REPROVADO")

print(f"A nota do aluno {alunos} é {notas}")


