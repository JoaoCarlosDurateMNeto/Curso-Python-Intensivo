#===================== RESUMÃO: (do que iremos aprender) ==============

# ->  variaveis, constantes e complexidade de codigo parte 1 e 2;
# ->  id - A identidade do valor que está na memória;
# ->  Flags, is, is not e None
# ->  Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string


# ->  while e break - Estrutura de repetição (Parte 1)
# ->  while - Condição em detalhes
# ->  Operadores de atribuição com operadores aritméticos
# ->  while + continue - pulando alguma repetição
# ->  while + while (laços internos)

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
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou')






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


