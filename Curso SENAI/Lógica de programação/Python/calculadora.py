print("="*15 + " CALCULADORA " + "="*15)
n1 = float(input("Digite um número: "))
operador = str(input("Digite a operação: "))
n2 = float(input("Digite o segundo numero: "))

if(operador == "+"):
    print(f"RESULTADO: {n1 + n2}")
elif(operador == "-"):
    print(f"RESULTADO: {n1 - n2}")
elif(operador == "*"):
    print(f"RESULTADO: {n1 * n2}")
elif(operador == "/"):
    print(f"RESULTADO: {n1 / n2}")


