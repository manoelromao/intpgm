import requests
from deep_translator import GoogleTranslator


def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code == 200:
        advice = response.json()["slip"]
        return advice["id"], advice["advice"]
    else:
        return None, "Erro ao acessar a API."


def save_advice_to_file(advice_list, filename="conselhos.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for advice_id, advice in advice_list:
            file.write(f"{advice_id} | {advice}\n")


def read_saved_advice(filename="conselhos.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def translate_text(text, target_language="pt"):
    translator = GoogleTranslator(source="auto", target=target_language)
    return translator.translate(text)


def save_translated_advice(advice, filename="conselhos_traduzidos.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(advice + "\n")


def read_translated_advice(filename="conselhos_traduzidos.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def main_menu():
    while True:
        print("\nMenu do Seu Zé:")
        print("1. Ouvir o Seu Zé (Receber conselhos traduzidos)")
        print("2. Mostrar os Conselhos (em português)")
        print("3. Guardar a Sabedoria (Salvar conselhos)")
        print("4. Traduzir conselhos salvos para outro idioma")
        print("5. Mostrar conselhos traduzidos")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            count = int(input("Quantos conselhos deseja receber? "))
            conselhos = [get_advice() for _ in range(count)]
            translated_conselhos = []
            for i, (advice_id, advice) in enumerate(conselhos, 1):
                if advice_id is not None:  
                    translated_advice = translate_text(advice, target_language="pt")
                    print(f"\nConselho {i} (ID: {advice_id}): {translated_advice}")
                    translated_conselhos.append((advice_id, translated_advice))
                else:
                    print(f"\nConselho {i}: Erro ao buscar o conselho.")
            save_advice_to_file(translated_conselhos)
        
        elif choice == "2":
            conselhos = read_saved_advice()
            if conselhos:
                print("\nConselhos em português:")
                for conselho in conselhos:
                    print(conselho.strip().split("|")[1])  
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif choice == "3":
            count = int(input("Quantos conselhos deseja salvar? "))
            conselhos = [get_advice() for _ in range(count)]
            translated_conselhos = [(advice_id, translate_text(advice, target_language="pt")) for advice_id, advice in conselhos if advice_id is not None]
            save_advice_to_file(translated_conselhos)
            print("Conselhos traduzidos e salvos com sucesso!")
        
        elif choice == "4":
            conselhos = read_saved_advice()
            if conselhos:
                print("\nConselhos salvos:")
                for i, conselho in enumerate(conselhos, 1):
                    print(f"{i}. {conselho.strip()}")
                idx = int(input("Escolha o número do conselho para traduzir: ")) - 1
                if 0 <= idx < len(conselhos):
                    original = conselhos[idx].split("|")[1].strip()
                    target_language = input("Para qual idioma deseja traduzir? (Ex: en, es, fr): ")
                    translated = translate_text(original, target_language=target_language)
                    print(f"\nConselho original: {original}")
                    print(f"Conselho traduzido ({target_language}): {translated}")
                    save_translated_advice(f"{original} -> {translated} ({target_language})")
                else:
                    print("Opção inválida!")
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif choice == "5":
            traducoes = read_translated_advice()
            if traducoes:
                print("\nConselhos traduzidos na opção 4:")
                for traducao in traducoes:
                    print(traducao.strip())
            else:
                print("Nenhuma tradução realizada ainda!")
        
        elif choice == "0":
            print("Até logo, Seu Zé!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
