import random

valores = []
for i in range(1, 6):
    n_aleatorio = random.randint(1, 20)
    valores.append(n_aleatorio)


tentativa = 1

while True:
    choices = []
    for i in range(5):
        while True: 
                choice = int(input(f"Escolha um número de 1 a 20 para a posição {i + 1}: "))
                if choice < 1 or choice > 20:
                    print('Escolha invalida. Digite um valor de 1 a 20')    
                    pass 
                else: 
                    choices.append(choice)
                    break 


    acertos = []
    for indice, choice in enumerate(choices, start=1):
        if choice == valores[indice - 1]:
            acertos.append(f"Você ACERTOU o valor do numero de posição {indice}. Sua Resposta: {choice}")
            
        elif choice < valores[indice - 1]:
            acertos.append(f"Você digitou um valor MENOR que o esperado no numero de posição {indice}. Sua Resposta: {choice}")
            
        else:
            acertos.append(f'Você digitou um valor MAIOR que o esperado no numero de posição {indice}. Sua Resposta: {choice}')
            


    print('\nResultado:')
    for msg in acertos:
        print(msg)

    if choices == valores:
        print('\nParabens! Voce acertou na tentativa de numero {}'.format(tentativa))
        break
    else:
        
        print(f'Tente novamente. Tentativa de numero: {tentativa}')
        tentativa += 1
        continue
                
            




