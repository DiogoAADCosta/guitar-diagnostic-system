# Version 3.1 - Conditional Level Progression (Pre-Rule Engine)

# This version introduces level progression based on user performance across rounds.
# The logic is implemented using nested conditional statements,
# which leads to repetition and limited scalability.


# Simplified question structure used to support level-based progression logic,
# mapping each question by level and sequence number.
# Differs from previous versions, which were designed for tag-based diagnostic analysis.
lista_perguntas = [
    {'nível': 1, 'número': 1, 'pergunta': 'Pergunta 1'},
    {'nível': 1, 'número': 2, 'pergunta': 'Pergunta 2'},
    {'nível': 1, 'número': 3, 'pergunta': 'Pergunta 3'},
    {'nível': 1, 'número': 4, 'pergunta': 'Pergunta 4'},
    {'nível': 1, 'número': 5, 'pergunta': 'Pergunta 5'},
    {'nível': 1, 'número': 6, 'pergunta': 'Pergunta 6'},
    {'nível': 1, 'número': 7, 'pergunta': 'Pergunta 7'},
    {'nível': 1, 'número': 8, 'pergunta': 'Pergunta 8'},
    {'nível': 2, 'número': 1, 'pergunta': 'Pergunta 1'},
    {'nível': 2, 'número': 2, 'pergunta': 'Pergunta 2'},
    {'nível': 2, 'número': 3, 'pergunta': 'Pergunta 3'},
    {'nível': 2, 'número': 4, 'pergunta': 'Pergunta 4'},
    {'nível': 2, 'número': 5, 'pergunta': 'Pergunta 5'},
    {'nível': 2, 'número': 6, 'pergunta': 'Pergunta 6'},
    {'nível': 2, 'número': 7, 'pergunta': 'Pergunta 7'},
    {'nível': 2, 'número': 8, 'pergunta': 'Pergunta 8'},
    {'nível': 3, 'número': 1, 'pergunta': 'Pergunta 1'},
    {'nível': 3, 'número': 2, 'pergunta': 'Pergunta 2'},
    {'nível': 3, 'número': 3, 'pergunta': 'Pergunta 3'},
    {'nível': 3, 'número': 4, 'pergunta': 'Pergunta 4'},
    {'nível': 3, 'número': 5, 'pergunta': 'Pergunta 5'},
    {'nível': 3, 'número': 6, 'pergunta': 'Pergunta 6'},
    {'nível': 3, 'número': 7, 'pergunta': 'Pergunta 7'},
    {'nível': 3, 'número': 8, 'pergunta': 'Pergunta 8'},
    {'nível': 4, 'número': 1, 'pergunta': 'Pergunta 1'},
    {'nível': 4, 'número': 2, 'pergunta': 'Pergunta 2'},
    {'nível': 4, 'número': 3, 'pergunta': 'Pergunta 3'},
    {'nível': 4, 'número': 4, 'pergunta': 'Pergunta 4'},
    {'nível': 4, 'número': 5, 'pergunta': 'Pergunta 5'},
    {'nível': 4, 'número': 6, 'pergunta': 'Pergunta 6'},
    {'nível': 4, 'número': 7, 'pergunta': 'Pergunta 7'},
    {'nível': 4, 'número': 8, 'pergunta': 'Pergunta 8'},
    {'nível': 5, 'número': 1, 'pergunta': 'Pergunta 1'},
    {'nível': 5, 'número': 2, 'pergunta': 'Pergunta 2'},
    {'nível': 5, 'número': 3, 'pergunta': 'Pergunta 3'},
    {'nível': 5, 'número': 4, 'pergunta': 'Pergunta 4'},
    {'nível': 5, 'número': 5, 'pergunta': 'Pergunta 5'},
    {'nível': 5, 'número': 6, 'pergunta': 'Pergunta 6'},
    {'nível': 5, 'número': 7, 'pergunta': 'Pergunta 7'},
    {'nível': 5, 'número': 8, 'pergunta': 'Pergunta 8'}
]

autoavaliacao_nivel = 2
nivel = autoavaliacao_nivel
rodada = 1

# Temporary values used to simulate user performance during development
acertos = 2
total_perguntas = 4
taxa = (acertos / total_perguntas) * 100
print(f'Taxa: {taxa:.1f}%')

# The system evaluates user performance in rounds, progressively increasing question count
# Main loop controlling level progression
while rodada < 4:
    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')
    for questao in lista_perguntas:
        # Question limits are defined conditionally inside the loop (pre-refactor approach)
        if rodada == 1:
            pergunta_limite = 4
        elif rodada == 2:
            pergunta_limite = 6
        elif rodada == 3:
            pergunta_limite =  8
        if questao['nível'] == nivel:
            print(f'Nível {questao["nível"]} - {questao["pergunta"]}')
            # Break statements interrupt the current flow to trigger level transitions or re-evaluation
            if questao['número'] == pergunta_limite:
                print('CONFERIR SCORE')
                taxa = int(input('Qual a taxa? '))
                # Rule logic is implemented through nested conditionals (pre-rule-engine structure)
                if rodada == 1:                               
                    if taxa >= 80:  
                        print('Sobe de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel < 5:
                            nivel += 1
                        else:
                            print('Nível máximo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
                    elif taxa > 50:  
                        print('Mais 2 perguntas')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada += 1
                    elif taxa > 35:  
                        print('Mais 4 perguntas')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada += 2
                    elif taxa > 0:    
                        print('Mais 2 perguntas')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada += 1
                    else:
                        print('Desce de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel > 1:
                            nivel -= 1
                        else:
                            print('Nível mínimo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
                elif rodada == 2:                            
                    if taxa >= 80: 
                        print('Sobe de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel < 5:
                            nivel += 1
                        else:
                            print('Nível máximo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
                    elif taxa > 60:  
                        print('Mais 2 perguntas')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada += 1
                    elif taxa >= 50:   
                        print('Confirma nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 4
                        break
                    else:
                        print('Desce de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel > 1:
                            nivel -= 1
                        else:
                            print('Nível mínimo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
                elif rodada == 3:                             
                    if taxa >= 75:  
                        print('Sobe de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel < 5:
                            nivel += 1
                        else:
                            print('Nível máximo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
                    elif 35 < taxa < 75:   
                        print('Confirma nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 4
                        break
                    else:
                        print('Desce de nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 1
                        if nivel > 1:
                            nivel -= 1
                        else:
                            print('Nível mínimo atingido')
                            print('Confirma nível')
                            rodada = 4
                        break
    else:
        # Exit loop if no matching question flow continues
        break
