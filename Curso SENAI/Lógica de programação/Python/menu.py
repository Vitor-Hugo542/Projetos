#Inicializamos a váriavel opção
opcao = 0

while opcao != 3:
    print("\n--- Menu do Sistema ---")
    print("\n1. Saudação")
    print("\n2. Informações do Sistema")
    print("\n3. Sair")

    # Recebendo entrada do usuário

    try: 
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Por favor digite apenas números!")

        # Estruturas de Decisão
    if opcao == 1:
            print("\nOlá! É um prazer ajuda-lo.")
    elif opcao == 2:
            print("\nSistema: Python 3.10")
            print("\nStatus: Operacional")
    elif opcao == 3:
            print("\nSaindo... até logo!")
    else:
            print("\nOpção inválida! Tente novamente.")