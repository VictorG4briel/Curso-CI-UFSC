#Aula
#Variáveis e constantes

#imports
import array as np



#declarações
firtsName = "João"
lastName = " Silva"
name = firtsName + lastName
valorHora= 45.36
valorHoraAprox = int(valorHora)
dias_Trabalhados = 30
HORAS_TRABALHADAS = 8
HORAS_TRABALHADAS_AJUST = float(HORAS_TRABALHADAS)
vencimento = (HORAS_TRABALHADAS_AJUST * valorHora) * dias_Trabalhados

dadosFuncionario = [firtsName,lastName,vencimento]
valores = np.array("f",{valorHora, HORAS_TRABALHADAS_AJUST})

#Saídas
print('Funcionario')
print(dadosFuncionario[0]+ "" + dadosFuncionario[1])
print("Salario/Mes")
print("R$" + "", dadosFuncionario[2])

print(valores)

#Aula revisão
import array as arr

alunos=["joão","Pedro","Paula","Carlos","Maria"]
#alunos.append("Rodrigo")
#alunos.remove("joão")
#alunos.reverse()
alunos.sort()


notas= arr.array("f",[4.5,5.0,8.5,3.5,10.0])


professores=["Ivam","João","Ricardo"]
print(alunos)
print(notas)
print(professores)
