# Função de processamento do programa
def funcao_processamento(desafio):
   match desafio:
       case 1:
           return "Seu desafio será enfrentar um dragão!"
       case 2:
           return "Seu desafio será enfrentar um golem!"
       case 3:
           return "Seu desafio será enfrentar uma aranha gigante!"
       case 4:
            return "Seu desafio será enfrentar um zumbi!"
       case 5:
            return "Seu desafio será enfrentar um cérbero!"
       case _:
           return "Porta Inválida, Escolha 1 para Porta 1, 2 para Porta 2, 3 para Porta 3, 4 para Porta 4 ou 5 para Porta 5."
    
try:
       escolha = int(input("Escolha uma Porta: Escolha 1 para Porta 1, 2 para Porta 2, 3 para Porta 3, 4 para Porta 4 ou 5 para Porta 5.):"))
       resultado = funcao_processamento(escolha)
       print(resultado)
    
except ValueError:
       print('Escolha inválida, insira uma opção.')
   
      
        
if __name__ == '__main__':

    # Mensagem de inicio de programa
    print("--- --- Iniciando Programa --- ---")

    # Processando realizado pelo programa
    funcao_processamento(escolha)
    # Mensagem de fim do programa
    print("--- --- Fim do Programa --- ---")