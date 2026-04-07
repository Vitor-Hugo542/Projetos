print("="*12 + " CADASTRO " + "="*11)
usuario_correto = str(input("Digite um nome: "))
senha_correta = str(input("Crie uma senha: "))


print("=== 🔐 SISTEMA DE ACESSO SENAI ===")

usuario_escrito = str(input("Digite o usuário: "))
senha_escrita = str(input("Digite a senha: "))

if(usuario_escrito != usuario_correto or senha_escrita != senha_correta):
    print("Usuário ou senha incorreto(s)!")
else:
    print("Acesso permitido!")
