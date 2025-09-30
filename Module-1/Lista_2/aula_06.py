#aula 16/09
#lista 2b

#3.MRUV

#declarações
#posição inicial

S_0= float(input("Digite o valor da posição inicial(em metros): "))

#velocidade
v=float(input("digite o valor da velocidade(m/s): "))

#tempo
tempo=[]
for i in range(5):
    t=float(input("Digite o tempo gasto no movimento(segundos): "))
    tempo.append(t)

#distancia percorrida
distancia = []
for i in range(len(tempo)):
    s= S_0 +(v*tempo[i])
    distancia.append(s)
    print(f"A distancia percorrida no movimento é: {distancia}m/s")
