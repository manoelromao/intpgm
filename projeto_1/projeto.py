import requests
from deep_translator import GoogleTranslator

# --===== Função para consumir a API de conselhos =====--
def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code == 200:
        advice = response.json()["slip"]
        return advice["id"], advice["advice"]
    else:
        return None, "Erro ao acessar a API."

# --===== Função para salvar conselhos em um arquivo =====--
def save_advice_to_file(advice_list, filename="conselhos.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for advice_id, advice in advice_list:
            file.write(f"{advice_id} | {advice}\n")

# --===== Função para ler conselhos salvos =====--
def read_saved_advice(filename="conselhos.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# --===== Função para traduzir texto =====--
def translate_text(text, target_language="pt"):
    translator = GoogleTranslator(source="auto", target=target_language)
    return translator.translate(text)

# --===== Função principal do menu =====--
def main_menu():
    while True:
        print("\nMenu do Seu Zé:")
        print("1. Ouvir o Seu Zé (Receber conselhos)")
        print("2. Mostrar os Conselhos")
        print("3. Guardar a Sabedoria (Salvar conselhos)")
        print("4. Mostrar os Conselhos guardados")
        print("5. Traduzir para o 'Gringo'")
        print("6. Relembrar as Dicas (Traduzir conselhos salvos)")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            count = int(input("Quantos conselhos deseja receber? "))
            conselhos = [get_advice() for _ in range(count)]
            for i, (advice_id, advice) in enumerate(conselhos, 1):
                print(f"\nConselho {i} (ID: {advice_id}): {advice}")
        
        elif choice == "2":
            conselhos = read_saved_advice()
            if conselhos:
                print("\nConselhos mágicos:")
                for conselho in conselhos:
                    print(conselho.strip())
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif choice == "3":
            count = int(input("Quantos conselhos deseja salvar? "))
            conselhos = [get_advice() for _ in range(count)]
            save_advice_to_file(conselhos)
            print("Conselhos salvos com sucesso!")
        
        elif choice == "4":
            conselhos = read_saved_advice()
            if conselhos:
                print("\nConselhos salvos:")
                for conselho in conselhos:
                    print(conselho.strip())
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif choice == "5":
            text = input("Digite o texto que deseja traduzir: ")
            translated = translate_text(text)
            print(f"\nTexto traduzido: {translated}")
        
        elif choice == "6":
            conselhos = read_saved_advice()
            if conselhos:
                print("\nConselhos salvos:")
                for i, conselho in enumerate(conselhos, 1):
                    print(f"{i}. {conselho.strip()}")
                idx = int(input("Escolha o número do conselho para traduzir: ")) - 1
                if 0 <= idx < len(conselhos):
                    original = conselhos[idx].split("|")[1].strip()
                    translated = translate_text(original)
                    print(f"\nConselho original: {original}")
                    print(f"Conselho traduzido: {translated}")
                else:
                    print("Opção inválida!")
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif choice == "0":
            print("Até logo, Seu Zé!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
