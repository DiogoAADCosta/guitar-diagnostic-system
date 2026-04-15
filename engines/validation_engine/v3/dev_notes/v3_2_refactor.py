# Version 3.2 - Partial Refactor with Action Functions

# This version introduces function-based actions to reduce code repetition.
# However, the decision logic still relies on nested conditional structures,
# limiting flexibility and scalability.


# Question structure organized by level and sequence number,
# supporting level-based progression logic
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


acertos = 2
total_perguntas = 4
taxa = (acertos / total_perguntas) * 100
print(f'Taxa: {taxa:.1f}%')

# Action functions extracted to centralize level transition behavior
def subir_nivel(nivel, rodada):
    # Functions include debug/output behavior, not purely logic (pre-separation of concerns)
    print('Sobe de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    if nivel < 5:
        nivel += 1
    else:
        print('Nível máximo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada

def descer_nivel(nivel, rodada):
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
    return nivel, rodada

# Main loop controlling level progression across rounds
while rodada < 4:
    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')
    for questao in lista_perguntas:
        if rodada == 1:
            pergunta_limite = 4
        elif rodada == 2:
            pergunta_limite = 6
        elif rodada == 3:
            pergunta_limite =  8
        if questao['nível'] == nivel:
            print(f'Nível {questao["nível"]} - {questao["pergunta"]}')
            if questao['número'] == pergunta_limite:
                taxa = int(input('Qual a taxa? '))

                # Decision logic still handled through nested conditionals (pre-rule abstraction)
                # Question limits are defined inside the loop (pre-refactor structure)
                # Logic remains duplicated across rounds despite function extraction
                if rodada == 1:                                
                    if taxa >= 80: 
                        nivel, rodada = subir_nivel(nivel, rodada)
                        print(taxa)
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
                        nivel, rodada = descer_nivel(nivel, rodada)
                        break
                elif rodada == 2:                              
                    if taxa >= 80: 
                        nivel, rodada = subir_nivel(nivel, rodada)
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
                        nivel, rodada = descer_nivel(nivel, rodada)
                        break
                elif rodada == 3:                           
                    if taxa >= 75: 
                        nivel, rodada = subir_nivel(nivel, rodada)
                        break
                    elif taxa > 35: 
                        print('Confirma nível')
                        print(taxa)
                        print(f'Rodada: {rodada}\n')
                        rodada = 4
                        break
                    else:
                        nivel, rodada = descer_nivel(nivel, rodada)
                        break
    else:
        break
