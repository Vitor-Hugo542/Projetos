
nota = float(input("Digite sua nota: "))

match nota:
    case n if n >= 7:
        print(f"Aprovado! Média: {nota}")
    case n if n < 7 and n > 5:
        print(f"Recuperação! Média: {nota}")
    case n if n < 5:
        print(f"REPROVADO! Média: {nota}")
           