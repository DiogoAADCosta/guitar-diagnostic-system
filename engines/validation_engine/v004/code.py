# Version 4 - Integration of progression engine (v3) with real answer validation and tag extraction (v2)

from random import shuffle


lista_perguntas = [
    {'id': '2-1',
    'nível': 2,
    'numero_pergunta': 1,
    'pergunta': 'Pergunta 1',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '2-2',
    'nível': 2,
    'numero_pergunta': 2,
    'pergunta': 'Pergunta 2',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '2-3',
     'nível': 2,
     'numero_pergunta': 3,
     'pergunta': 'Pergunta 3',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                     ]
     },
    {'id': '2-4',
    'nível': 2,
    'numero_pergunta': 4,
    'pergunta': 'Pergunta 4',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '2-5',
    'nível': 2,
    'numero_pergunta': 5,
    'pergunta': 'Pergunta 5',
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                     ]
    },
    {'id': '2-6',
     'nível': 2,
     'numero_pergunta': 6,
     'pergunta': 'Pergunta 6',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                     ]
     },
    {'id': '2-7',
     'nível': 2,
     'numero_pergunta': 7,
     'pergunta': 'Pergunta 7',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '2-8',
     'nível': 2,
     'numero_pergunta': 8,
     'pergunta': 'Pergunta 8',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                    ]
     },
    {'id': '3-1',
     'nível': 3,
     'numero_pergunta': 1,
     'pergunta': 'Pergunta 1',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '3-2',
     'nível': 3,
     'numero_pergunta': 2,
     'pergunta': 'Pergunta 2',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '3-3',
     'nível': 3,
     'numero_pergunta': 3,
     'pergunta': 'Pergunta 3',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                    ]
     },
    {'id': '3-4',
     'nível': 3,
     'numero_pergunta': 4,
     'pergunta': 'Pergunta 4',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '3-5',
     'nível': 3,
     'numero_pergunta': 5,
     'pergunta': 'Pergunta 5',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '3-6',
     'nível': 3,
     'numero_pergunta': 6,
     'pergunta': 'Pergunta 6',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                    ]
     },
    {'id': '3-7',
     'nível': 3,
     'numero_pergunta': 7,
     'pergunta': 'Pergunta 7',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '3-8',
     'nível': 3,
     'numero_pergunta': 8,
     'pergunta': 'Pergunta 8',
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
                     {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
                    ]
     },
    {'id': '4-1',
     'nível': 4,
     'numero_pergunta': 1,
     'pergunta': 'Pergunta 1',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '4-2',
     'nível': 4,
     'numero_pergunta': 2,
     'pergunta': 'Pergunta 2',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '4-3',
     'nível': 4,
     'numero_pergunta': 3,
     'pergunta': 'Pergunta 3',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
     ]
     },
    {'id': '4-4',
     'nível': 4,
     'numero_pergunta': 4,
     'pergunta': 'Pergunta 4',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '4-5',
     'nível': 4,
     'numero_pergunta': 5,
     'pergunta': 'Pergunta 5',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '4-6',
     'nível': 4,
     'numero_pergunta': 6,
     'pergunta': 'Pergunta 6',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
     ]
     },
    {'id': '4-7',
     'nível': 4,
     'numero_pergunta': 7,
     'pergunta': 'Pergunta 7',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '4-8',
     'nível': 4,
     'numero_pergunta': 8,
     'pergunta': 'Pergunta 8',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
     ]
     },
    {'id': '5-1',
     'nível': 5,
     'numero_pergunta': 1,
     'pergunta': 'Pergunta 1',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '5-2',
     'nível': 5,
     'numero_pergunta': 2,
     'pergunta': 'Pergunta 2',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '5-3',
     'nível': 5,
     'numero_pergunta': 3,
     'pergunta': 'Pergunta 3',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
     ]
     },
    {'id': '5-4',
     'nível': 5,
     'numero_pergunta': 4,
     'pergunta': 'Pergunta 4',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '5-5',
     'nível': 5,
     'numero_pergunta': 5,
     'pergunta': 'Pergunta 5',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '5-6',
     'nível': 5,
     'numero_pergunta': 6,
     'pergunta': 'Pergunta 6',
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 4'},
         {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 5'}
     ]
     },
    {'id': '5-7',
     'nível': 5,
     'numero_pergunta': 7,
     'pergunta': 'Pergunta 7',
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'acerto']], 'texto': 'Alternativa Certa'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 1'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 2'},
                      {'correção': False, 'tag': [['limitador', 'grafia_cifras']], 'texto': 'Alternativa 3'}
                      ]
     },
    {'id': '5-8',
     'nível': 5,
     'numero_pergunta': 8,
     'pergunta': 'Pergunta 8',
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

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

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
    return nivel, rodada, 4

def descer_nivel(nivel, rodada):
    print('Desce de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    if nivel > 2:
        nivel -= 1
    else:
        print('Nível mínimo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada, 4

# Helper actions designed to be used directly inside rule definitions
def mais_2(nivel, rodada):
    print('Mais 2 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 2

def mais_4(nivel, rodada):
    print('Mais 4 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 4

def confirma_nivel(nivel, rodada):
    print('Confirma nível')
    print(f'Rodada: {rodada}\n')
    rodada = 4
    return nivel, rodada, 0

regras = {
    1: [
        (lambda t: t >= 80, subir_nivel),
        (lambda t: t > 50, mais_2),
        (lambda t: t > 35, mais_4),
        (lambda t: t > 0, mais_2),
        (lambda t: True, descer_nivel)
    ],
    2: [
        (lambda t: t >= 75, subir_nivel),
        (lambda t: t > 65, mais_2),
        (lambda t: t >= 35, confirma_nivel),
        (lambda t: True, descer_nivel)
    ],
    3: [
        (lambda t: t >= 75, subir_nivel),
        (lambda t: t > 35, confirma_nivel),
        (lambda t: True, descer_nivel)
    ]
}


rodada = 1

acertos = 0
erros = 0
total_perguntas = 0
perguntas_restantes = 4  
ultima_pergunta = 0



# Initial self-assessment to determine starting level
autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
if autoavaliacao_nivel == 1:
    # Users at level 1 and 2 start from the same test (level 2)
    nivel = 2
else:
    nivel = autoavaliacao_nivel

# Main execution loop:
# Combines level progression (v3) with real answer validation and tag collection (v2)
# Maximum of 3 rounds per level evaluation
while rodada < 4:

    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')

# Select and present questions based on current level and progression sequence
    for questao in lista_perguntas:
        if questao['nível'] == nivel and questao['numero_pergunta'] > ultima_pergunta:
            print()
            print(f'Nível: {questao["nível"]}')
            print(questao['pergunta'])
            print()
            total_perguntas += 1
            perguntas_restantes -= 1
            ultima_pergunta = questao['numero_pergunta']

            alternativas_embaralhadas = (questao['alternativas'])[:]
            shuffle(alternativas_embaralhadas)

            mapa_respostas = {}

            for numero, resposta in enumerate(alternativas_embaralhadas):
                letra = lista_alternativas[numero]
                mapa_respostas[letra] = resposta
                print(f'{letra} - {resposta["texto"]}')

            resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

            # Validate answer and update performance and tag data
            if mapa_respostas[resposta_usuario]['correção']:
                print('Você ACERTOU')
                acertos += 1
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    lista_capacidades_respostas_usuario.append(tag)
            else:
                print('Você ERROU')
                erros += 1
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    lista_limitadores_respostas_usuario.append(tag)

            # Check if current round reached its question limit
            if perguntas_restantes == 0:
                print('CONFERIR SCORE')
                taxa_acertos = (acertos / total_perguntas) * 100
                print(f'Taxa de acertos: {taxa_acertos:.1f}%')

                print(f'Você acertou {acertos} respostas de um total de {total_perguntas} perguntas. Você acertou {taxa_acertos:.1f}%.')
                print(f'Total erros: {erros}')

                print(f'Lista de capacidades do usuário: {lista_capacidades_respostas_usuario}')
                print(f'Lista de limitadores do usuário: {lista_limitadores_respostas_usuario}')

                # Apply progression rules based on current accuracy
                for condicao, acao in regras[rodada]:
                    if condicao(taxa_acertos):
                        nivel_anterior = nivel
                        nivel, rodada, perguntas_restantes = acao(nivel, rodada)
                        if nivel != nivel_anterior:
                            # Reset performance tracking when level changes
                            acertos = 0
                            erros = 0
                            total_perguntas = 0
                            ultima_pergunta = 0
                        break
                break
    else:
        break
