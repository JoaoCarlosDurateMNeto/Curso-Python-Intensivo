# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


# ====================== Solução do Professor: =========================
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')






# ====================== Minha Solução: =========================
acertos = 0
for questao in perguntas:
     escolha = ''
     
     print(f"Pergunta: {questao['Pergunta']}")
     print("Opções: ")
     
     for k, i in enumerate(questao['Opções']):
         print(f"{k}) {i}")
     
     escolha = int(input("Qual é a resposta correta: "))
     
     if questao['Opções'][escolha] == questao['Resposta']:
         acertos += 1
         print(f"{questao['Resposta']}, Parabens! voce acertou")
     else:
        print(f"{questao['Resposta']}, Errou!")
    
print(f"voce acertou {acertos} de 3 Questões")