import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Não é possível dividir por zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Não é possível calcular a raiz quadrada de um número negativo."
    else:
        return math.sqrt(x)

print("Menu de operações:")
print("1. Adição.")
print("2. Subtração.")
print("3. Multiplicação.")
print("4. Divisão.")
print("5. Potência.")
print("6. Raiz quadrada.")

while True:
    escolha = input("Digite o número da operação desejada: ")

    if escolha in ('1', '2', '3', '4', '5', '6'):
        if escolha in ('1', '2', '3', '4', '5'):
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print('Resultado:', add(n1, n2))
        elif escolha == '2':
            print('Resultado:', subtract(n1, n2))
        elif escolha == '3':
            print('Resultado:', multiply(n1, n2))
        elif escolha == '4':
            print('Resultado:', divide(n1, n2))
        elif escolha == '5':
            print('Resultado:', power(n1, n2))
        elif escolha == '6':
            n = float(input('Digite o número para calcular a raiz quadrada: '))
            print('Resultado:', square_root(n))
    else:
        print('Escolha inválida. Por favor, tente novamente.')
        break

    novamente = input('Deseja fazer outra operação? (sim/não): ')
    if novamente.lower() != 'sim':
        break


