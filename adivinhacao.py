import random

def adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Tente adivinhar o número entre 1 e 100!")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
            elif palpite < numero_secreto:
                print("Tente um número maior!")
            elif palpite > numero_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

adivinhacao()
