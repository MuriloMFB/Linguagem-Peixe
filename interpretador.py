from ast1 import *

class Interpretador:
    def __init__(self):
        self.variaveis = {}

    def executar(self, no):
        if isinstance(no, Programa):
            for stmt in no.statements:
                self.executar(stmt)

        elif isinstance(no, Declaracao):
            valor = self.executar(no.valor) if no.valor else None
            self.variaveis[no.nome] = valor

        elif isinstance(no, Atribuicao):
            valor = self.executar(no.valor)
            self.variaveis[no.nome] = valor

        elif isinstance(no, Numero):
            return no.valor

        elif isinstance(no, String):
            return no.valor

        elif isinstance(no, Booleano):
            return no.valor

        elif isinstance(no, Variavel):
            return self.variaveis.get(no.nome, None)

        elif isinstance(no, BinOp):
            esquerda = self.executar(no.esquerda)
            direita = self.executar(no.direita)
            op = no.operador.tipo.name

            if op == "SOMA":
                if isinstance(esquerda, str) or isinstance(direita, str):
                    return str(esquerda) + str(direita)
                return esquerda + direita
            elif op == "SUBTRACAO":
                return esquerda - direita
            elif op == "MULTIPLICACAO":
                return esquerda * direita
            elif op == "DIVISAO":
                return esquerda / direita
            elif op == "MODULO":
                return esquerda % direita
            elif op == "POTENCIA":
                return esquerda ** direita

            elif op == "IGUAL":
                return esquerda == direita
            elif op == "DIFERENTE":
                return esquerda != direita
            elif op == "MENOR":
                return esquerda < direita
            elif op == "MENOR_IGUAL":
                return esquerda <= direita
            elif op == "MAIOR":
                return esquerda > direita
            elif op == "MAIOR_IGUAL":
                return esquerda >= direita

            elif op == "E_LOGICO":
                return esquerda and direita
            elif op == "OU_LOGICO":
                return esquerda or direita

        elif isinstance(no, UnaryOp):
            valor = self.executar(no.operando)
            op = no.operador.tipo.name

            if op == "NAO_LOGICO":
                return not valor
            elif op == "SUBTRACAO":
                return -valor

        elif isinstance(no, Exibir):
            valor = self.executar(no.expressao)
            print(valor)

        elif isinstance(no, Se):
            cond = self.executar(no.condicao)
            if cond:
                for stmt in no.entao:
                    self.executar(stmt)
            elif no.senao:
                for stmt in no.senao:
                    self.executar(stmt)

        elif isinstance(no, Enquanto):
            while self.executar(no.condicao):
                for stmt in no.corpo:
                    self.executar(stmt)

        elif isinstance(no, Ler):
            entrada = input(no.mensagem.valor if no.mensagem else "")
            return entrada