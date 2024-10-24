import sqlite3
import os

if os.path.exists('faculdade.db'):
    os.remove('faculdade.db')

conn = sqlite3.connect('faculdade.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INT PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR[50],
    cpf var[11],
    email VARCHAR[50]
)
''')

conn.commit()
conn.close()