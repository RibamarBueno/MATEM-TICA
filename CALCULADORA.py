git init

def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Não é possivel dividir por zero."
    else:
        return x / y

print("Menu de operações:")
print("1. Adição.")
print("2. Subtração.")
print("3. Multiplicação.")
print("4. Divisão.")

while True:
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha in ('1','2','3','4'):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print('Resultado:', add(n1,n2))
        elif escolha == '2':
            print('Resultado:', subtract(n1,n2))
        elif escolha == '3':
            print('Resultado:', multiply(n1,n2))
        elif escolha == '4':
            print('Resultado:', divide(n1,n2))

else:
    print('Escolha invalida. Por favor, tente novamente.')

novamente = input('Deseja fazer outra operação? (sim/não):')
if novamente.lower() != 'sim' :
break    

