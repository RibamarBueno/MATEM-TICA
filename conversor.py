def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 

print("Qual operação você deseja fazer?")
print("1. Celsius para Fahrenheit.")
print("2. Fahrenheit para Celsius.")

while True:
    escolha = input("Digite a temperatura desejada (ou 's' para sair): ")

    if escolha == 's':
        break

    if escolha in ('1', '2'):
        valor = float(input("Digite a temperatura a ser convertida: "))

        if escolha == '1':
            resultado = celsius_to_fahrenheit(valor)
            print("Resultado:", resultado, "ºF")

        elif escolha == '2':
            resultado = fahrenheit_to_celsius(valor)
            print("Resultado:", resultado, "ºC")

    else:
        print("Escolha inválida. Por favor, tente novamente.")