import os, random, time, platform
from dao import DAO

def input_int(mensagem, minimo=None, maximo=None):
    valido = False
    while not valido:
        try:
            numero = int(input(mensagem))
            if minimo is not None:
                if numero < minimo:
                    raise ValueError()
            if maximo is not None:
                 if numero > maximo:
                     raise ValueError()
        except ValueError as identifier:
            print(' Valor inválido!')
        else:
            valido = True
    return numero

class Perguntas():
	
    def __init__(self, jogador):
        self.jogador = jogador
        self.temas = [
            [0, "Plantas"],
            [1, "Reino Vegetal I"],
            [2, "DNA e RNA - I"],
            [3, "Genética - I"],
            [4, "Simulado do Enem - Biologia Celular"]
        ]
        tema = self.definirTema()
        self.perguntas = self.pegarPerguntas(tema)
        self.jogo()


    def pegarPerguntas(self, tema):
        DAO.criar_conexao()
        sql = "SELECT * FROM perguntas WHERE lower(tema) = '%s'" %(tema.lower())
        DAO.cursor.execute(sql)
        self.lista = DAO.cursor.fetchall()
        DAO.fechar_conexao()
        return self.lista

    def limpar(self):
        if platform.system() == 'Windows':
            os.system("cls")
        elif platform.system() == 'Linux':
            os.system("clear")
        else:
            return "Error"

    def definirTema(self):
        print("Escolha um dos numeros que corresponde ao tema:")
        for x in self.temas:
            print("%i - %s" %(x[0], x[1]))
        
        tema = input_int('Número: ', 0, len(self.temas))
        return self.temas[tema][1]


    def jogo(self):
        perdeu = False
        self.pontuacao = 0
        self.pergunta = 0
        self.max_pergunta = len(self.perguntas)-1
        alternativas = [3,4,5,6]
        pontos = [10, 20, 30]
        while not perdeu:
            try:
                self.limpar()
                print("Pergunta %i/%i | Pontuação = %i" %(self.pergunta, self.max_pergunta+1, self.pontuacao))
                print("%i) %s" %(self.perguntas[self.pergunta][0], self.perguntas[self.pergunta][2]))
                alt_a = random.choice(alternativas)

                if alt_a == 6:
                    resposta = "a"
                    alternativas.remove(alt_a)
                print("a) %s" %(self.perguntas[self.pergunta][alt_a]))
                if alt_a in alternativas:
                    alternativas.remove(alt_a)
                alt_b = random.choice(alternativas)
                if alt_b == 6:
                    resposta = "b"
                    alternativas.remove(alt_b)
                print("b) %s" %(self.perguntas[self.pergunta][alt_b]))
                if alt_b in alternativas:
                    alternativas.remove(alt_b)
                alt_c = random.choice(alternativas)
                if alt_c == 6:
                    resposta = "c"
                    alternativas.remove(alt_c)
                print("c) %s" %(self.perguntas[self.pergunta][alt_c]))
                

                if alt_c in alternativas:
                    alternativas.remove(alt_c)
                alt_d = random.choice(alternativas)
                if alt_d == 6:
                    resposta = "d"
                    alternativas.remove(alt_d)
                print("d) %s" %(self.perguntas[self.pergunta][alt_d]))
                if alt_d in alternativas:
                    alternativas.remove(alt_d)
                respost = input("Alternativa: ")
                if self.pergunta == self.max_pergunta:
                    self.pontuacao += pontos[self.perguntas[self.pergunta][7]]
                    print("Parabens %s! Você passou por todas as perguntas" %(self.jogador))
                    print("Sua pontuação foi de %i pontos" %(self.pontuacao))
                    perdeu = True

                if respost.lower() == resposta:
                    print("Você acertou, pressione enter para ir para a proxima")
                    input()
                    self.pontuacao += pontos[self.perguntas[self.pergunta][7]]
                    self.pergunta += 1
                    alternativas = [3,4,5,6]
                    self.limpar()
                else:
                    print("Lamento, você perdeu tudo")
                    print("Sua pontuação foi de %i pontos" %(self.pontuacao))
                    perdeu = True
            except KeyboardInterrupt:
                return "Error"
