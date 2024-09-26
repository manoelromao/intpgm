def decimal_para_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario if binario else "0"

numero = int(input("Digite um número decimal: "))

print(f"O número {numero} em binário é {decimal_para_binario(numero)}.")
