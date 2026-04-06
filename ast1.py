# Classe base (opcional, mas bom ter)
class ASTNode:
    pass


class Programa(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Programa({self.statements})"


class Numero(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor})"


class String(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"String({self.valor})"


class Booleano(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Booleano({self.valor})"


class Variavel(ASTNode):
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Variavel({self.nome})"


class BinOp(ASTNode):
    def __init__(self, esquerda, operador, direita):
        self.esquerda = esquerda
        self.operador = operador
        self.direita = direita

    def __repr__(self):
        return f"BinOp({self.esquerda}, {self.operador.tipo}, {self.direita})"


class UnaryOp(ASTNode):
    def __init__(self, operador, operando):
        self.operador = operador
        self.operando = operando

    def __repr__(self):
        return f"UnaryOp({self.operador.tipo}, {self.operando})"


class Declaracao(ASTNode):
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f"Declaracao({self.nome}, {self.valor})"


class Atribuicao(ASTNode):
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f"Atribuicao({self.nome}, {self.valor})"


class Exibir(ASTNode):
    def __init__(self, expressao):
        self.expressao = expressao

    def __repr__(self):
        return f"Exibir({self.expressao})"


class Se(ASTNode):
    def __init__(self, condicao, entao, senao=None):
        self.condicao = condicao
        self.entao = entao
        self.senao = senao

    def __repr__(self):
        return f"Se({self.condicao}, {self.entao}, {self.senao})"


class Enquanto(ASTNode):
    def __init__(self, condicao, corpo):
        self.condicao = condicao
        self.corpo = corpo

    def __repr__(self):
        return f"Enquanto({self.condicao}, {self.corpo})"


class Ler(ASTNode):
    def __init__(self, mensagem=None):
        self.mensagem = mensagem

    def __repr__(self):
        return f"Ler({self.mensagem})"