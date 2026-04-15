# Version 3 - Rule-Based Level Progression Engine

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

autoavaliacao_nivel = 3
nivel = autoavaliacao_nivel
rodada = 1

# Temporary values used to simulate user performance during development
acertos = 2
total_perguntas = 4
taxa = (acertos / total_perguntas) * 100
print(f'Taxa: {taxa:.1f}%')

# Actions used by the rule engine to control level transitions and test flow
def subir_nivel(nivel, rodada):
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
    print(f'Rodada: {rodada}\n')
    rodada = 1
    if nivel > 1:
        nivel -= 1
    else:
        print('Nível mínimo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada

def mais_2(nivel, rodada):
    print('Mais 2 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada

def mais_4(nivel, rodada):
    print('Mais 4 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 2
    return nivel, rodada

def confirma_nivel(nivel, rodada):
    print('Confirma nível')
    print(f'Rodada: {rodada}\n')
    rodada = 4
    return nivel, rodada

# Rule-based system: each round defines conditions and corresponding actions
regras = {
    1: [
        (lambda t: t >= 80, subir_nivel),
        (lambda t: t > 50, mais_2),
        (lambda t: t > 35, mais_4),
        (lambda t: t > 0, mais_2),
        (lambda t: True, descer_nivel)
    ],
    2: [
        (lambda t: t >= 80, subir_nivel),
        (lambda t: t > 60, mais_2),
        (lambda t: t >= 50, confirma_nivel),
        (lambda t: True, descer_nivel)
    ],
    3: [
        (lambda t: t >= 75, subir_nivel),
        (lambda t: t > 35, confirma_nivel),
        (lambda t: True, descer_nivel)
    ]
}

# Defines how many questions are evaluated in each round
limites = {1: 4, 2: 6, 3: 8}

# Main loop: iterates through rounds until the level is confirmed
while rodada < 4:
    pergunta_limite = limites[rodada]
    limite_anterior = limites.get(rodada - 1, 0)

    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')

    for questao in lista_perguntas:
        if questao['nível'] == nivel and limite_anterior < questao['número'] <= pergunta_limite:
            print(f'Nível {questao["nível"]} - {questao["pergunta"]}')
            if questao['número'] == pergunta_limite:
                print('CONFERIR SCORE')
                taxa = float(input('Qual a taxa? '))

                # Evaluate rules sequentially and execute the first matching condition
                for condicao, acao in regras[rodada]:
                    if condicao(taxa):
                        nivel, rodada = acao(nivel, rodada)
                        break
                break
    else:
        break
