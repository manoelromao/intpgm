# Função de processamento do programa
def funcao_processamento():
    print('Digite seu animal favorito:')
    print('1 - Mamífero \n2 - Réptil')
    opcao = int(input('Qual sua opção?'))

    if opcao == 1:
        print('Ah! Certeza que é um doguinho')
    else:
        print('Caramba! Você gosta de répteis!')
if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")