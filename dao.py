from sqlite3 import connect
import os
class DAO(object):
	""" 
	A classe DAO é uma classe composta por métodos estáticos que buscam realizar acessos ao banco de dados.
	"""

	filename = 'storage.db'
	filename_tabelas = 'arquivo.txt'


	@staticmethod
	def criar_bd():
		""" 
		O método estático criar_bd realiza a criação de um banco de dados e suas tabelas em SQLite 3.
		"""
		if os.path.exists(DAO.filename):
			os.remove(DAO.filename)
		DAO.criar_conexao()

		DAO.cursor.execute(" \
			CREATE TABLE perguntas ( \
			nmr_questao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
			tema varchar(20) NOT NULL,  \
			pergunta varchar(100) NOT NULL, \
			resposta1 varchar(100) NOT NULL, \
			resposta2 varchar(100) NOT NULL, \
			resposta3 varchar(100) NOT NULL, \
			resposta4 varchar(100) NOT NULL, \
			dificuldade int NOT NULL); \
			")
		
		print("Tabela criada com sucesso")
		for linha in DAO.pegar_perguntas_all():
			print(linha)

		#arq = open(DAO.filename_tabelas, "r")
		arq = open("arquivo.txt", "r")

		DAO.criar_conexao()
		for i in arq:
			b = arq.readline()
			DAO.cursor.execute(b)
			print(b)
		arq.close()
		
		DAO.fechar_conexao()
		for linha in DAO.pegar_perguntas_all():
			print(linha)

	@staticmethod
	def criar_conexao():
		DAO.conn = connect(DAO.filename)
		DAO.cursor = DAO.conn.cursor()


	@staticmethod
	def fechar_conexao():
		DAO.conn.commit()
		DAO.cursor.close()
		DAO.conn.close()


	@staticmethod
	def pegar_perguntas(tema):
		sql = "SELECT * FROM perguntas WHERE lower(tema) = '%s'" %(tema.lower())
		DAO.cursor.execute(sql)
		DAO.lista = DAO.cursor.fetchall()
		return DAO.lista


	@staticmethod
	def pegar_perguntas_all():
		DAO.criar_conexao()
		DAO.cursor.execute("SELECT * FROM perguntas")
		lista = DAO.cursor.fetchall()
		DAO.fechar_conexao()
		return lista

if __name__ == '__main__':
	DAO.criar_bd()
