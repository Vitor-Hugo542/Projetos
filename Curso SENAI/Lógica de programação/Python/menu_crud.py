import sqlite3

#Conectando ao banco de dados
conn = sqlite3.connect("bd_senai")
cursor = conn.cursor()

# Criando a tabela com o campo id
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota INTEGER                        
               )"""
    )
# --- Adicionando aluno via input do usuário ---
print("\n --- Adicionr novo aluno ---")
nome_novo_aluno = input("Digite o nome do novo aluno: ")
while True:
    try:
        nota_novo_aluno = int(input("Digite a nota do novo aluno (Número inteiro): "))
        break
    except ValueError:
        print("Entrada inválidal. Por favor digite um número inteiro para a nota.")

cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)",(nome_novo_aluno, nota_novo_aluno))

conn.commit()

print(f"Aluno {nome_novo_aluno} com a nota {nota_novo_aluno} adicionando com sucesso ao banco de dados!\n")

print("=== Dados da tabela (sem ordenação) ===\n")
cursor.execute("SELECT * FROM alunos ORDER BY 2 ASC")
alunos = cursor.fetchall()

#for aluno in alunos:
#    print(aluno) # mostra (id, nome, nota)
#print("\n" + "="*50)

print("\n. FOR simples mostrando nome e nota: ")

for aluno in alunos: 
    print(f"ID: {aluno[0]} {aluno[1]} nota {aluno[2]}")