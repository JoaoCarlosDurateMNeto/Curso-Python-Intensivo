#===================== RESUMÃO: (do que iremos aprender) ==============

# ->  variaveis, constantes e complexidade de codigo parte 1 e 2;
# ->  id - A identidade do valor que está na memória;
# ->  Flags, is, is not e None
# ->  Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string


#  WHILE
# ->  while e break - Estrutura de repetição (Parte 1)
# ->  while - Condição em detalhes
# ->  Operadores de atribuição com operadores aritméticos
# ->  while + continue - pulando alguma repetição
# ->  while + while (laços internos)
# ->  while / else (recurso peculiar do Python)
# ->  while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)

#   FOR
# -> Introdução ao for / in - estrutura de repetição para coisas finitas
# -> range + for para usar intervalos de números
# -> Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)
# -> O que aprendemos com while também funciona no for (continue, break, else, etc)
#===========================================================================










#   INICIO




#============== variaveis, constantes e complexidade de codigo parte 1 e 2 ===================
"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 =  local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                         local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print("velocidade do carro passou do radar um")


if carro_multado_radar_1 and \
        velocidade_carro_passou_radar_1:
        print("carrod multado em radar 1")














#============== id - A identidade do valor que está na memória ===================

v1 = 'a'
print(id(v1)) # pega o valor da memoria;











#========================= Flags, is, is not e None ===========================

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)








#====== Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string =========
"""
https://docs.python.org/pt-br/3/library/stdtypes.html  ==> Tipos embutidos
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
opa = "otavio luid"
# outra_variavel = f'{string[:3]}ABC{string[4:]}' # luiz otavio
# print(string)
# print(outra_variavel.captalize()) #maiusculos no inicio
print(string.zfill(10))
print(opa.capitalize())
print(opa.title())













#================== while e break - Estrutura de repetição (Parte 1) =================
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou')
"""





#====== while - Condição em detalhes  =============================
#====== Operadores de atribuição com operadores aritméticos =======
"""
Repetições:
  while (enquanto)
  Executa uma ação enquanto uma condição for verdadeira
  Loop infinito -> Quando um código não tem fim

Operadores de atribuição:
  = += -= *= /= //= **= %=
"""
contador = 10
contador /= 5 # contador = contador / 5
print(contador)


contador = 0
while contador <= 10:
    contador += 1
    print(contador)

print('Acabou')
















#============= while + continue - pulando alguma repetição ===============
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break
    
print('Acabou')
















#=================  while + while (laços internos) ===================

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}', end=" ")
        coluna += 1
        
        
    print(f'{linha=} {coluna=}')
    linha += 1


print('Acabou')




















#==================== while/else (recurso peculiar do Python) ==================
""" 
     while / else
     
    => Recomendavel não Usar; 
""" 
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
    
print('Fora do while.')


























#====== while - Qual letra apareceu mais vezes na frase? (Iterando strings com while) ======
frase = 'O Python é uma Linguagem de Programação' \
        'multiparadigma' \
        'Python Foi criado Por Guidon van Russon'


# Resposta do professor: ( Quantas vezes a palavra apareceu, o python e case sensitive )
# print(frase.count("Python")) # resposta simples e direta ao ponto

i=0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
espaco = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu_atual = frase.count(letra_atual)
    
    # pulando/ignorando os espaços e voltando direto para o while sem considerar o resto abaixo
    if letra_atual == " ":
        i += 1 # se o continue executar o encrementador deve estar no inicio para evitar um loop infinito
        continue
    
    # contando a letra que mais apareceu ignorando os caracteres de espaços
    if (qtd_apareceu_mais_vezes < quantas_vezes_apareceu_atual) and (letra_atual != " "):
         qtd_apareceu_mais_vezes = quantas_vezes_apareceu_atual
         letra_apareceu_mais_vezes = letra_atual 
    
    # contando somente os espaços
    #if (qtd_apareceu_mais_vezes < quantas_vezes_apareceu_atual) and (letra_atual == " "):
    #    espaco = quantas_vezes_apareceu_atual
         
    i += 1
    
print(f"A Letra {letra_apareceu_mais_vezes} apareceu => {qtd_apareceu_mais_vezes} veze(s)")
#print(f"o numero de espaços foi {espaco}")

###################### minha solução temporária: ###################
# cont=0 #Contador
# i=0    #Quantidade de letras
# letra = input("Qual letra você busca? \n")  #Letra buscada

# while cont < len(frase):
#     if frase[cont] == letra:
#         i+=1
#     cont += 1
# print(f"apareçeu {i} o numero de '{letra}' na frase.")




























#============= Introdução ao for / in - estrutura de repetição para coisas finitas =====================

# utilizamos "for" para coisas que tem uma determinada quantidade de tamanho determinada;

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

# Iteravel entrega um valor por vez
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    
print(novo_texto + '*')




















#======================== range + for para usar intervalos de números =================================
"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#=========== Como o for funciona por baixo dos panos? (next, iter, iterável e iterador) ==================
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# print(texto.__next__()) -> L
# print(texto.__next__()) -> u
# print(texto.__next__()) -> i

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#=================== O que aprendemos com while também funciona no for (continue, break, else, etc) =======================
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')