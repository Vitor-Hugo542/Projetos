print("="*20 + " Lanchonete SENAI " + "="*20)

nome_usuario=input("Por favor, digite seu nome: ")
print(f"Seja bem vindo a nossa cantina {nome_usuario}!")
print("-"*55)
print("\n==== NOSSO CARDÁPIO ====")
print(f"\n1. Hambúrger Clássico: R$22.80")
print(f"2. Refrigerantes: R$8.50")

total_burguer = int(input("\nQuantos hamburgueres você deseja? "))
total_refri = int(input("Quantos refrigerantes você deseja? "))


valor_burguer = float(total_burguer * 22.90)
valor_refri = float(total_refri * 8.50)

total = valor_burguer + valor_refri
print("-"*55)
print(" "*15 + "CUPOM FISCAL" + " "* 15)

print(f"Nome cliente : {nome_usuario}")
print(f"Total Hambúrgeres: {total_burguer} X R$22.80 = R${total_burguer * 22.80}")
print(f"Total Refris: {total_refri} X R$8.50 = R${total_refri * 8.50}")
print(f"Total: R${total}\nEspero que goste, volte sempre!")
