# Version 3 - Full Dataset and Basic Analysis
#
# Goal:
# Expand the system with real questions and prepare data for diagnosis.
#
# In this version:
# - All questions, answers, and tags are fully defined
# - Each answer includes a 'texto' field for display purposes
# - The system collects user responses and stores tags
#
# Additionally:
# - Tag frequencies are calculated using Counter
# - The most frequent limitations and strengths are identified
#
# This version moves from data structure design to basic data analysis,
# preparing the foundation for generating a diagnosis.


from collections import Counter

# Data model:
# Each question contains multiple answers.
# Each answer contains:
# - 'resposta': identifier used for matching user input
# - 'texto': display text shown to the user
# - 'tag': list of [type, value] pairs (e.g., ['limitador', 'ritmo'])

# 'resposta' is used for internal logic (matching user input)
# 'texto' is used only for display purposes

lista_perguntas = [
    {'pergunta': '1 - Quando monta um acorde, você: ',
     'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não consigo montar nenhum acorde'},                       
                    {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Monta um dedo de cada vez'},
                    {'resposta': 'C', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Monta em blocos (2 dedos + o resto)'},
                    {'resposta': 'D', 'tag': [['capacidade', 'troca_de_acorde']], 'texto': 'Consegue encaixar todos os dedos de uma vez'}
                    ]
    },
    {'pergunta': '2 - Tocando com uma música ou metrônomo, você consegue trocar os acordes sem atrasar o ritmo?',
    'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo nem começar a tocar com a música'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Preciso parar o ritmo para trocar o acorde'},
                   {'resposta': 'C', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo me manter no ritmo'},
                   {'resposta': 'D', 'tag': [['capacidade', 'ritmo']], 'texto': 'Consigo me manter no ritmo, mas escapando às vezes'},
                   {'resposta': 'E', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'O ritmo continua normal'}
                   ]
    },
    {'pergunta': '3 - Quando monta um acorde qualquer, sem pestana, e toca uma corda de cada vez: ',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Há duas ou mais cordas que o som não sai'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Há uma única corda que o som não sai'},
                   {'resposta': 'D', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Você consegue ouvir bem o som de cada corda'}
                   ]
     },
    {'pergunta': '4 - Diagramas Lá maior Shape de A e Shape de E ',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei ler esse diagrama e montar os acordes'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Sei ler o diagrama mas não consigo tocar nenhum'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Toco apenas um e o som não sai legal'},
                   {'resposta': 'D', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Toco apenas um e o som sai legal'},
                   {'resposta': 'E', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Toco os dois e o som não sai legal'},
                   {'resposta': 'F', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Toco os dois sem dificuldade'}
                   ]
     },
    {'pergunta': '5 - Ao fazer um Fá maior com pestana, você consegue ouvir o som das cordas 1, 2, 3?',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'base']], 'texto': 'Não sei quais são as cordas 1, 2, 3'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Não ouço as cordas 1, 2, 3'},
                   {'resposta': 'D', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Ouço apenas uma das cordas'},
                   {'resposta': 'E', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Ouço apenas duas das cordas (uma corda ainda fica com som abafado)'},
                   {'resposta': 'F', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Ouço claramente todas as cordas'}
                   ]
     },
    {'pergunta': '6 - Em uma música aparecem os seguintes acordes: C Am F G. Você:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sabe montar todos os acordes'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Demora pra trocar os acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'troca_de_acorde'], ['capacidade', 'ritmo']], 'texto': 'Tem uma certa dificuldade na hora de trocar de acorde mas ainda consegue acompanhar'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'Consegue trocar de acordes rápido, mas tem dificuldade para se manter no ritmo'},
                   {'resposta': 'E', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'Acha fácil e consegue tocar sem problemas'}
                   ]
     },
    {'pergunta': '7 - Tocando uma música inteira com muitos acordes com pestana:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde'], ['limitador', 'nao_consegue_pestana']], 'texto': 'Não consigo ainda fazer pestana'},
                   {'resposta': 'C', 'tag': [['limitador', 'resistencia']], 'texto': 'Cansa/dói a mão'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo']], 'texto': 'Perco o ritmo'},
                   {'resposta': 'E', 'tag': [['limitador', 'resistencia'], ['capacidade', 'ritmo']], 'texto': 'Cansa a mão um pouco mas toco inteira'},
                   {'resposta': 'F', 'tag': [['capacidade', 'resistencia'], ['capacidade', 'ritmo']], 'texto': 'Toco sem problema'}
                   ]
     },
    {'pergunta': '8 - Se você erra durante uma música, você:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo ainda acompanhar músicas'},
                   {'resposta': 'B', 'tag': [['limitador', 'ritmo']], 'texto': 'Preciso parar a música e voltar para uma parte específica para conseguir voltar a tocar junto'},
                   {'resposta': 'C', 'tag': [['limitador', 'ritmo']], 'texto': 'Consigo voltar a tocar com a música sem parar, mas demoro um  pouco esperando uma parte específica'},
                   {'resposta': 'D', 'tag': [['capacidade', 'continuidade']], 'texto': 'Consigo voltar a tocar com a música quase que imediatamente após o erro'}
                   ]
     },
    {'pergunta': '9 - O que você acha mais difícil?',     # This question will allow multiple answers (handled later in JavaScript)
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Montar os acordes e soar limpos'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Trocas rápidas de acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'base']], 'texto': 'Ler cifras e tablaturas'},
                   {'resposta': 'D', 'tag': [['capacidade', 'ritmo']], 'texto': 'Tocar junto com a música'}
                   ]
     }
]

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

# Main execution loop:
# - Display question and options
# - Capture user input
# - Match answer and collect tags

for questao in lista_perguntas:
    print()
    print(questao['pergunta'])
    print()

    for alternativa in questao['respostas']:
        print(f'{alternativa["resposta"]} - {alternativa["texto"]}')

    # Will be replaced by UI interaction in the final version (JavaScript)
    # Input validation intentionally omitted at this stage
    resposta_usuario = input('\nSua Resposta: ').strip().upper()

    # Collect tags associated with the selected answer
    # Multiple tags per answer allow richer behavioral classification
    for alternativa in questao['respostas']:
        if resposta_usuario == alternativa['resposta']:
            for tipo, tag in alternativa['tag']:
                if tipo == 'limitador':
                    lista_limitadores_respostas_usuario.append(tag)

                elif tipo == 'capacidade':
                    lista_capacidades_respostas_usuario.append(tag)


print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')

# Count frequency of each limitation and strength
# Frequency is used as a simple scoring mechanism for diagnosis
contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)
print(f'Limitadores: {contador_limitadores}')
print(f'Capacidades: {contador_capacidades}')

# Extract most frequent items (strongest signals for diagnosis)
print(f'O item mais frequente em limitadores é {contador_limitadores.most_common(1)}')
print(f'O item mais frequente em capacidades é {contador_capacidades.most_common(1)}')
