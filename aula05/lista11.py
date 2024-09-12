def funcao_processamento():
    candidato1 = float(input('Digite a nota do candidato 1: '))
    candidato2 = float(input('Digite a nota do candidato 2: '))
    candidato3 = float(input('Digite a nota do candidato 3: '))

    media1 = candidato1
    media2 = candidato2
    media3 = candidato3

    if media1 > media2 and media1 > media3:
        print('O primeiro candidato é o vencedor!')
    elif media2 > media1 and media2 > media3:
        print('O segundo candidato é o vencedor!')
    elif media3 > media1 and media3 > media2:
        print('O terceiro candidato é o vencedor!')
    elif media1 == media2 == media3:
        print('Houve um empate entre todos os candidatos!')
    elif media1 == media2 and media1 > media3:
        print('Houve um empate entre o primeiro e o segundo candidato!')
    elif media1 == media3 and media1 > media2:
        print('Houve um empate entre o primeiro e o terceiro candidato!')
    elif media2 == media3 and media2 > media1:
        print('Houve um empate entre o segundo e o terceiro candidato!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")
