# Version 1 - Question structure with randomized alternatives and basic answer validation

from random import shuffle


lista_perguntas = [
    {'id': '1-1',
    'nível': 1,
    'pergunta': 'Pergunta 1',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'grafia_cifras']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '1-2',
    'nível': 1,
    'pergunta': 'Pergunta 2',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'grafia_cifras']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '1-3',
     'nível': 1,
     'pergunta': 'Pergunta 3',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'grafia_cifras']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
         ]
     }
]
lista_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']



for questao in lista_perguntas:
    print()
    print(questao['pergunta'])
    print()

    # Create a copy of the alternatives and shuffle them to randomize order
    alternativas_embaralhadas = (questao['alternativas'])[:]
    shuffle(alternativas_embaralhadas)

    # Map displayed options (A, B, C...) to their corresponding data
    mapa_respostas = {}

    # Display shuffled alternatives with corresponding letters
    for numero, resposta in enumerate(alternativas_embaralhadas):
        letra = lista_alternativas[numero]
        mapa_respostas[letra] = resposta
        print(f'{letra} - {resposta["texto"]}')


    # Capture user response (input validation is intentionally omitted;
    # in the final version, interaction will be handled via UI buttons)
    resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

    if mapa_respostas[resposta_usuario]['correção']:
        print('Você ACERTOU')
    else:
        print('Você ERROU')
