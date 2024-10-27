convidados = ["Djavan", "Reginaldo Rossi", "Roberto Carlos", "Waldick Soriano", "Fernando Mendes"]

mensagem_convite = "Olá {nome}, você está convidado para um jantar em minha casa!"

print("Convites enviados:")
for convidado in convidados:
    print(mensagem_convite.format(nome=convidado))

desistentes = ["Reginaldo Rossi", "Waldick Soriano"]

print("\nDesistentes:")
for desistente in desistentes:
    print(desistente)

for desistente in desistentes:
    convidados.remove(desistente)

novos_convidados = ["Nelson Gonçalves", "José Augusto"]
convidados.extend(novos_convidados)

print("\nNovos convites enviados:")
for convidado in convidados:
    print(mensagem_convite.format(nome=convidado))
