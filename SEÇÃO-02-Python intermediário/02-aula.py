#========================= RESUMAO (do que iremos aprender) ===========================

# -> Introdução ao tipo de dados dict - Dicionários em Python
# -> Manipulando chaves e valores em dicionários em Python
# -> (Parte 1) Métodos úteis nos dicionários Python (dict)

# -> Shallow Copy vs Deep Copy em dados mutáveis Python

# -> (Parte 2) Métodos úteis nos dicionários Python (dict)



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


