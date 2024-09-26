import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

while True:
    tentativa = int(input("Qual é o seu palpite? "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Mais alto! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Mais baixo! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break

print("Fim do jogo.")