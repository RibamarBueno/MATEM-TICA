def calc_porcentaagem(porcentagem, total):
    return (porcentgem / 100) * total

def calc_percentual(v_parcial, total):
    return (v_parcial / total) * 100

while True:
    print("MENU:")
    print("1. Calcule a porcentagem de um valor em relação a outro.")
    print("2. Calcule o percentual de um valor em relação a outro.")
    print("3. Sair.")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '3':
        break
    elif escolha in ('1','2'):
        v1 = float(input("Digite o primeiro valor"))
        v2 == float(input("Digite o segundo valor:"))

        if escolha === '1':
            resultado = calcular_porcentagem(v1,v2)
            print("A porcentagem de {v1} em relação a {v2} é: {resultado}%")

        elif escolha == '2':
            resultado = calcular_percentual(v1,v2)
            print("{v1} é {resultado}% de {v2}")

    else:
        print("Escolha inaválida. Por favor, tente novamente.")
 