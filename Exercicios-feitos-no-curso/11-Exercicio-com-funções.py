"""
  Exercicios com funções:
  
  - Crie uma função que multiplique todos os (argumentos/parametros) nao nomeados recebidos,
  - Retorne o total para uma variavel e mostre o valor da variavel;
  
  
  - Crie uma Função fala se um numero é Par ou Impar,
  - Retorne se um número é Par ou Impar;
"""




# ==================== MINHA SOLUÇÃO: ====================

def func_Mult(*args):
    total = 1
    for valor in args:
        total = total * valor # (total = total * valor)
    return total
valoresTot = func_Mult(1, 2, 3, 4, 5)
print(valoresTot)


def func_ParImpar(*args):
    vetorPar = []
    vetorImpar = []
    
    for valor in args:
        if valor%2 == 0:
             vetorPar.append(valor)
        else:
             vetorImpar.append(valor)
             
    return {'Par':vetorPar, 'Impar':vetorImpar}  # Retorna um dicionario com vetores impar e par

valores_pares_e_impares = func_ParImpar(2, 3, 4, 5, 3_000_32, 23, 35, 74, 80)
print(valores_pares_e_impares)
#==========================================================================================












# SOLUÇÃO DO PROFESSOR: 

# A de multiplicação ficou quase igual so mudou os nomes

def par_impar(numero):
    return f'{numero} é PAR' if numero % 2 == 0 else f'{numero} é IMPAR' 

valor = par_impar(5)
print(valor)
valor = par_impar(2)
print(valor)