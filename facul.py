import sqlite3
import os

db_path = 'faculdade.db'

def exibir():
    try:

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM alunos')
        alunos = cursor.fetchall()

        if alunos:
            print("\nAlunos cadastrados: ")

            for aluno in alunos:
                print(f"matricula: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"CPF: {aluno[2]}")
                print(f"Email: {aluno[3]}")
                print("-----------------------------------")
        
        else:
            print("Nenhum aluno cadastrado")

    except sqlite3.DatabaseError as e:
        print(f"EROO {e}")

    finally:
        conn.close()

def criar_tabela():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL
        
    )
    ''')
    
    conn.commit()  
    conn.close()   

def salvar_aluno(nome, cpf, email):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO alunos(nome,cpf, email)
        values (?,?,?,?)
                       ''', (nome, cpf, email))
        
        conn.commit()
        print("Aluno cadastrado com sucesso!")

    except sqlite3.DatabaseError as e:
        print(f"ERRO ao cadastrar: {e}")

    finally:
        conn.close()

def cadastro():

    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF, apenas numeros ")
    email = input("digite o email: ")
    return nome, cpf, email

criar_tabela()

op = input("digite 1 para cadastra e 2 para exibir: ")

if op =='1':
    nome, cpf, email = cadastro()
    salvar_aluno(nome, cpf, email)

elif op =='2':
    exibir()

else:
    print("entrada invalida")