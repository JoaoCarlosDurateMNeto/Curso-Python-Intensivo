"""
API simples e GRATUITA que obtém os resultados das loterias da caixa.

Compatível com as seguintes loterias: "megasena", "quina", "lotofacil", "lotomania", "duplasena", "timemania", "diadesorte", "federal", "loteca", "supersete", "maismilionaria"

Caso queira apenas utilizar a API, ela está disponível no endereço: https://api.guidi.dev.br/loteria, para utilizar basta fazer um GET na url, passando o código da loteria e o concurso.

Exemplo para obter o último concurso da megasena: https://api.guidi.dev.br/loteria/megasena/ultimo

Exemplo para obter o concurso 2000 da megasena: https://api.guidi.dev.br/loteria/megasena/2000




============================= Apenas Avaliação =======================================================

- MEGA-SENA: Números => 01 até 50; - Podendo ecolher até 6 valores com 12% de chances de acertar, por (R$: 4,50);

- LOTOFACIL: Números => 01 até 25; - Podendo ecolher até 15 valores com 60% de chances de acertar, por (R$: 2,50);

Taxa-do-App: R$: 30,00 (PODENDO REALIZAR MAIS DE UMA APOSTA)

"""
print("Iniciando Projeto Loteria")


# Apenas um exemplo (numeros historico da mega_sena pegos pela api)
historico_de_numeros_sorteados = [ [ 48,1, 3, 3, 5, 6, 9 ], [ 50, 42, 4, 2, 34, 5 ], [50,30, 45, 8, 9, 30]]


# Total de valores que podem ser da mega sena
def totalDeSena(initial, fim):
        vetor_total_da_loteria = []
        
        # atribuindo os valores totais da sena que esta sendo apostada:
        for nuns in range(initial, fim+1):
            vetor_total_da_loteria.append(nuns)
        
        return  vetor_total_da_loteria

# Pegando valores do historico
def pegar_val_do_historico_da_sena(historico):
        NumeroDoHistorico = []
        
        # Percorrendo o vetor Principal:
        for vet in historico_de_numeros_sorteados:
            # Pegando os valores de cada uma dos vetores:
            for num in vet:
                    # Pegando os valores, numeros do historico da loteria da mega-sena
                    NumeroDoHistorico.append(num)
        
        return NumeroDoHistorico


# Objetivo pegar os valores do historico e o total da loteria apostada e comparar afim de obter  valores repetidos(pegar os 5 valores mais repetidos)



# Testando a Saída:
valores = pegar_val_do_historico_da_sena(historico_de_numeros_sorteados)
total = totalDeSena(1, 50)

print(valores)
print(total)





