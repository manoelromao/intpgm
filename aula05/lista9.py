# Função de processamento do programa
def funcao_processamento(feitico):
   match feitico:
       case 1:
           return "Feitiço Escolhido: Fogo"
       case 2:
           return "Feitiço Escolhido: Água"
       case 3:
           return "Feitiço Escolhido: Terra"
       case _:
           return "Feitiço Inválido, Escolha 1 para Fogo, 2 para Água ou 3 para Terra"
    
try:
       escolha = int(input("Escolha um feitiço (1 para Fogo, 2 para Água, 3 para Terra):"))
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