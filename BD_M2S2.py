#Criação de tabelas no Banco de Dados SQLite3.

import sqlite3
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE tarefas (id INT NOT NULL PRIMARY KEY, 
nome VARCHAR(100), 
data DATE, 
categoria VARCHAR(30), 
concluído TEXT CHECK( concluído IN ('S','N') ));''')

cursor.execute('''CREATE TABLE eventos (id INT NOT NULL, 
titulo VARCHAR(100), 
data DATE, 
local VARCHAR(100),
organizador_id INT NOT NULL, 
PRIMARY KEY (id), 
FOREIGN KEY (organizador_id)REFERENCES organizador (id));''')

cursor.execute('''CREATE TABLE organizador (id INT NOT NULL, 
nome VARCHAR(100), 
email VARCHAR(100), 
cpf VARCHAR(11) UNIQUE, 
PRIMARY KEY (id));''')
conexao.commit()
conexao.close()