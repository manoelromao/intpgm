# 1- Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).
def verificar_valor():
    valor_str = input("Digite um valor numérico (inteiro ou real): ")
    
    try:
        valor = float(valor_str)
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico.")
        return
    
    if valor >= 0:
        print("O valor é positivo.")
    else:
        print("O valor é negativo.")

verificar_valor()
