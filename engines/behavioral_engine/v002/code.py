# Version 2 - Improved Tag Iteration
#
# Goal:
# Simplify tag processing by standardizing the data structure.
#
# In version 1, tags had inconsistent formats, requiring complex checks:
# - alternativa['tag'][i]
# - alternativa['tag'][i][0]
#
# In this version:
# - All tags follow a consistent structure: [type, value]
# - Tags are always stored as a list of pairs: [[type, value], ...]
# - Iteration is done using tuple unpacking: for tipo, tag in ...
#
# This removes the need for index-based access and simplifies the logic.

lista_perguntas = [
    {'pergunta': 'Pergunta 1',
     'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'base']]},                       
                    {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']]},
                    {'resposta': 'C', 'tag': [['limitador', 'troca_de_acorde']]},
                    {'resposta': 'D', 'tag': [['capacidade', 'troca_de_acorde']]}
                    ]
    },
    {'pergunta': 'Pergunta 2',
         'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'ritmo']]},
                        {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']]},
                        {'resposta': 'C', 'tag': [['limitador', 'ritmo']]},
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
            for tipo, tag in alternativa['tag']:      
                if tipo == 'limitador':
                    lista_limitadores_respostas_usuario.append(tag)

                elif tipo == 'capacidade':
                    lista_capacidades_respostas_usuario.append(tag)


print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')
