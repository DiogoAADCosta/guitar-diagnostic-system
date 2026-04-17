# Version 2 - Track correct and incorrect answers and store capability and limitation tags

from random import shuffle


lista_perguntas = [
    {'id': '1-1',
    'nível': 1,
    'pergunta': 'Pergunta 1',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '1-2',
    'nível': 1,
    'pergunta': 'Pergunta 2',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '1-3',
     'nível': 1,
     'pergunta': 'Pergunta 3',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
         ]
     }
]
lista_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# Counters to track user performance
acertos = 0
erros = 0
total_perguntas = 0

# Store capability and limitation tags extracted from user responses
lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []





for questao in lista_perguntas:
    print()
    print(questao['pergunta'])
    print()
    total_perguntas += 1

    alternativas_embaralhadas = (questao['alternativas'])[:]
    shuffle(alternativas_embaralhadas)

    mapa_respostas = {}

    for numero, resposta in enumerate(alternativas_embaralhadas):
        letra = lista_alternativas[numero]
        mapa_respostas[letra] = resposta
        print(f'{letra} - {resposta["texto"]}')

    resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

    if mapa_respostas[resposta_usuario]['correção']:
        print('Você ACERTOU')
        acertos += 1
        # Store tags associated with correct answers
        for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
            lista_capacidades_respostas_usuario.append(tag)
    else:
        print('Você ERROU')
        erros += 1
        # Store tags associated with incorrect answers
        for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
            lista_limitadores_respostas_usuario.append(tag)

# Calculate accuracy
total_acertos = acertos / total_perguntas
print(f'Você acertou {acertos} respostas de um total de {total_perguntas} perguntas. Você acertou {total_acertos * 100:.1f}%.')
print(f'Total erros: {erros}')

print(f'Lista de capacidades do usuário: {lista_capacidades_respostas_usuario}')
print(f'Lista de limitadores do usuário: {lista_limitadores_respostas_usuario}')

