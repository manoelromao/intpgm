def funcao_processamento():
    ataque1 = float(input("Digite o poder de ataque do guerreiro 1: "))
    defesa1 = float(input("Digite o poder de defesa do guerreiro 1: "))

    ataque2 = float(input("Digite o poder de ataque do guerreiro 2: "))
    defesa2 = float(input("Digite o poder de defesa do guerreiro 2: "))

    soma1 = ataque1 + defesa1
    soma2 = ataque2 + defesa2

    if soma1 > soma2:
        print("O guerreiro 1 é o vencedor!")
    elif soma2 > soma1:
        print("O guerreiro 2 é o vencedor!")
    else:
        if defesa1 > defesa2:
            print("O guerreiro 1 é o vencedor por ter uma defesa maior!")
        elif defesa2 > defesa1:
            print("O guerreiro 2 é o vencedor por ter uma defesa maior!")
        else:
            print("Empate entre os guerreiros!")

if __name__ == '__main__':
    # Mensagem de início do programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")
