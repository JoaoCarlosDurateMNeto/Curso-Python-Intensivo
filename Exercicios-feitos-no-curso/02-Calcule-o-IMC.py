nome = "Pedro Enrique"
altura = 1.80
peso = 95

# fazendo cast para float, para evitar supostos problemas:
peso = float(peso)
altura = float(altura)

imc = ( peso /  (altura * altura) )  # o imc de uma pessoa é o seu: peso/altura²

print(f" O IMC do {nome} foi de: {imc}")
