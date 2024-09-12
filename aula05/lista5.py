# Função de processamento do programa
def funcao_processamento():
    agua_disponivel = float(input('Digite a quantidade de água(em litros) disponível: '))
    distancia = float(input("Digite a distância(em km): "))

    agua_necessaria = distancia * 2

    if agua_disponivel >= agua_necessaria:
        print(f'Essa água é suficiente!')
    else:
        print(f'Essa água é insuficiente!')


if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")