def calculadora_media_notas():
    notas = []
    
    while (nota := float(input("Digite uma nota (ou -1 para encerrar): "))) != -1:
        notas.append(nota)
    
    print(f"Média: {sum(notas) / len(notas):.2f}" if notas else "Nenhuma nota foi inserida.")

calculadora_media_notas()
