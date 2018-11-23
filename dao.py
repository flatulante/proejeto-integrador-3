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
		DAO.fechar_conexao()
		print("Tabela criada com sucesso")
		for linha in DAO.pegar_perguntas_all():
			print(linha)

		#arq = open(DAO.filename_tabelas, "r")
		
		arq = [
			("Plantas", "Qual e o nome do grupo de plantas mais primitivo da terra?", "Angiospermas", "Pteridofitas", "Gimnospermas", "Briofitas", 0),
			("Plantas", "Como e chamado o caule horizontal da maioria das plantas pteridofitas?", "Rizomatla", "Horizontado", "Cauloide", "Rizoma", 1),
			("Plantas", "Como sao chamados os dois tipos de vasos vasculares existentes nas plantas?", "xilema e atemia", "xilema e veia", "xilema e cloroplasto ", "xilema e floema", 1),
			("Plantas", "sao caracteristicas das plantas:", "Autotrofos, unicelulares e procariontes", "Heterotrofos, pluricelulares e procariontes", "Autotrofos, unicelulares e procariontes", "Autotrofos, pluricelulares e eucariontes", 2),
			("Plantas", "Quais dessa especies sao exemplos de briofitas (grupo de plantas)?", "Laranjeira e mangueira", "Samambaia e pinheiro", "abacateiro e sambaiacu", "Musgos e hepaticas", 0),
			("Plantas", "Qual e o tipo de caule da bananeira?", "caule espinhoso", "caule aquatico", "caule musgoso", "caule subterraneo", 1),
			("Matematica", "Quanto é 1+1?", "1", "3", "4", "2", 0)
		]
		DAO.inserir_pergunta(arq)

		for linha in DAO.pegar_perguntas_all():
			print(linha)



	@staticmethod
	def inserir_pergunta(lista):
		DAO.criar_conexao()
		DAO.cursor.executemany("INSERT INTO perguntas (tema, pergunta, resposta1, resposta2, resposta3, resposta4, dificuldade) VALUES (?, ?, ?, ?, ?, ?, ?)", lista)
		DAO.fechar_conexao()


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