def tabuada_personalizada():
    numero = int(input("Digite um número para gerar a tabuada: "))
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabuada_personalizada()