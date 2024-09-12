def funcao_processamento():
    ataque_espada = float(input('Digite o poder de ataque da espada: '))
    durabilidade_espada = float(input('Digite a durabilidade da espada: '))

    ataque_arco = float(input('Digite o poder de ataque do arco: '))
    durabilidade_arco = float(input('Digite a durabilidade do arco: '))

    ataque_lanca = float(input('Digite o poder de ataque da lança: '))
    durabilidade_lanca = float(input('Digite a durabilidade da lança: '))

    if ataque_espada > 50 and durabilidade_espada > 70:
        espada_adequada = True
    else:
        espada_adequada = False

    if ataque_arco > 50 and durabilidade_arco > 70:
        arco_adequado = True
    else:
        arco_adequado = False

    if ataque_lanca > 50 and durabilidade_lanca > 70:
        lança_adequada = True
    else:
        lança_adequada = False

    if espada_adequada and (not arco_adequado and not lança_adequada):
        print('A espada é a melhor opção!')
    elif arco_adequado and (not espada_adequada and not lança_adequada):
        print('O arco é a melhor opção!')
    elif lança_adequada and (not espada_adequada and not arco_adequado):
        print('A lança é a melhor opção!')
    elif espada_adequada and arco_adequado and not lança_adequada:
        print('A espada e o arco são boas opções!')
    elif espada_adequada and lança_adequada and not arco_adequado:
        print('A espada e a lança são boas opções!')
    elif arco_adequado and lança_adequada and not espada_adequada:
        print('O arco e a lança são boas opções!')
    elif espada_adequada and arco_adequado and lança_adequada:
        print('Todas as armas são boas opções!')
    else:
        print('Nenhuma presta. Busque uma nova arma.')

if __name__ == '__main__':
    # Mensagem de início do programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")
