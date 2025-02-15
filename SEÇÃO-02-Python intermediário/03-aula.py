#========================= RESUMAO (do que iremos aprender) ===========================

# -> Introdução à função lambda + list.sort e sorted
# -> Funções lambda complexas (para entendimento)


#======================================================================================


# INICIO:














#==================== Introdução à função lambda + list.sort e sorted ========================
# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]



""" 
def exibir(lista):
    for item in lista:
        print(item)
    print()

#sorted(lista, função_criada_para_fazer_como_queremos_ordenar, e_o_item_que_queremos_ordenar)
l1 = sorted(lista, key=lambda item: item['nome']) # lambida => def sem contar com o nome e so passando o item sem precisar ter de usar um return
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
"""




























#===================== Funções lambda complexas (para entendimento) ========================
