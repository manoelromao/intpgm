def funcao_processamento():
    posicao_exercito = input("Digite a posição do exército (dentro ou fora): ")

    match posicao_exercito:
        case "fora":
            print("O sistema de defesa está ativado.")
        case "dentro":
            print("O sistema de defesa está desativado.")
        case _:
            print("Posição inválida. Por favor, digite 'dentro' ou 'fora'.")

if __name__ == '__main__':
    # Mensagem de início do programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")
