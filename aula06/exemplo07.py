usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    usuario = {"nome": nome, "idade": idade, "email": email}
    usuarios.append(usuario)

def exibir_usuarios():
    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")

while True:
    cadastrar_usuario()
    continuar = input("Deseja cadastrar outro usuário? (s/n): ")
    if continuar.lower() != 's':
        break

exibir_usuarios()
