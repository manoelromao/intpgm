# 2- Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

def calcular_custo():
    num_macas = input("Digite o número de maçãs compradas: ")
    
    try:
        num_macas = int(num_macas)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    if num_macas < 12:
        preco_unitario = 1.30
    else:
        preco_unitario = 1.00
    
    custo_total = num_macas * preco_unitario
    
    print(f"O custo total da compra é R$ {custo_total:.2f}")

calcular_custo()
