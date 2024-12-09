#========================= RESUMAO (do que iremos aprender) ===========================

# -> "def" define uma função personalizada - Introdução às funções em Python

# -> Argumentos nomeados e argumentos posicionais (não nomeados) em funções

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
