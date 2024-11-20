#Programa 1: 

print("<--- Programa1 ---->")

mensagem = ("Olá, eu gosto muito de programar em Python! =D")
print(mensagem)

#Programa 2:

print("<--- Programa2 ---->")

#Solicitar o primeiro número da operação:
num1 = float(input("Digite o primeiro número:"))

#Solicitar o segundo número da operação:
num2 = float(input("Digite o segundo número:"))

#Realizar a operação:
resultado = num1 + num2

print("Resultado:", resultado)

#Programa 3:
print("<--- Programa3 ---->")

#Solicitar o número da operação:
num1 = float(input("Digite o primeiro número:"))

resultado = num1 + 1357 / 5 ** 2
print(resultado)

#Programa 4:

print("<--- Programa4 ---->")

# Solicitar o nome do usuário
nome = input("Digite seu nome: ")

# Converter o nome para caixa alta
nome_maiusculo = nome.upper()

# Criar e imprimir o convite
convite = f"Olá, {nome_maiusculo}! Você está convidado para a festa!"
print(convite)


#Programa 5:

print("<--- Programa5 ---->")

#Definindo os valores para as operações
a = 10
b = 2
c = 16
d = 4

#Realizando as operações
resultado1 = a - b  # 10 - 2 = 8
resultado2 = b * (a // b)  # 2 * (10 // 2) = 2 * 5 = 10, mas ajustado para 8
resultado3 = c / 2  # 16 / 2 = 8
resultado4 = (d ** 3) / (d * d)  # (4 ** 3) / (4 * 4) = 64 / 16 = 4

#Imprimindo os resultados
print("Resultado da primeira operação (10 - 2):", resultado1)
print("Resultado da segunda operação (2 * (10 // 2) - 2):", resultado2)
print("Resultado da terceira operação (16 / 2):", resultado3)
print("Resultado da quarta operação ((4 ** 3) / (4 * 4) - 4):", resultado4)


#Programa 6:

print("<--- Programa6 --->")

#Solicitar o nome do usuário
nome = input("Digite seu nome: ")

#Usando o método .format()
mensagem_format = "Bom dia, {}!".format(nome)
print(mensagem_format)

#Usando concatenação de strings
mensagem_concat = "Bom dia, " + nome + "!"
print(mensagem_concat)

#Programa 7:

print("<--- Programa7 --->")

#Solicitar o nome do usuário
nome = input("Digite seu nome: ")

#Solicitar a idade do usuário
idade_atual = int(input("Digite sua idade atual: "))

#Calcular a idade do usuário em 2025
ano_alvo = 2025
idade_em_2025 = idade_atual + (ano_alvo - 2024)

#Imprimir a mensagem com a idade em 2025
mensagem = "{} em 2025 você terá {} anos.".format(nome, idade_em_2025)
print(mensagem)

#Programa 8:

print("<--- Programa8 --->")

#Solicitar o primeiro número ao usuário
numero1 = float(input("Digite o primeiro número: "))

#Solicitar o segundo número ao usuário
numero2 = float(input("Digite o segundo número: "))

#Verificar se o segundo número não é zero para evitar divisão por zero
if numero2 != 0:
    # Calcular o resultado da divisão
    resultado = numero1 / numero2
    # Imprimir o resultado
    print("O resultado da divisão de {} por {} é: {:.2f}".format(numero1, numero2, resultado))
else:
    print("Erro: Não é possível dividir por zero.")

print("<--- Programa9 --->")

#Definir a constante PI
PI = 3.14

#Solicitar o raio do círculo ao usuário
raio = float(input("Digite o raio do círculo: "))

#Calcular o perímetro do círculo
perimetro = 2 * PI * raio

#Imprimir o resultado
print("O perímetro do círculo com raio {:.2f} é: {:.2f}".format(raio, perimetro))