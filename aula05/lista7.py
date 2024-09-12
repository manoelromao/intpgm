# Função de processamento do programa
def funcao_processamento(altura):
    if altura < 1:
        print("A planta é pequena.")
    elif 1 <= altura <= 3:
        print("A planta é média.")
    else:
        print("A planta é grande.")

altura_planta = float(input("Digite a altura da planta (em metros): "))

if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento(altura_planta)

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")