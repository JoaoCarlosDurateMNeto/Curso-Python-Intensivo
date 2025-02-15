#========================= RESUMAO (do que iremos aprender) ===========================

# -> Introdução ao tipo de dados dict - Dicionários em Python
# -> Manipulando chaves e valores em dicionários em Python
# -> (Parte 1) Métodos úteis nos dicionários Python (dict)
# -> Shallow Copy vs Deep Copy em dados mutáveis Python
# -> (Parte 2) Métodos úteis nos dicionários Python (dict)

# -> Introdução ao tipo set em Python (conjuntos)
# -> Peculiaridades do tipo mutável set em Python
# -> Métodos úteis do tipo set em Python
# -> Operadores importantes para o tipo set (conjuntos)
# -> Exemplo de uso do tipo set
#======================================================================================




# INICIO



#=============== Introdução ao tipo de dados dict - Dicionários em Python =====================
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
    
    
    
    
    
    
    
    
    

































# ============== Manipulando chaves e valores em dicionários em Python ========================
# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome')) # tenta obter um valor de chave
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')







































#================== (Parte 1) Métodos úteis nos dicionários Python (dict) ======================

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0) # adicionando um valor padrao, caso nao haja a chave; (e tbm adiciona uma chave caso tbm nao exista)
print(pessoa['idade'])
# print(len(pessoa))

# REALIZANDO UM CAST PARA TRANSFORMAR OS ITENS ANBAIXO UMA LISTA DE ALGO QUE QUEREMOS:
# print(list(pessoa.keys())) 
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

































#================ Shallow Copy vs Deep Copy em dados mutáveis Python ==================
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


#import copy  (para poder usar o deepcopy(item))

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2], # nao sera copiado, sera apenas uma copia rasa, ou seja d2 vai apontar para a mesma lista que a do d1, para evitar isso podemos fazer uma deepcopy();
}
d2 = d1.copy()
# d2 = copy.deepcopy(d1) (nao recomendavel para sistemas muito grandes, muito processamento)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)


























#=============== (Parte 2) Métodos úteis nos dicionários Python (dict) ==============

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'(valor padrão) ))

# nome = p1.pop('nome')  #-> apagando o item e ao mesmo tempo o armazenando; 
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # -> remove a ultima chave do dicionário e armazenandoa;
# print(ultima_chave)
# print(p1)

# assunto complexo e ao mesmo tempo divertido: update(atualização)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30) # -> bom de fazer, quando vamos usar de forma dinamica
# tupla = (('nome', 'novo valor'), ('idade', 30)) # -> outra maneira de fazer um update
lista = [['nome', 'novo valor'], ['idade', 30]] # -> igual a de cima porém com lista, e valores mutaveis

# p1.update(tupla)
p1.update(lista)

print(p1)




































# ================ Introdução ao tipo set em Python (conjuntos) ====================

# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} # parcem dicionario mas so tem valores 
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos







































#====================== Peculiaridades do tipo mutável set em Python ===============
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1] # podemos usar 'set' para remover valores iguais 
# s1 = set(l1)
# l2 = list(s1) # e convertelo para uma lista e manipulala
# s1 = {1, 2, 3}
# print(3 not in s1) => false
# print(2 in s1) => True
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos















































#=================== Métodos úteis do tipo set em Python =============================
# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)


























#===============  Operadores importantes para o tipo set (conjuntos) =====================
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)




















#======================= Exemplo de uso do tipo set ======================================
# Exemplo de uso dos sets
# pode digitanr varias vezes a mesma letra mas sempre manterá uma
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)