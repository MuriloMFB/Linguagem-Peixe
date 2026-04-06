from lexer import AnalisadorLexico
from parser import Parser
from interpretador import Interpretador

def nome_operador(tipo):
    mapa = {
        "SOMA": "salmao",
        "SUBTRACAO": "atum",
        "MULTIPLICACAO": "tilapia",
        "DIVISAO": "bacalhau",
        "MODULO": "sardinha",
        "POTENCIA": "peixe_espada",
        "IGUAL": "igual",
        "DIFERENTE": "diferente",
        "MENOR": "menor",
        "MENOR_IGUAL": "menor_igual",
        "MAIOR": "maior",
        "MAIOR_IGUAL": "maior_igual",
        "E_LOGICO": "e",
        "OU_LOGICO": "ou",
        "NAO_LOGICO": "nao",
    }
    return mapa.get(tipo.name, tipo.name)


def imprimir_ast(no, prefixo="", eh_ultimo=True):
    conector = "└── " if eh_ultimo else "├── "

    if no is None:
        print(prefixo + conector + "None")
        return

    nome_classe = no.__class__.__name__

    if nome_classe == "Programa":
        print(prefixo + conector + "Programa")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        total = len(no.statements)
        for i, stmt in enumerate(no.statements):
            imprimir_ast(stmt, novo_prefixo, i == total - 1)

    elif nome_classe == "Declaracao":
        print(prefixo + conector + f"Declaracao: {no.nome}")
        if no.valor is not None:
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            imprimir_ast(no.valor, novo_prefixo, True)

    elif nome_classe == "Atribuicao":
        print(prefixo + conector + f"Atribuicao: {no.nome}")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        imprimir_ast(no.valor, novo_prefixo, True)

    elif nome_classe == "Numero":
        print(prefixo + conector + f"Numero: {no.valor}")

    elif nome_classe == "String":
        print(prefixo + conector + f'String: "{no.valor}"')

    elif nome_classe == "Booleano":
        valor = "cru" if no.valor else "cozido"
        print(prefixo + conector + f"Booleano: {valor}")

    elif nome_classe == "Variavel":
        print(prefixo + conector + f"Variavel: {no.nome}")

    elif nome_classe == "BinOp":
        print(prefixo + conector + f"BinOp: {nome_operador(no.operador.tipo)}")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        imprimir_ast(no.esquerda, novo_prefixo, False)
        imprimir_ast(no.direita, novo_prefixo, True)

    elif nome_classe == "UnaryOp":
        print(prefixo + conector + f"UnaryOp: {nome_operador(no.operador.tipo)}")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        imprimir_ast(no.operando, novo_prefixo, True)

    elif nome_classe == "Exibir":
        print(prefixo + conector + "Exibir: omakase")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        imprimir_ast(no.expressao, novo_prefixo, True)

    elif nome_classe == "Se":
        print(prefixo + conector + "Condicional: nori")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")

        print(novo_prefixo + "├── Condicao")
        cond_prefixo = novo_prefixo + "│   "
        imprimir_ast(no.condicao, cond_prefixo, True)

        print(novo_prefixo + "├── Entao")
        entao_prefixo = novo_prefixo + "│   "
        total_entao = len(no.entao)
        for i, stmt in enumerate(no.entao):
            imprimir_ast(stmt, entao_prefixo, i == total_entao - 1)

        if no.senao is not None:
            print(novo_prefixo + "└── Senao: wasabi")
            senao_prefixo = novo_prefixo + "    "
            total_senao = len(no.senao)
            for i, stmt in enumerate(no.senao):
                imprimir_ast(stmt, senao_prefixo, i == total_senao - 1)

    elif nome_classe == "Enquanto":
        print(prefixo + conector + "Laco: temaki")
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")

        print(novo_prefixo + "├── Condicao")
        cond_prefixo = novo_prefixo + "│   "
        imprimir_ast(no.condicao, cond_prefixo, True)

        print(novo_prefixo + "└── Corpo")
        corpo_prefixo = novo_prefixo + "    "
        total_corpo = len(no.corpo)
        for i, stmt in enumerate(no.corpo):
            imprimir_ast(stmt, corpo_prefixo, i == total_corpo - 1)

    elif nome_classe == "Ler":
        print(prefixo + conector + "Entrada: cardapio")
        if no.mensagem is not None:
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            imprimir_ast(no.mensagem, novo_prefixo, True)

    else:
        print(prefixo + conector + nome_classe)


def main():
    codigo = """
sushiman distancia = 100;
sushiman tempo = 5;
sushiman velocidade = distancia bacalhau tempo;

omakase("O atum percorreu " salmao distancia salmao " metros em " salmao tempo salmao " segundos.");
omakase("Velocidade: " salmao velocidade);
"""

    lexer = AnalisadorLexico(codigo)
    tokens = lexer.analisar()

    parser = Parser(tokens)
    ast = parser.parse()

    print("=== AST ===")
    imprimir_ast(ast)

    if parser.erros:
        print("\n=== ERROS ===")
        for erro in parser.erros:
            print(erro)
    
    print("\n=== EXECUÇÃO ===")
    interpretador = Interpretador()
    interpretador.executar(ast)


if __name__ == "__main__":
    main()