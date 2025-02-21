#jogo de adivinhação criado com 90% de ajuda de IA

import random

numero_aleatorio = random.randint(1, 100)

print("Tenta adivinhar o numero que estou pensando de 1 a 100")
tentativas = 0

while True:
    try:

        palpite = int(input("De seu palpite:"))
        tentativas+= 1

        if palpite < numero_aleatorio:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_aleatorio:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabens!! Voce acertou em {tentativas} tentativas.")
            break
    except ValueError:
        print("Por favor, digite um numero valido!")