#Calculadora:

#Solicitar o primeiro número da operação:
num1 = float(input("Digite o primeiro número:"))

#Solicitar o segundo número da operação:
num2 = float(input("Digite o segundo número:"))

#Solicitar a operação desejada:
operacao = input("Escolha a operação: ( +, -, *, / ):")

#Realizar a operação:
if operacao == "+": 
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
    #Verificar se o divisor é "0"
    if num2 !=0: 
        resultado= num1 / num2
    else: 
         resultado = "Erro de divisão! divisão por zero, não é permitida!."
else: 
    resultado = "Operação inválida!" 

#Exibir Resultado
print("Resultado:", resultado)
