"""
 Faça uma lista de comprar com listas 
 O usuario deve ter a possibilidade de: 
 inserir, apagar e listar valores de sua lista
 Nao permita que o programa quebre com 
 erros de indices na lista
"""

import os

lista = []

while True:
    print('Selecione uma Opção')
    opcao = input('[I]nserir [A]pagar [L]istar [S]air: ')

    try:
      op = opcao.lower()
    except:
      print("erro de conversão")
      
    if op == 'i':
        os.system('cls') # "clear" para Linux
        valor = input('Valor: ')
        lista.append(valor)
        
    elif op == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    
    
    elif op == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
            
    elif op == 's':
        break
    
    else:
        print('Por favor, escolha i, a ou l.')