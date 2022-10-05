
import sqlite3

conexao = sqlite3.connect('bancotest.sqlite')
sql_cliente = '''
CREATE TABLE Cliente (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    cpf TEXT(14) NOT NULL,
    CONSTRAINT cliente_UN UNIQUE(cpf)
    );
    
'''
cursor = conexao.cursor()
cursor.execute(sql_cliente)

conexao = sqlite3.connect('bancotest.sqlite')
sql_pedido = '''
CREATE TABLE Pedido(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
"data" TEXT(20) NOT NULL,
cliente_id INTEGER NOT NULL,
CONSTRAINT pedido_FK FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);
'''
cursor.execute(sql_pedido)




conexao = sqlite3.connect('bancotest.sqlite')
sql_item_pedido = '''
CREATE TABLE Item_pedido(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
pedido_id INTERGER NOT NULL,
produto TEXT(100),
valor REAL,
quantidade INTEGER,
CONSTRAINT item_pedido_FK FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
'''
cursor.execute(sql_item_pedido)

conexao.commit()
conexao.close()


import sqlite3
conexao = sqlite3.connect('bancotest.sqlite')
print("insira os dados do cliente: ")
nome = input("Qual o nome do cliente? ")
cpf = input("Qual o cpf do cliente? ")
valores = [nome, cpf]
sql_inserir = 'insert into cliente (nome, cpf) values (?,?)'
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()


