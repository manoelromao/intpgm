# Função de processamento do programa
def funcao_processamento():
    qtd_25 = float(input('Digite a quantidade de moedas de 25 centavos: '))
    qtd_1 = float(input('Digite a quantidade de moedas de 1 real: '))
    qtd_50= float(input('Digite a quantidade de 50 centavos: '))

    total = qtd_25 + qtd_1 + qtd_50

    if total:
        print(f'Esse é o total de moedas: {total}!')


if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")