import random

def jogo_adivinhacao():
    numero_secreto =  random.randint(1,100)
    tentativas = 0

    print("Bwm vindo ao Jogo da Adivinhação!\n Tente adivinhar um número entre 1 a 100. ")

    while True:
        tentativa = int(input("Digite um número:"))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Número menor que o numero secreto. Tente novamente.")
        
        elif tentaiva> numero_secreto:
            print("Numero maior que o número secreto. Tente novamente.")

        else:
            print("Show!! Você acertou o número secreto é {numero_secreto}.  E você fez {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()