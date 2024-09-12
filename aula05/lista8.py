# Função de processamento do programa
def funcao_processamento(bonus):
    if bonus > 10:
        print('Parabéns, você ganhou 100 moedas de ouro!')
    
    elif 5 < bonus <= 10:
        print('Parabéns, você ganhou 50 moedas de ouro!')
    
    else:
        print('Parabéns, você ganhou 10 moedas de ouro!')

bonus = int(input('Digite a quantidade de missões: '))
    
if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento(bonus)

    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")