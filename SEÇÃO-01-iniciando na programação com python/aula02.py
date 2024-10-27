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
print(valor)
print(f"valor e {valor}, e seu tipo é {type(valor)}")