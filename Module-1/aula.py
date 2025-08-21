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