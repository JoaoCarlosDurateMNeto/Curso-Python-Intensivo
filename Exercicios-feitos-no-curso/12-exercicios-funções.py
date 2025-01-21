# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


# ================ Solução do Professor: =========================







# ================= minha solução foia mesma do professor: ================================
def duplica(numero):
    return 2*numero  

def triplica(numero):
    return  3*numero

def quadruplica(numero):
    return 4*numero

r1 = duplica(6)
r2 = triplica(6)
r3 = quadruplica(6)

print(r1)
print(r2)
print(r3)



# ================= solução mais complexa, professor: ================================

# cirando uma função que pode fazer tudo das demais acima (aula de clouser):
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador 
    return multiplicar

#multi1 = criar_multiplicador(2) # Multiplicador será o "multiplicador"
#print(multi1(2)) # E o numero será o "numero"

numero = 3

for i in [2, 3, 4]:
    multi1 = criar_multiplicador(i)
    print(multi1(numero))
    
