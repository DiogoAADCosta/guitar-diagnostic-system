'''====================================================================================================================================================================================================
Versão 1 - Mostrar as perguntas e embaralhar as alternativas
====================================================================================================================================================================================================
'''

'''
# Autoavaliação
# autoavaliacao_nivel = input('Qual seu nível? ')
from random import choice, shuffle


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
    # Mostra a pergunta
    print()
    print(questao['pergunta'])
    print()

    # Cria uma cópia da lista de alternativas e embaralha
    alternativas_embaralhadas = (questao['alternativas'])[:]
    shuffle(alternativas_embaralhadas)

    # Dicionário onde vamos guardar as letras das alternativas (A, B, C, etc) com as tags certo/errado para poder contabilizar os acertos.
    mapa_respostas = {}

    # Mostra as alternativas da lista embaralhada com as letras em ordem
    for numero, resposta in enumerate(alternativas_embaralhadas):
        letra = lista_alternativas[numero]
        mapa_respostas[letra] = resposta
        print(f'{letra} - {resposta["texto"]}')


    # Guarda a resposta do usuário - PRÓXIMA ETAPA - CONTABILIZAR OS ERROS E ACERTOS E GUARDAR AS TAGS.
    resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

    if mapa_respostas[resposta_usuario]['correção']:
        print('Você ACERTOU')
    else:
        print('Você ERROU')
'''
