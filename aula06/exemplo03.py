numero = int(input("Digite um número para calcular a tabuada: "))

nome_arquivo = "tabuada.txt"

with open(nome_arquivo, "w") as arquivo:
    arquivo.write(f"Tabuada do {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        arquivo.write(f"{numero} x {i} = {resultado}\n")

print(f"A tabuada do {numero} foi salva em '{nome_arquivo}'!")
