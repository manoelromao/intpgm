import requests
from googletrans import Translator

def buscar_conselhos_traduzidos():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            conselho = response.json()["slip"]["advice"]
            log_acao(f"Conselho recebido: {conselho}")
            return traduzir_para_portugues(conselho)
        else:
            log_acao("Erro ao acessar a API de conselhos.")
            return "Erro ao acessar a API."
    except Exception as e:
        log_acao(f"Erro ao buscar conselhos: {e}")
        return "Erro ao buscar conselhos."


def salvar_conselhos(lista_conselhos, filename="conselhos.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            for conselho in lista_conselhos:
                file.write(f"{conselho}\n")
                log_acao(f"Conselho salvo: {conselho}")
        print("Conselhos salvos com sucesso!")
    except Exception as e:
        log_acao(f"Erro ao salvar conselhos: {e}")


def ler_conselhos_salvos(filename="conselhos.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        log_acao("Arquivo de conselhos não encontrado.")
        return []
    except Exception as e:
        log_acao(f"Erro ao ler conselhos salvos: {e}")
        return []


def traduzir_para_portugues(text):
    try:
        translator = Translator()
        traducao = translator.translate(text, src="en", dest="pt")
        return traducao.text
    except Exception as e:
        log_acao(f"Erro ao traduzir texto: {e}")
        return "Erro ao traduzir."


def log_acao(acao):
    print(f"[LOG] {acao}")


def menu():
    while True:
        print("\nMenu do Seu Zé:")
        print("1. Ouvir o Seu Zé (Receber conselhos traduzidos)")
        print("2. Mostrar os Conselhos")
        print("3. Guardar a Sabedoria (Salvar conselhos)")
        print("4. Mostrar os Conselhos guardados")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        log_acao(f"Opção selecionada: {escolha}")

        if escolha == "1":
            try:
                count = int(input("Quantos conselhos deseja receber? "))
                conselhos = [buscar_conselhos_traduzidos() for _ in range(count)]
                for i, conselho in enumerate(conselhos, 1):
                    print(f"\nConselho {i}: {conselho}")
                log_acao(f"{count} conselhos exibidos.")
            except ValueError:
                log_acao("Erro: Entrada inválida para o número de conselhos.")

        elif escolha == "2":
            conselhos = ler_conselhos_salvos()
            if conselhos:
                print("\nConselhos salvos:")
                for conselho in conselhos:
                    print(conselho.strip())
            else:
                print("Nenhum conselho salvo ainda!")

        elif escolha == "3":
            try:
                count = int(input("Quantos conselhos deseja salvar? "))
                conselhos = [buscar_conselhos_traduzidos() for _ in range(count)]
                salvar_conselhos(conselhos)
            except ValueError:
                log_acao("Erro: Entrada inválida para o número de conselhos.")

        elif escolha == "4":
            conselhos = ler_conselhos_salvos()
            if conselhos:
                print("\nConselhos salvos:")
                for conselho in conselhos:
                    print(conselho.strip())
            else:
                print("Nenhum conselho salvo ainda!")

        elif escolha == "0":
            log_acao("Saindo do programa.")
            print("Até logo, Seu Zé!")
            break

        else:
            log_acao("Erro: Opção inválida selecionada.")
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
