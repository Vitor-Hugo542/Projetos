while True:
    comando = str(input("Digite a ação que deseja realizar: ")).lower()


    match comando:
        case "salvar": 
            print("Salvando o seu game ...")
        case "carregar":
            print("Carregando save game...")
        case "sair":
            print("Leave game...")
        case _:
            print("Comando iválido! Try again.")
    break    
                    