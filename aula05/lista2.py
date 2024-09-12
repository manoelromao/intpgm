# Função de processamento do programa
def funcao_processamento():
    qtd_ferro = float(input('Digite a quantidade de forrro: '))
    qtd_ouro = float(input('Digite a quantidade de ouro: '))

    total_liga_metalica = qtd_ferro + qtd_ouro

    if (qtd_ferro/total_liga_metalica) >= 0.7:
        print("A sua armadura é massa!")
    else:
        print("Essa armadura vai quebrar!")
    


if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")