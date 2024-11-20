import random

A = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]

soma = sum(sum(linha) for linha in A)
print("Soma de todos os valores da matriz A:", soma)

B = [[A[i][j] * 3 for j in range(10)] for i in range(10)]

print("Matriz B (valores de A * 3):")
for linha in B:
    print(linha)
