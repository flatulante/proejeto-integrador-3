import sqlite3

class DAO(object):

	@staticmethod
	def criar_bd():
		conn = sqlite3.connect('perguntas.db')

		cursor = conn.cursor()

		cursor.execute("""
		CREATE TABLE perguntas (
			nmr_questao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			tema varchar(20) NOT NULL,
			pergunta varchar(100) NOT NULL,
			resposta1 varchar(100) NOT NULL,
			resposta2 varchar(100) NOT NULL,
			resposta3 varchar(100) NOT NULL,
			resposta4 varchar(100) NOT NULL,
			dificuldade int NOT NULL);
			""")

		print("Tabela criada com sucesso")
		cursor.execute("select * from perguntas")

		arq = open("arquivo.txt", "r")

		for i in arq:
			b = arq.readline()
			cursor.execute(b)
			print(b)
		arq.close()
		conn.commit()

		cursor.execute("""

		SELECT * FROM perguntas;
		""")

		for linha in cursor.fetchall():
			print(linha)

	