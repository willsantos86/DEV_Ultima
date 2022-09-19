#%%
#Importando pacote.
import sqlite3

#%%
#Criando a Tabela Fornecedor.
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor (id INT, nome VARCHAR(100), endereco VARCHAR(250));')
conexao.commit()
conexao.close()
# %%
#Criando a Tabela Cliente.
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE cliente (id INT NOT NULL, nome VARCHAR(100), cpf VARCHAR(250) UNIQUE, PRIMARY KEY(ID));')
conexao.commit()
conexao.close()

# %%
#Criando a Tabela Consulta.
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE consulta (id INT, medico_crm VARCHAR(10), horario VARCHAR(20), UNIQUE (medico_crm, horario));')
conexao.commit()
conexao.close()
# %%
#Criando a Tabela Categoria.
conexao = sqlite3.connect('BD_SQLite')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE categoria (id INT NOT NULL, nome VARCHAR(100), PRIMARY KEY (id));')
cursor.execute('CREATE TABLE produto (id INT NOT NULL, nome VARCHAR(100), categoria_id INT NOT NULL, PRIMARY KEY (id), FOREIGN KEY (categoria_id)REFERENCES categoria (id));')
conexao.commit()
conexao.close()
# %%
