"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.

01 - Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.


02 - Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.

   2.1 - Se a letra digitada estiver na
    palavra secreta; exiba a letra;

    2.2- Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = "Baile da Tuca"
letras_acertadas = ""
tent = 1*len(palavra_secreta) # para ficar justo as tentativas sempre serao p triplo das qtd carac em palavras secretas
palavraTot=''

while True:
    letra_digitada = input(f"\nDigite uma Letra: ( Tentativas restantes: {tent} ) ")
    tent -= 1
    
    
    # caso as tentativas se terminem o usuario perde
    if tent == 0:
        print(f"\nVocê perdeu o jogo, a palavra secreta era '{palavra_secreta}'.")
        break
    
    
    # Teste de Verificação: 
    if len(letra_digitada) > 1:
        print("\n Digite apenas uma letra")
        continue
    
    
    # ira apenas concatenar os caracteres acertados pelo usuario e armazenalos na string
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
        
    # comparando letras acertadas percorendo toda a "palavra_secreta" usando uma variavel chamada "letra_secreta"
    for letra_secreta in palavra_secreta:
            
        if letra_secreta in letras_acertadas:
            palavraTot += letra_secreta
            print(letra_secreta, end=" ")
        else:
            palavraTot += '*'
            print("*", end=" ")
    
    
    # verificação para que quando as palavra estiver completa o jogo acabe e o usuario ganhe    
    if palavraTot != palavra_secreta:
        palavraTot = ''
        continue
    else:
        print(f"\nParabens!, você ganhou o jogo, a palavra secreta era '{palavra_secreta}'.")
        break
    
   

    
    