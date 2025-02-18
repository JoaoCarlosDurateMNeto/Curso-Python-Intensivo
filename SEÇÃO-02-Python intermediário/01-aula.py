#========================= RESUMAO (do que iremos aprender) ===========================

# -> "def" define uma função personalizada - Introdução às funções em Python

# -> Argumentos nomeados e argumentos posicionais (não nomeados) em funções
# -> Valores padrão para parâmetros em funções Python + NoneType e None

# -> (Parte 1 e 2) Escopo de funções e módulos em Python + global

# -> Retorno de valores das funções (return)

# -> (Parte 1 e 2) *args para quantidade de argumentos não nomeados variáveis

# -> Higher Order Functions - Funções de primeira classe

# -> Closure e funções que retornam outras funções
#======================================================================================






# INICIO


#==============  "def" define uma função personalizada - Introdução às funções em Python =============
"""
Introdução as funções (def) em python 
Funções são trechos de codigo usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor especifico.
Por padrão, Funções python retornam None (nada)
"""

# nomes de função em minusculo:
# def imprimir():
 #   print("vários 1")
 #   print("vários 2")
 #   print("vários 3")
 #   print("vários 4")
 #   print("vários 5")
 #
 # imprimir()

#def imprimir(a, b, c):
#    print(a, b, c)
#    
#imprimir('oi', 1, 23) # chamando a função (procedural com parametros, sem retorno)

def imprimir(nome='sem nome'):
    print(f"Olá, {nome}!")
    
imprimir() # chamando a função (procedural com parametros, e com param padrao caso nao haja valor, sem retorno), se nao passar nenhum parametro para a função, gerará um erro
imprimir("joao")
imprimir("Ana")


















#=========== Argumentos nomeados e argumentos posicionais (não nomeados) em funções ===============
"""
Argumentos nomeados e não nomeados em funções Python:
  -> Argumento nomeado tem nome com sinal de igual;
  -> Argumento não nomeado recebe apenas o argumento (valor);
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)

# soma(y=2, x=1, z=5)  # Caso a ordem dos valores enviados faça a diferença, que na maioria dos casos fará! (usamos aegumento nomeado)

soma(1, y=2, z=5) # podemos fazer dessa forma mas nao e recomendavel, todos os argumentos que vierem depois de um argumento nomeado, devem ser o mesmo

print(1, 2, 3, sep='-')



























#======= Valores padrão para parâmetros em funções Python + NoneType e None =====================
 
"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x+y+z)
    else:
        print(f"{x=} {y=}", x+y)
        
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)


    


























#============== (Parte 1 e 2) Escopo de funções e módulos em Python + global =========================
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra 'global' faz uma variavel do escopo externo ser a mesma no escopo interno.
"""


x = 1


def escopo():
    global x   # apenas para aprendizado, pois isso e má prática; 
    x = 10     # alterar variaveis de escopo global tbm e má pratica;
    
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
        
    outra_funcao()
    print(x)


print(x)
escopo()
print(x)




























#=================== Retorno de valores das funções (return) =============================

"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))




























#=========== (Parte 1 e 2) *args para quantidade de argumentos não nomeados variáveis ==========

"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento), args(sao tuplas mas podemos alteralos para listas)
"""
# e apartir da estrelinha que havera o empacotamento - (colocara os parametros nao nomeados em uma tupla);
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10 # Basicamente uma tupla, pois argumentos nao nomeados funcionam com tuplas
outra_soma = soma(*numeros) # aqui nesse caso ha um desempacotamento pois ja tem uma tupla; entao para nao ficar uma tupla dentro de outra, será realizado o desempacotamento atraves de '*';
print(outra_soma)

print(sum(numeros)) # a função soma ja realiza a soma, mas tem que passar uma tupla para ela
# print(*numeros)























# ============== Higher Order Functions - Funções de primeira classe ===================
"""
Higher Order Functions
Funções de primeira classe
"""
"""
 Academicamente, os termos 
 Higher Order Functions e First-Class Functions 
 têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu 
código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser 
diferentes e ainda refletir o mesmo significado.
"""

# very very bisonho!!!!
def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))




































# ================= Closure e funções que retornam outras funções ==========================

"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))




