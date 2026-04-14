# Version 1 - Initial Structure
# Basic execution flow:
# - Display questions
# - Capture input
# - Store tags as limitations or strengths

lista_perguntas = [
    {'pergunta': 'Pergunta 1',
     'respostas':  [{'resposta': 'A', 'tag': ['limitador', 'base']},
                    {'resposta': 'B', 'tag': ['limitador', 'troca_de_acorde']},
                    {'resposta': 'C', 'tag': ['limitador', 'troca_de_acorde']},
                    {'resposta': 'D', 'tag': ['capacidade', 'troca_de_acorde']}
                    ]
    },
    {'pergunta': 'Pergunta 2',
         'respostas':  [{'resposta': 'A', 'tag': ['limitador', 'ritmo']},
                        {'resposta': 'B', 'tag': ['limitador', 'troca_de_acorde']},
                        {'resposta': 'C', 'tag': ['limitador', 'ritmo']},
                        {'resposta': 'D', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']]}
                        ]
    }
]

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

for questao in lista_perguntas:
    print()
    print(questao['pergunta'])

    for alternativa in questao['respostas']:
        print(alternativa['resposta'])

# Will be replaced by UI interaction in the final version (JavaScript)
# Input validation intentionally omitted at this stage
    resposta_usuario = input('\nSua Resposta: ').strip().upper()

    for alternativa in questao['respostas']:
        if resposta_usuario == alternativa['resposta']:
            # Handles inconsistent tag formats: ['type', value] vs [['type', value], ...]
            for i in range(0, len(alternativa['tag'])):
                if alternativa['tag'][i] == 'limitador':
                    lista_limitadores_respostas_usuario.append(alternativa['tag'][1])
                elif alternativa['tag'][i][0] == 'limitador':
                    lista_limitadores_respostas_usuario.append(alternativa['tag'][i][1])

                if alternativa['tag'][i] == 'capacidade':
                    lista_capacidades_respostas_usuario.append(alternativa['tag'][1])
                elif alternativa['tag'][i][0] == 'capacidade':
                    lista_capacidades_respostas_usuario.append(alternativa['tag'][i][1])


print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')

