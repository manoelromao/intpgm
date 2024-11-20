vet = []
for i in range(10):
    num = int(input(f"Digite o número na posição {i}: "))
    vet.append(num)

posicoes = {}

for i in range(len(vet)):
    if vet[i] in posicoes:
        posicoes[vet[i]].append(i)
    else:
        posicoes[vet[i]] = [i]

repetidos = False
for numero, pos in posicoes.items():
    if len(pos) > 1:
        print(f"O número {numero} é repetido nas posições {pos}")
        repetidos = True

if not repetidos:
    print("Não existem números repetidos no vetor.")
