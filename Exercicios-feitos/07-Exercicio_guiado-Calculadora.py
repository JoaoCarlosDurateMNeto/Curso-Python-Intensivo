

# ================ CALCULADORA COM WHILE =======================


while True:
    num_01 = input("Digite 1° numero: ")
    num_02 = input("Digite 2° numero: ")
    operador = input("Escolha um Operador: (+, x, -, /) ")
    numeros_validos = None
    
    
    
    try:
        num_01 = float(num_01)
        num_02 = float(num_02)
        numeros_validos = True
    except: 
        numeros_validos = None
        
    
    
        
    # se o operador escolhido nao esta entre os operadores validos   
    operador_permitidos = '+x/+-'
    if (operador not in operador_permitidos) or (len(operador) > 1):
        print("operador invalido")
        continue    
    
    # se um dos numeros nao for convertivel para float
    if numeros_validos is None: 
        print("Numeros invalido")
        continue
    
    
    # onde irá ocorrer operações:
    if operador == "+":
        print(f"{num_01} + {num_02} = {num_01 + num_02}")
    elif operador == "-":
        print(f"{num_01} - {num_02} = {num_01 - num_02}")
    elif operador == "x":
        print(f"{num_01} x {num_02} = {num_01 * num_02}")       
    elif operador == "/":
        print(f"{num_01} / {num_02} = {num_01 / num_02:.2f}")
    
    
    #########################################################################
    
    
    sair = input("quer sair? ( [s]im / [n]ão )").lower().startswith("s") # convertendo para minusculo e se a palavra começar com "s";
    
    if sair is True:
         break
        