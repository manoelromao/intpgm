def enviar_convites(arquivo):
    try:
        with open(arquivo, 'r') as file:
            vingadores = file.readlines()
        
        for vingador in vingadores:
            vingador = vingador.strip() 
            if vingador:  
                mensagem = f"Olá {vingador}, você está convidado para uma festa na minha casa!"
                print(mensagem)
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo = 'vingadores.txt'
enviar_convites(arquivo)
