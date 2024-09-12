def funcao_processamento():
    energia = float(input("Digite o valor da energia (em %): "))
    coordenadas = input("Digite as coordenadas de destino: ")
    tempo = input("Digite o estado do tempo: ")

    energia_correta = energia > 80
    coordenadas_certas = coordenadas == "preciso"
    tempo_ajustado = tempo == "ajustado"

    if energia_correta and coordenadas_certas and tempo_ajustado:
        print("O portal pode ser ativado.")
    else:
        if not energia_correta:
            print("A energia está abaixo de 80%.")
        if not coordenadas_certas:
            print("As coordenadas de destino estão incorretas.")
        if not tempo_ajustado:
            print("O tempo não está ajustado corretamente.")

if __name__ == '__main__':
    # Mensagem de início do programa
    print("--- --- Iniciando Programa --- ---")

    # Processa a ativação do portal
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")
