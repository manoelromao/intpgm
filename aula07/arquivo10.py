import random

def simular_lancamento_dados(num_lancamentos):
    resultados = []
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6)  
        resultados.append(resultado)
    return resultados

num_lancamentos = int(input("Quantas vezes você deseja lançar o dado? "))

resultados = simular_lancamento_dados(num_lancamentos)
print("Resultados dos lançamentos:", resultados)
