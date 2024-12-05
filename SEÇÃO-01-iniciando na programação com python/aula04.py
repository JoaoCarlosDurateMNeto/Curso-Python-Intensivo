#===================== RESUMÃO: (do que iremos aprender) ==============

# -> Tipo list - Introdução às listas mutáveis em Python
# -> Alterando uma lista com índices, del, append e pop (Tipo list)
# -> Inserindo itens em qualquer índice da lista com insert (Tipo list)
# -> Concatenando e estendendo listas em Python
# -> Cuidados com tipos de dados mutáveis - list e copy
# -> for in com tipo list

# -> Introdução ao empacotamento e desempacotamento (ou multipla-atribuição)

# -> Tipo tuple (tuplas)

# -> enumerate para enumerar valores de iteráveis (pegar índices)

# -> Imprecisão dos números de ponto flutuante + round e decimal.Decimal

# -> split, join e strip são métodos muito úteis da str

# -> Listas dentro de listas (iteráveis dentro de iteráveis)

# -> Desempacotamento em chamadas de funções

# -> Operação ternária com Python (if e else de uma linha)

#======================================================================





# INICIO










#========================== Tipo list - Introdução às listas mutáveis em Python =======================
"""
Listas em Python
Tipo list - Mutável (coisa que nao podemos fazer na lista de strings);
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len) (lista de caracteres imutavel)
# print(bool([]))  # false
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []] # ao contrario da linguagem C podemos usar varios tipos em um unico array/list;
lista[-3] = 'Maria' # alterando o valor de "luiz otavio" para "maria"
print(lista)
print(lista[2], type(lista[2]))

lista_de_frutas = ["Maçã", "Banana", "Côco"]
print(lista_de_frutas[0])
























#================ Alterando uma lista com índices, del, append e pop (Tipo list) =====================

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # deletando um indice em especifico (evitar pois exige mt processamento ao excluir itens iniciais de listas muito grandes)
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop() # exclui o ultimo valor da lista
lista.append(60) # adiciona um valor ao final da lista
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)




















#=================== Inserindo itens em qualquer índice da lista com insert (Tipo list) ============

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido (list.insert(indice/posição, valor_a_ser_inserido))
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    remove - remove um valor escolhido
    + - concatena listas
    sort - organiza permanentemente uma lista em ordem alfabetica - podemos tbm sort(reverse=true)
    reverse - exibe uma lista de traz para frente, de sua original
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.remove(lista[0]) # => ou 10, ou (var = 10, lista.remove(var)) => temos essas formas de remover um item
lista.append(1233)
del lista[-1]
# lista.clear() -> vai lmpar toda a lista
lista.insert(100, 5) # vai dar erro, vai adicionar o 5, mas erro de indice "100", pois so vai ate o indice 3 adicionando o valor 5;
print(lista[3]) # => 5
print(lista)
























#======================== Concatenando e estendendo listas em Python =============================

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # contatenando duas listas (realiza uma extensao de uma lista_a com outra lista_b)
lista_a.extend(lista_b)   # estendendo a lista_a com a lista_b
print(lista_c)
print(lista_a)





















#=================== Cuidados com tipos de dados mutáveis - list e copy ==================
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # lista_b sera uma copia da lista_a, sem essa função "copy()" as duas listas irao apontar para o mesmo espaço na memoria, oq pode dar muita dor de cabeça no futuro;

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)



























#=================================== for in com tipo list ===============================
"""
for in com listas

Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista)) # criando um range do tamanho da lista;

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))


""" 
minha resp:

i=0
for nome in lista:
    print(i, nome, type(nome))
    i+=1
"""



























#============================ Introdução ao empacotamento e desempacotamento (ou atribuição multipla) ======================

"""
Introdução ao empacotamento e desempacotamento

__ -> signofoca que temos esse valor mas nao iremos usálo, isso e para o outros devs; 
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz', 'marcelo', 'Martins']
print(resto)
print(nome)

for nome in resto:
    print(nome)
    
    
























#==================== Tipo tuple (tuplas) ====================
"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes) # convertendo uma lista para uma tupla
# nomes = list(nomes) # convertendo uma tupla para uma lista
print(nomes[-1])
print(nomes)



























#=============== enumerate para enumerar valores de iteráveis (pegar índices) ===============
"""
enumerate - enumera iteráveis (índices)
"""
# [ (0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João') ]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = list(enumerate(lista, start=10)) -> (podemos fazer cast de tuple para list e o contrario tbm), o enumerat é responsavel por enumerar os indices(e podemos ditar seu inicio), ja que nao conseguimos pegalos no python para imprimilos; mas usalos sim

#lista_enumerada = enumerate(lista) -> evitar para nao dar problemas, use direto para sempre cirar um novo iterator e nao esgotar os valores;


for indice, nome in enumerate(lista): # fazendo desempacotamento(ou multipla-atribuição) direto no for
    print(indice, nome, lista[indice])
    
# for item in enumerate(lista):
#     indice, nome = item    -> # ex: indice, nome = [ (0, 'Maria'), ..... ] # fazendo desempacotamento(ou multipla-atribuição)
#     print(indice, nome)     # ex: 0 Maria


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')     -> saida:  FOR da tupla: 
#                                                  0
#                                                  Maria



























#================ Imprecisão dos números de ponto flutuante + round e decimal.Decimal ================
"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1') # modulo do python decimal, para trabalahar, quando necessário, de forma mais precisa, passar uma "string" no lugar de um "float" ou "int";
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2)) # round(valor, n°de_casas_decimais)



























#==================== split, join e strip são métodos muito úteis da str ======================

"""
split e join com list e str
split - divide uma string (list)
join - une uma string

strip - corta espaços do começo e do fim; (lstrip - esquerda), (rstrip - direita) 
"""

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # mais para frente aprenderemos "expressao regular" e faremos cortes mais refinados;

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)































#================= Listas dentro de listas (iteráveis dentro de iteráveis) ================
"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    
    # 0
    ['Elaine', ],  # 1
    
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
        




























#========================= Desempacotamento em chamadas de funções ============================
# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista) # => 'Maria', 'Helena', 1, 2, 3, 'Eduarda'
# print(*string)
# print(*tupla)

print(*salas, sep='\n') # sep - separador de lista/strings,tuplas...iteraveis     
#saida: 
    # ['Maria', 'Helena', ]  
    # ['Elaine', ]
    # ['Luiz', 'João', 'Eduarda', ]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




#==================== Operação ternária com Python (if e else de uma linha) ======================
"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')