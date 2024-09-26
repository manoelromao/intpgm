frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

count_vogais = sum(1 for char in frase if char in vogais)
count_consoantes = sum(1 for char in frase if char in consoantes)

print(f"Número de vogais: {count_vogais}")
print(f"Número de consoantes: {count_consoantes}")