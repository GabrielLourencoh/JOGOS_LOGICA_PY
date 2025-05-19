import random
import time
import os

while True:
    simbolos = ["🥸", "😎", "🫡", "🥳", "🤠", "🧐", "🤓", "🥶"]

    def limpar_tela():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    print("Bem-vindo ao Giro da Sorte!")
    input("Pressione Enter para girar...")

    for i in range(10):
        a = random.choices(simbolos)
        b = random.choices(simbolos)
        c = random.choices(simbolos)
        limpar_tela()

        print(f"| {a} | {b} | {c} |")
        time.sleep(0.5)

        print("\nResultado: ")
        if a == b and b == c:
            print("🏆 Parabéns! Você mandou bem!")
        elif a == b or b == c or a == c:
            print("Quase lá! Dois simbolos iguais.")
        else:
            print("Putz! Não foi dessa vez.")