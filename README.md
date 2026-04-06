# Linguagem-Peixe

# 🍣 SushiLang - Linguagem de Programação Temática

## 🎯 Descrição

A **SushiLang** é uma mini-linguagem de programação com temática baseada em sushi e peixes.  
Ela permite declaração de variáveis, operações matemáticas, estruturas condicionais, repetição e entrada/saída de dados.

---

## 🧩 Tokens

### 🔹 Palavras-chave

| Palavra   | Token     | Descrição                  |
|----------|----------|---------------------------|
| sushiman | CRIAR    | Declara variável          |
| nori     | SE       | Condicional               |
| wasabi   | SENAO    | Else                      |
| temaki   | ENQUANTO | Loop                      |
| itamae   | DEFINIR  | Definição de função       |
| gohan    | RETORNAR | Retorno                   |
| omakase  | EXIBIR   | Saída                     |
| cardapio | LER      | Entrada                   |
| hashi    | INICIO   | Início de bloco           |
| bento    | FIM      | Fim de bloco              |

---

### 🔹 Tipos

| Palavra | Valor |
|--------|------|
| cru    | true |
| cozido | false |

---

### 🔹 Operadores Aritméticos

| Palavra       | Operação |
|--------------|--------|
| salmao       | +      |
| atum         | -      |
| tilapia      | *      |
| bacalhau     | /      |
| sardinha     | %      |
| peixe_espada | ^      |

---

### 🔹 Operadores Relacionais

| Palavra        |
|---------------|
| igual         |
| diferente     |
| menor         |
| menor_igual   |
| maior         |
| maior_igual   |

---

### 🔹 Operadores Lógicos

| Palavra |
|--------|
| e      |
| ou     |
| nao    |

---

## 📐 Gramática (EBNF)

```ebnf
programa ::= { comando }

comando ::= declaracao
          | atribuicao
          | condicional
          | repeticao
          | exibicao
          | entrada

declaracao ::= "sushiman" IDENTIFICADOR "=" expressao ";"

atribuicao ::= IDENTIFICADOR "=" expressao ";"

condicional ::= "nori" "(" expressao ")" "hashi" { comando } "bento"
               [ "wasabi" "hashi" { comando } "bento" ]

repeticao ::= "temaki" "(" expressao ")" "hashi" { comando } "bento"

exibicao ::= "omakase" "(" expressao ")" ";"

entrada ::= "cardapio" "(" STRING ")" ";"

expressao ::= termo { ("salmao" | "atum") termo }

termo ::= fator { ("tilapia" | "bacalhau" | "sardinha") fator }

fator ::= NUMERO
        | STRING
        | IDENTIFICADOR
        | "(" expressao ")"

```

## 🚀 Como Usar

### Executar um programa

# Na raiz do projeto
python main.py

## Exemplo de Programa
```
sushiman distancia = 100;
sushiman tempo = 5;

sushiman velocidade = distancia bacalhau tempo;

omakase("O atum percorreu " salmao distancia salmao " metros em " salmao tempo salmao " segundos.");
omakase("Velocidade: " salmao velocidade);
```
Saída Esperada
```
O atum percorreu 100 metros em 5 segundos.
Velocidade: 20
```
## Exemplo de AST

Para o código:
```
sushiman distancia = 100;
sushiman tempo = 5;
sushiman velocidade = distancia bacalhau tempo;
```

A AST gerada fica:
```
Programa
├── Declaracao: distancia
│   └── Numero: 100
├── Declaracao: tempo
│   └── Numero: 5
└── Declaracao: velocidade
    └── BinOp: bacalhau
        ├── Variavel: distancia
        └── Variavel: tempo
```

## Precedência

Ordem de prioridade:

1 -Parênteses ()
2 -nao
3 - peixe_espada
4 - tilapia, bacalhau, sardinha
5 - salmao, atum
6 - Relacionais (maior, menor, etc.)
7 - Lógicos (e, ou)

## Estrutura de blocos

Os blocos são delimitados por:
```
hashi   → início
bento   → fim
```
