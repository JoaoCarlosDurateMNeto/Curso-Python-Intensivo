#========================= RESUMAO (do que iremos aprender) ===========================

# -> "def" define uma função personalizada - Introdução às funções em Python

# -> Argumentos nomeados e argumentos posicionais (não nomeados) em funções
# -> Valores padrão para parâmetros em funções Python + NoneType e None
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
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)

