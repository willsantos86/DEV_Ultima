#%%
import sqlite3

#%%
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor (id INT, nome VARCHAR(100), endereco VARCHAR(250));')
conexao.commit()
conexao.close()
# %%
import sqlite3

conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE cliente (id INT, nome VARCHAR(100), cpf VARCHAR(11), data_de_cadastro DATE, endereco VARCHAR(250));')
conexao.commit()
conexao.close()

# %%
