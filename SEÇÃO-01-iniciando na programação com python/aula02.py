#===================== RESUMÃO: (do que iremos aprender) ==============

# -> uma introdução a f-strings(formatação de strings);
# -> Formatação de string com o método "format";
# -> usando a função "input" para coletar dados do usuário;


# -> introdução aos blocos (condicionais): if / elif / else 
# -> if/elif/else => entendendo o fluxo do interpretador em condicionais;
# -> o Debugger do VSCODE e o interpretador do Python lendo os códigos;

# -> Operadores Relacionais(de comparação) em Python;
# -> Operadores Lógicos(and, or, not);
# -> Operadores "in" e "not in"; 

# -> Interpolação de strings com % em Python;
# -> Formatação de strings com f-strings;

# -> Fatiamento de Strings e a função "len";

# -> Introdução ao "try" e "except" para capturar erros (exeptions);

#===========================================================================


# INÍCIO: 





# =========== uma introdução a f-strings(formatação de strings): ============================
nome = "gabriel souza"
frase = f"essa e uma frase para o(a) {nome}!"
altura = 3.00000
print(f"ola {nome}, sua altura é de {altura:.2f}")
print(frase)






# =========== Formatação de string com o método "format": ============================
pont = 12.6454545
idade = 23

string = "sua idade é: {}"
formato = string.format(idade)
print(formato)

print("seu nome é {}, e sua isade é {} e pontuou: {:.2f}".format(nome, idade, pont))

# podemos alterar a ordem usando os indiçes: nome:(indice 0); idade:1, pont:2
print("seu nome é {1}, e sua idade é {0} e pontuou: {2:.2f}".format(nome, idade, pont))

# podemos tambem renomear e alterar a ordem
print("seu nome é {c}, e sua idade é {b} e pontuou: {a:.2f}".format(c=nome, b=idade, a=pont))












# =========== usando a função "input" para coletar dados do usuário: ============================
# -> POR PADRAO O INPUT RETORNA UM VALOR DE STRING;
print("qual o seu nome? ")
n = input()
print(n)

# ou

valor = input("Digite um valor?")
valor2 = input("segundo valor?")

print(valor)
print(f"valor e {valor}, e seu tipo é {type(valor)}")

# realizando casting e atribuição multipla ao mesmo tempo;
num1, num2 = int(valor), int(valor2)
print(f"a soma dos valores é: {num1 + num2}")










#=========== introdução aos blocos (condicionais): if / elif / else: ===============
v = 4

if v == 4:
    print("é 4") 
elif v > 4:
    print("e maior que 4")
else:
    print("e diferente de 4")
#=========== if/elif/else => entendendo o fluxo do interpretador em condicionais: ===============
# nada muito diferente, tudo normal;
#o Debugger do VSCODE e o interpretador do Python lendo os códigos;








#============  Operadores Relacionais(de comparação) em Python ================================
# OP      Significado         Exemplo (True)
# >       maior               2 > 1
# >=      maior ou igual      2 >= 2
# <       menor               1 < 2
# <=      menor ou igual      2 <= 2
# ==      igual               'a' == 'a'
# !=      diferente           'a' != 'b'





#=========== Operadores Lógicos(and, or, not) ========================
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True







# ============= Operadores "in" e "not in" ==============
# Strings são iteráveis (item por item)
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')


if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    
    
if encontrar not in nome:
    print(f'{encontrar} não está em {nome}')
else:
    print(f'{encontrar} está em {nome}')
    
    
    
    



#============= Interpolação de strings com % em Python ===============
"""
#Interpolação básica de strings
#s - string
#d e i - int
#f - float
#x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
# e melhor usar f-strings mesmo








#=================== Formatação de strings com f-strings ===================
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preencha 10 caracteres na esquerda;
print(f'{variavel: <10}.') # preencha 10 caracteres na direita;
print(f'{variavel: ^10}.') # fixa no centro com 10 caracteres de cada lado;
print(f'{1000.4873648123746:0=+10,.1f}') # e tipo um :.2f, separação por vigula
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
# tem outras formas mais faceis e melhores de se formatar dados no python, com bibliotecas etc...









#============= Fatiamento de Strings e a função "len" ======================
# Fatiamento de strings
# 012345678
# Olá mundo
# -987654321
# Fatiamento [i:f:p] [::] (inicio, fim, passo)
# Obs.: a função len retorna a qtd 
# de caracteres da str

variavel = 'Olá mundo'
print(variavel[::-1]) # passos invertido, vai inverter o "ola mundo" para "odnum alo"

print(len(variavel)) # tamanho da string















#=============== Introdução ao "try" e "except" para capturar erros (exeptions) ================
"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')


