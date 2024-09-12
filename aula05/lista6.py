# Função de processamento do programa
def funcao_processamento():
    distancia1 = float(input('Digite a distancia do primeiro dragão: '))
    velocidade1 = float(input("Digite a velocidade do primeiro dragão: "))

    distancia2 = float(input('Digite a distancia do segundo dragão: '))
    velocidade2 = float(input("Digite a velocidade do segundo dragão: "))

    tempo1 = velocidade1/distancia1
    tempo2 = velocidade2/distancia2

    if tempo1 > tempo2:
        print(f'O primeiro dragão é mais rápido!')
    if tempo2 > tempo1:
        print(f'O segundo dragão é mais rápido!')
    else:
        print(f'Os dois tem a mesma velocidade!')


if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")