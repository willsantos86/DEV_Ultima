import sqlite3
conexao = sqlite3.connect('banco_dados_ultima')
nome = input('Qual é o seu nome? ')
cpf = input('Digite o CPF: ')
valores = [nome, cpf]
sql_inserir = 'INSERT into cliente (nome, cpf) VALUES (?, ?)'
cursor = conexao.cursor()
cursor. execute(sql_inserir, valores)
#cursor.execute('CREATE TABLE cliente(id INT, nome VARCHAR(100), cpf VARCHAR(100)UNIQUE);')
conexao.commit()
conexao.close()
