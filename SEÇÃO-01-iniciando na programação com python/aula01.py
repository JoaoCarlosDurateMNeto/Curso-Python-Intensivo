#===================== RESUMÃO: (do que iremos aprender) ==============

# -> Aprendendo a usar Comentários e usar o Docstring para comentar;
# -> Sobre Função, Print();

# ================= Introdução aos Tipos De Dados: ====================
# -> Tipo str (strings);
# -> Tipo int e float (números);
# -> Tipo bool(boolean);
# -> Cast(converção de um tipo de dados para outro);
# =====================================================================

# -> Introdução a Váriaveis ;

# ====== Introdução a Operadores Aritiméticos =========================
# -> Ordem de Precedência;
# -> concatenação(+) e repetição(*) com operadores aritimeticos;
#=======================================================================



# INICIO

# Assim se escreve um comentário usando a cerquilha;

"""
   isso é uma Docstring; o python a lê, ele não a pula;
   usamos ela para outras coisas alem de anotar blocos de códigos;
"""


# Sobre a Função  Print(): serve para exibir as coisas na tela, atraves de argumentos recebidos; (temos muitas opções para trabalhar com ela)
print(12, 13, sep="-") # mudá o separador/espaco entre as palavras na hora de exibir na tela

print("Olá \n Mundo", end="\n") 
# o "end" serve para alterar algo no fim de cada linha;
# "\n" - quebra a linha;


 
 
 
 
 
 
 

"""
  *Python = linguagem de programação; 
  *Tipo de tipagem = Dinamica/Forte;
  *str -> string -> texto; (conjunto de caracteres);
  *Strings são textos que estão dentro de aspas;
"""
# aspas duplas
print("ola mundo")
# Escape
print("ola \"mundo\" ") # => ola "mundo"
# r
print(r"ola \"mundo\" ") # => ola \"mundo\"












"""
  ========= TIPOS (int e float): =================
  - int => numero inteiro, seja negativo ou positivo;
  - float => numero com ponto flutuante, seja positivo ou negativo;  
"""
print(-1, 23) # int
print(1.40, 9.0) # float


# a classe "type()" é muito util para desenvolver programas que verifiquem dados de entrada entre outros;
print(type("ola"))
print(type(2))












"""
    ================= TIPO (BOOLEANO): =============================
    - ao questionar algo em um programa;
    - só existem duas respostas possiveis;
    - valor "True" ou "False", frequentimente usados para condições; 
"""
print(10 == 10) # True
print(12 >= 23) # False
print(type(2 == 2)) # bool











"""
  ========= Converção de Tipos para outros Tipos: =================
  - type convertion, type casting, coertion;
  - é o ato de converter um tipo em outro tipo; 
"""
print(1 + 3) # vai realizar uma operação de soma; (4)
print("r" + "d") # vai concatenar, pois o tipo ede str; (rd)

# exemplos de conversão de tipos:
print(str(34)) # convertendo int "34" para uma str "34";
print(int("10")  + 23)
print(str(12) + str(23))
print(float("20") + int("2"))
print(bool(' '))

















"""
  ========= Introdução há Variavies: =================
  - PEP8: guia de estilo do código python
  - Variaveis sao algo para salvar na memoria do computador;
  - o sinal "=" é o operador de atribuição;
  - Uso: nome_da_variavel = expressão
"""
nome = "pedro alvares"
soma = 13 + 6
idade_maior =  soma >= 30

print(nome)
print(soma)
print(idade_maior)
print(f"seu nome é: {nome}  e sua idade e a soma:{soma}") # f-string -> formatação de string, veremos mais na frente;













"""
  ========= Introdução aos Operadores Aritiméticos: =================
  - soma[ + ], subtração[ - ], multiplicação[ * ], divisão[ / ], resto[ % ], expoente[ ** ];
  - concatenação(+) e repetição(*) com operadores aritimeticos;
  - Ordem de Precedência:
    1.()
    2.**
    3.*  /  //  %
    4.+  -
"""
soma = 2 + 2
subtracao = 2 - 2
multiplicacao = 2 * 2
divisao = 2 / 2
divisao_inteira = 10 // 3
resto = 2 % 2
expoente = 3**2
print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("Divisão Inteira: ", divisao_inteira)
print("Resto da Divisão: ", resto)
print("Expoente: ", expoente)


# concatenação(+) e repetição(*) com operadores aritimeticos;
# peculiariedades:
concatenacao = "Luiz" + "Bertolo" + " " + "!"
tres_vezes_luiz = 3 * "Luiz"
A_10_vezes = 10 * "A"
print(concatenacao)
print(tres_vezes_luiz)
print(A_10_vezes)

# Ordem de precedência:
conta_1 = (1+1)**(5+5) #1024
print(conta_1)