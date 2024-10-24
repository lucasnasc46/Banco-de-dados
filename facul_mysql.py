import mysql.connector
from mysql.connector import Error

def conectarBd():

    try:
        conn = mysql.connector.connect(
            host ='localhost',
            user='root',
            password='admsys2811',
            database='faculdade'
        )

        if conn.is_connected():
            return conn
    
    except Error as e:
        print(f"ERRO: {e}")
        return None
    
def salvaAluno(nome, cpf, email):

    conn = conectarBd()

    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute('''
            INSERT INTO alunos (nome, cpf, email)
            VALUES (%s, %s, %s)
            ''', (nome, cpf, email))
            
            conn.commit()
            print ("Aluno cadastrado com sucesso! ")

        except Error as e:
            print(f"ERRO: {e}")

        finally:
            cursor.close()
            conn.close()

def exibir():
    conn = conectarBd()
    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM alunos')
            alunos = cursor.fetchall()

            if alunos:
                print ("\nAlunos cadastrados: ")
                print("----------")

                for aluno in alunos:
                    print(f"Matricula: {aluno[0]}")
                    print(f"Nome: {aluno[1]}")
                    print(f"CPF: {aluno[2]}")
                    print(f"e-mail: {aluno[3]}")
                    print("-------------------------")

            else:
                print("Nenhum aluno cadastrado")

        except Error as e:
            print(f"ERRO: {e}")

        finally:
            cursor.close()
            conn.close()

def cadastraAluno():
    
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    email = input("Digite o email: ")

    return nome, cpf, email

op = input("Digite c para cadastrar e e para exibir: ")

if op == 'c':
    nome, cpf, email =cadastraAluno()
    salvaAluno(nome, cpf, email)

elif op == 'e':
    exibir()

else:
    print("opcao invalida")

