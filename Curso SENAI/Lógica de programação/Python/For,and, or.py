for tentativa in range (1,4):
    usuario_correto =  str("Vitor")
    senha_correta = 2008
    
    
    usuario = input(f"Digite seu usuario(tentativa{tentativa}/3)").strip()
    senha = input(f"Digite sua senha(tentativa{tentativa}/3)").strip()
    if usuario == usuario_correto or senha == senha_correta:
        print(f"Olá, {usuario}! Tudo bem?")
        break
    print("Você digitou usuario ou senha incorreto!")
else:
    #Só roda se esgotou as 3 tentativas
    print("Tentativas esgotadas")