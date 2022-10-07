import sqlite3
conexao = sqlite3.connect('banco_dados_familia')
id = input('Qual o ID? ')
nome = input('Qual é o seu nome? ')
time = input('Qual o time de coração? ')
valores = [id, nome,time]
sql_inserir = 'INSERT into familia (id, nome, time) VALUES (?,?,?)'
cursor = conexao.cursor()
cursor. execute(sql_inserir, valores)
#cursor.execute('CREATE TABLE familia(id INT, nome VARCHAR(100), idade VARCHAR(100), time VARCHAR(100));')
conexao.commit()
conexao.close()
