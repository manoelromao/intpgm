nome_arquivo = "tabuadas.txt"

with open(nome_arquivo, "w") as arquivo:
    for i in range(1, 11):
        arquivo.write(f"Tabuada do {i}:\n")
        for j in range(1, 11):
            resultado = i * j
            arquivo.write(f"{i} x {j} = {resultado}\n")
        arquivo.write("\n") 

print(f"As tabuadas foram salvas em '{nome_arquivo}'!")
