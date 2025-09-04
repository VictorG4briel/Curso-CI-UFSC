while True:
    total_eleitores = int(input("Digite o número total de eleitores: "))
    votos_brancos = int(input("Digite o número de votos brancos: "))
    votos_nulos = int(input("Digite o número de votos nulos: "))
    votos_validos = int(input("Digite o número de votos válidos: "))
    if (votos_brancos + votos_nulos + votos_validos) == total_eleitores:
        break
    else:
        print("A soma de votos brancos, nulos e válidos não equivale ao total de eleitores. Por favor, tente novamente.")

percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100
print(f"Percentual de votos brancos: {percentual_brancos:}%")
print(f"Percentual de votos nulos: {percentual_nulos:}%")
print(f"Percentual de votos válidos: {percentual_validos:}%")