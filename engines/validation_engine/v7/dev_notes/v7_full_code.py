'''====================================================================================================================================================================================================
Versão 7 - Construção de diagnóstico - Construindo as regras para análise dos resultados. Gerando diagnósticos em forma de frases.
====================================================================================================================================================================================================
'''
from random import shuffle, choice
from collections import Counter
from itertools import chain, repeat


lista_perguntas = [
    {'id': '2-1',
    'nível': 2,
    'numero_pergunta': 1,
    'pergunta': 'Numa música temos os seguintes acordes: G e Bm. Que acordes são esses? ',       # Pipeline: Ler cifra -> Fundamental Acordes -> Qualidade acordes
    'contexto': ['triades_simples'],
    'interface': ['leitura_cifras'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'Sol Maior e Si Menor'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Sol Menor e Si Maior'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Dó Maior e Si Menor'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Lá Maior e Mi Maior'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Dó Maior e Ré Menor'},
                     {'correção': False, 'tag': [['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}            # Adicionando o tipo
                     ]
    },
    {'id': '2-2',
    'nível': 2,
    'numero_pergunta': 2,
    'pergunta': '(Figura do Braço - Am D) Quais cifras correspondem a esses acordes? ',            # Pipeline: Diagrama braço -> Fundamental Acordes -> Qualidade acordes -> Leitura Cifras
    'contexto': ['triades_simples'],
    'interface': ['diagrama_braco', 'leitura_cifras'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'Am, D'},  # preciso de leitura de cifras?
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'A, Dm'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'A, D'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Lá Menor e Ré Maior'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras, mas não sei quais os acordes', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-3',
     'nível': 2,
     'numero_pergunta': 3,
     'pergunta': 'Qual das opções representa um Power Chord B5? (DIAGRAMA BRAÇO NAS RESPOSTAS)',    # Pipeline: Ler Cifra -> Fundamental acorde -> Qualidade Acorde -> Montar no braço -> Associar ao diagrama
     'contexto': ['power_chords'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'B5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Bb5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'C5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'G5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'F#5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras mas não sei qual é o acorde', 'tipo': 'nao_sei'}
                     ]
     },
    {'id': '2-4',
    'nível': 2,
    'numero_pergunta': 4,
    'pergunta': '(Tablatura com notas na corda 6) Você toca isso em qual corda? (TABLATURA)',       # Pipeline: Ler tablatura -> Saber a ordem das cordas
    'contexto': ['leitura_tablatura_basica'],
    'interface': ['leitura_tablatura'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_tablatura']], 'texto': 'Na mais grossa'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Na mais fina'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Em alguma corda do meio'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-5',
    'nível': 2,
    'numero_pergunta': 5,
    'pergunta': 'Qual das opções representa um Dó Maior e um Ré Menor? (GRAFIA CIFRAS)',    # Pipeline: Recebe acorde -> Traduz nota fundamental -> traduz qualidade acorde
    'contexto': ['triades_simples'],
    'interface': ['leitura_cifras'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'C, Dm'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'C, D'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'G, Dm'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'B, F'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'E, Am'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-6',
     'nível': 2,
     'numero_pergunta': 6,
     'pergunta': '(Figura do Braço - dois acordes - menor maior) Esses acordes são, respectivamente: (DIAGRAMA BRAÇO)',   # Pipeline: Diagrama -> qualidade acorde
     'contexto': ['triades_simples'],
     'interface': ['diagrama_braco'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde']], 'texto': 'Menor, Maior'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Menor, Menor'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Maior, Maior'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Maior, Menor'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler a figura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                     ]
     },
    {'id': '2-7',
     'nível': 2,
     'numero_pergunta': 7,
     'pergunta': 'Qual das opções temos um acorde Menor? (DIAGRAMA  BRAÇO NAS RESPOSTAS)',   # Pipeline: Diagrama -> qualidade acorde
     'contexto': ['triades_simples'],
     'interface': ['diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde']], 'texto': 'Diagrama do braço - Am'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Diagrama do braço - E'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Diagrama do braço - D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Diagrama do braço - C'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Diagrama do braço - G'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '2-8',
     'nível': 2,
     'numero_pergunta': 8,
     'pergunta': '(Tablatura do acorde F5) Que Power Chord é esse? (TABLATURA)',    # Pipeline: leitura tablatura -> Fundamental acorde -> Leitura Cifra
     'contexto': ['power_chords'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'fundamental_acorde']], 'texto': 'F5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'E5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'G5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'C5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'A5'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler a tablatura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                    ]
     },
    {'id': '3-1',
     'nível': 3,
     'numero_pergunta': 1,
     'pergunta': 'Quais cifras correspondem aos acordes Si Bemol Menor e Fá Sustenido Maior? (GRAFIA CIFRAS)',   # Pipeline:  Acordes -> Fundamental Acorde -> Qualidade acorde
     'contexto': ['triades_simples'],
     'interface': ['leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'Bbm, F#'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Bb, F#m'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Bbm, G#'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Bb, G#m'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-2',
     'nível': 3,
     'numero_pergunta': 2,
     'pergunta': '(Figura do Braço - C7M, Dm7 - shapes simples) Quais cifras correspondem a esses acordes? (DIAGRAMA BRAÇO)',   # Pipeline: Diagrama -> Fundamental Acordes -> Qualidade acordes -> Leitura Cifras
     'contexto': ['tetrades_simples'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'C7M, Dm7'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'C7M, Em7'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'C7, E7M'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Dó Maior com sétima maior, Ré menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Dó menor com sétima, Mi menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Consigo ler as figuras, mas não sei quais os acordes', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Consigo ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-3',
     'nível': 3,
     'numero_pergunta': 3,
     'pergunta': 'Marque a opção que temos o mesmo acorde representado de maneiras diferentes (DIAGRAMA BRAÇO NAS RESPOSTAS)',  # Pipeline: Leitura de tudo
     'contexto': ['triades_simples'],
     'interface': ['leitura_cifras', 'diagrama_braco', 'leitura_tablatura'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': '(Cifra, diagrama e tab) F - F shape  E - F shape E'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(Cifra, diagrama e tab) A - A shape A - Am shape A'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': '(Cifra, diagrama e tab) A - Gm shape E - A shape A '},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': '(Cifra, diagrama e tab) G - F shape E - C shape A'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Sei ler a cifra mas não sei ler as figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Sei ler as figuras mas não sei ler a cifra', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_tablatura'], ['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei nem começar', 'tipo': 'nao_sei'}
                    ]
     },
    {'id': '3-4',
     'nível': 3,
     'numero_pergunta': 4,
     'pergunta': 'Qual das opções representa um D7M? (TABLATURA)',   # Pipeline Leitura Cifra -> Fundamental -> Qualidade acorde -> Tablatura
     'contexto': ['tetrades_simples'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': 'Tablatura - D7M shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Tablatura - Dm shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Tablatura - D(#5) shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Tablatura - D7 shape D'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Sei ler a cifra mas não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Sei ler as figuras mas não sei ler a cifra', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei nem começar', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-5',
     'nível': 3,
     'numero_pergunta': 5,
     'pergunta': '(Figura do Braço - G7, Am7) Esses diagramas representam acordes: (DIAGRAMA BRAÇO)',  # Pipeline: Diagrama -> Qualidade Acorde
     'contexto': ['tetrades_simples'],
     'interface': ['diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde']], 'texto': 'Maior com sétima, Menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Menor com sétima, Maior com sétima'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Menor com sétima, Menor com sétima maior'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Maior com sétima maior, Maior com sétima'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Maior com sétima maior, Menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-6',
     'nível': 3,
     'numero_pergunta': 6,
     'pergunta': 'Em qual opção temos os acordes F7M e Fm7? (TABLATURA)',  # Pipeline: Leitura Cifra -> Fundamental -> Qualidade -> Tablatura
     'contexto': ['tetrades_simples'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': 'Tablatura - F7M shape E, Fm7 shape A'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Tablatura - F7M shape A, Fm tríade shape E'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Tablatura - F7 shape E, Fm7 shape D'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Tablatura - G7M shape E, Cm7 shape A'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Sei ler tablatura mas não sei que acordes são', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Sei ler tablatura, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                    ]
     },
    {'id': '3-7',
     'nível': 3,
     'numero_pergunta': 7,
     'pergunta': 'O acorde Cm7 pode ser escrito como: (DIAGRAMA BRAÇO NAS RESPOSTAS)',  # Pipeline: leitura Cifra -> fundamental -> qualidade -> diagrama
     'contexto': ['tetrades_simples'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': '(dois diagramas) - Cm7 shape E, Cm7 shape A'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(dois diagramas) - Cm tríade shape E, Cm tríade shape A'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': '(dois diagramas) - Cm7 shape A, Dm7 shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': '(dois diagramas) - C7M shape A, G7 shape E'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-8',
     'nível': 3,
     'numero_pergunta': 8,                   # Pipeline: Tablatura -> Fundamental -> Qualidade -> Leitura cifras -> intervalos
     'pergunta': '(Tablatura G7M shape E) Partindo do acorde na tablatura - 1. Que acorde é esse? 2. Em qual corda devemos mudar a casa para ter um acorde Maior com sétima? (TABLATURA)',
     'contexto': ['tetrades_simples'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras'], ['capacidade', 'intervalos']], 'texto': 'G7M, corda 4'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'F7M, corda 4'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'G7, corda 3'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'leitura_tablatura']], 'texto': 'F7, corda 1'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'leitura_tablatura']], 'texto': 'Em7, corda 1'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Consigo ler a tablatura mas não sei dizer o acorde', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': 'Consigo ler a tablatura, sei o acorde mas não sei qual corda', 'tipo': 'nao_sei'}
                    ]
     },
    {'id': '4-1',
     'nível': 4,
     'numero_pergunta': 1,                      # Pipeline: Cifra -> Interpretação
     'pergunta': 'Você está tocando uma música junto com um baixista e de repente aparece na cifra o acorde D/C. Você toca qual acorde?',
     'contexto': ['inversoes'],
     'interface': ['leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'D'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'C'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-2',
     'nível': 4,
     'numero_pergunta': 2,
     'pergunta': 'Quais outras opções para tocar esse mesmo acorde? (Figura do braço com C shape C)',   # Pipeline: diagrama -> Fundamental -> Qualidade -> Diagrama
     'contexto': ['shapes_caged_triades'],
     'interface': ['diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde'], ['capacidade', 'fundamental_acorde']], 'texto': 'Diagramas do braço - C shape A, C shape G, C shape D'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Diagramas do braço - C shape E, C shape D, B shape A'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Diagramas do braço - C shape G, G shape E, D shape C'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Diagramas do braço - A shape A, Cm shape E, F shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Diagramas do braço - Cm, shape A, Cm shape E, Cm shape D'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'],  ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-3',
     'nível': 4,
     'numero_pergunta': 3,
     'pergunta': '(Diagrama do braço - Lá maior com pestana e corda solta) Esses dois shapes representam quais acordes?',   # Pipeline: diagrama -> fundamental -> qualidade -> Leitura cifras
     'contexto': ['shapes_caged_triades'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'A,  A'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Am, A '},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'E, A'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'E, G'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'E, Cm'},
         {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler a figura', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Sei ler a figura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
     ]
     },
    {'id': '4-4',
     'nível': 4,
     'numero_pergunta': 4,
     'pergunta': '(Tab com bend, slide e hammer-on) Qual dessas opções descreve corretamente a execução dessa frase??',    # Pipeline: Leitura tablatura -> Interpretação símbolos
     'contexto': ['leitura_tablatura_articulacoes'],
     'interface': ['leitura_tablatura'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_tablatura']], 'texto': 'Bend, Slide e Hammer-On'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura']], 'texto': 'Slide, Bend e Pull-Off'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura']], 'texto': 'Pull-Off, Tapping, Ligadura'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura']], 'texto': 'Bend, Ligadura, Ghost Note'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-5',
     'nível': 4,
     'numero_pergunta': 5,
     'pergunta': 'Na cifra aparece E/G#. O que isso significa? ',     # Pipeline: leitura cifra -> Interpretação Cifra
     'contexto': ['inversoes'],
     'interface': ['leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'Acorde E com G# no baixo'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Acorde G# com E no baixo'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Dois acordes tocados ao mesmo tempo'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Acorde E sem a nota G#'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Acorde G# sem a nota E'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-6',
     'nível': 4,
     'numero_pergunta': 6,
     'pergunta': '(Diagrama braço - Ab shape G, F# shape C) Que acordes são esses?',   # Pipeline: Diagrama -> fundamental -> Qualidade -> Leitura Cifras
     'contexto': ['shapes_caged_triades'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'Ab, F#'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'G, C'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Gm, Cm'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Abm, C'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Ab, F#m'},
         {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Sei ler as figuras mas não sei que acordes são', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Sei ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
     ]
     },
    {'id': '4-7',
     'nível': 4,
     'numero_pergunta': 7,
     'pergunta': 'Qual das opções corresponde aos acordes Eb, Fm e Bm(b5)',    # Pipeline: Leitura Cifras -> Qualidade -> Fundamentais -> Diagrama
     'contexto': ['shapes_caged_triades'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': '(três diagramas) - Eb shape C, Fm shape E, Bm(b5) shape A'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(três diagramas) - Eb shape A, Fm shape D, Bm shape A'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': '(três diagramas) - D shape C, Em shape D, B(#5) shape A'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(três diagramas) - Ebm shape D, F shape E, B(#5) shape C'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']],'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False,'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']],'texto': 'Sei ler as figuras mas não sei que acordes são', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']],'texto': 'Sei ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-8',
     'nível': 4,
     'numero_pergunta': 8,
     'pergunta': 'Qual dessas posições representa C/E e Dm/C?',     # Pipeline:  Leitura Cifras  -> interpretar baixo -> encontrar nota baixo no braço -> combinar com acorde shapes CAGED -> leitura tablatura
     'contexto': ['inversoes'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': '(tablatura) - 032010 e x3x231'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': '(tablatura) 332010 e x3x231'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': '(tablatura) - 032010 e 1x0231'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(tablatura) - 03555x e x3x232'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': '(tablatura) - 0x5543 e x00231'},
         {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']],'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'leitura_cifras']],'texto': 'Não sei o que significam essas cifras', 'tipo': 'nao_sei'}
     ]
     },
    {'id': '5-1',
     'nível': 5,
     'numero_pergunta': 1,
     'pergunta': 'Você está tocando sozinho em casa e se depara com a cifra F/G. Qual acorde você toca?',    # Pipeline: Leitura cifras -> interpretar baixo -> interpretar intervalos -> construção acorde -> leitura cifras
     'contexto': ['inversoes', 'extensoes'],
     'interface': ['leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras'], ['capacidade', 'intervalos']], 'texto': 'G7sus4(9)'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'F'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'G'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'F7M'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'F7(9)'},
                      {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': 'G7(13)'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '5-2',
     'nível': 5,
     'numero_pergunta': 2,
     'pergunta': '(Figura do braço = F#7M(#11)) Este acorde possui:',       # Pipeline: Diagrama -> Qualidade + intervalos (extensões)
     'contexto': ['extensoes'],
     'interface': ['diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco']], 'texto': '7ª maior e #11'},
                      {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': '7ª maior e 13 maior'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': '7ª menor e 9 menor'},
                      {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': '7ª maior e 9 maior'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': '7ª menor e 13 maior'},
                      {'correção': False, 'tag': [ ['limitador', 'intervalos']], 'texto': '7ª maior e #5'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler a figura', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'Sei ler a figura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '5-3',
     'nível': 5,
     'numero_pergunta': 3,
     'pergunta': 'Qual opção corresponde ao acorde C7(9) e G7(13)?  (DIAGRAMA BRAÇO NAS RESPOSTAS)',    # Pipeline: Leitura Cifras -> Qualidade + intervalos (extensões) -> diagrama
     'contexto': ['extensoes'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': '(Diagrama braço) - C7(9) x3233x - G7(13) 3x345x'},
         {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': '(Diagrama braço) C7(b9) x3232x - G7(b13) 3x344x'},
         {'correção': False, 'tag': [['limitador', 'intervalos'], ['limitador', 'qualidade_acorde']], 'texto': '(Diagrama braço) - C7M(9) x3243x - G7(#11)  3x342x'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(Diagrama braço) - Cm7(9)  x3133x - G7M(13) 3x445x'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': '(Diagrama braço) C7(13) x3x355 - G7sus4(9) - 3x321x'},
         {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'intervalos'], ['limitador', 'qualidade_acorde']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
     ]
     },
    {'id': '5-4',
     'nível': 5,
     'numero_pergunta': 4,
     'pergunta': '(Tablatura - acorde D meio diminuto shape C) Que acorde é esse?',    # Pipeline: Tablatura -> shapes caged -> construção acordes qualidade (intervalos) -> Leitura Cifras
     'contexto': ['shapes_caged_tetrades'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': 'DØ'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Fm(9)'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Dm7M'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Fº'},
                      {'correção': False, 'tag': [ ['limitador', 'qualidade_acorde']], 'texto': 'F7(b5)'},
                      {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei  ler a tablatura', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Sei ler a tablatura mas não sei interpretar as respostas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '5-5',
     'nível': 5,
     'numero_pergunta': 5,
     'pergunta': '(Figura do braço - Am7(9)/C  x35200) Qual cifra corresponde a esse acorde?',     # Pipeline: diagrama -> qualidade acorde, intervalos (extensões) -> nota do baixo -> leitura cifras
     'contexto': ['inversoes', 'extensoes'],
     'interface': ['diagrama_braco', 'leitura_cifras'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras'], ['capacidade', 'diagrama_braco']], 'texto': 'Am7(9)/C'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Am7(9)'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'C7M(9)'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Cm7(13)'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Cm7(13)/G'},
                      {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': 'Am7(11)/C'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler a figura', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'intervalos'], ['limitador', 'qualidade_acorde'], ['limitador', 'leitura_cifras']], 'texto': 'Sei ler a figura mas não consigo interpretar as respostas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '5-6',
     'nível': 5,
     'numero_pergunta': 6,
     'pergunta': 'Qual desses acordes possui 9 maior e 13 maior?',   # Pipeline: intervalos -> qualidade + extensões -> diagrama braço
     'contexto': ['extensoes'],
     'interface': ['diagrama_braco'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'intervalos']], 'texto': '(Diagrama do braço) D7M(9) shape A, C7M(13) shape A'},
         {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': '(Diagrama do braço) G7(#11) shape E, F7M(#11) shape D'},
         {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': '(Diagrama do braço) E7(9) shape D, A(add9) shape A'},
         {'correção': False, 'tag': [ ['limitador', 'intervalos']], 'texto': '(Diagrama do braço) F7M(#5) shape E, G7sus4(9) (F/G)'},
         {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': 'Sei ler as figuras mas não sei interpretar as respostas', 'tipo': 'nao_sei'}
     ]
     },
    {'id': '5-7',
     'nível': 5,
     'numero_pergunta': 7,
     'pergunta': 'Em qual opção temos apenas o acorde D7?',     # Pipeline:  Leitura cifras -> qualidade acorde -> diagramas
     'contexto': ['shapes_caged_tetrades'],
     'interface': ['diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': '(três diagramas) - D7 shapes - A, D, C'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(três diagramas) - D7 shape E, D7M shape D, D(#5) shape C'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': '(três diagramas) - D7 shape A, D7M shape C, G shape E'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': '(três diagramas) - D7M shape A, C7 shape C, D7 shape D'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': '(três diagramas) - Não sei ler essas figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': '(três diagramas) - Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '5-8',
     'nível': 5,
     'numero_pergunta': 8,
     'pergunta': '(tablatura E7M(#11) shape C) Qual cifra corresponde a esse acorde?',   # Pipeline: tablatura -> qualidade acorde + intervalos -> leitura cifra
     'contexto': ['shapes_caged_tetrades', 'extensoes'],
     'interface': ['leitura_tablatura', 'leitura_cifras'],
     'alternativas': [
         {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'leitura_cifras']], 'texto': 'E7M(#11)'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'E7(#11)'},
         {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'E7(9)'},
         {'correção': False, 'tag': [['limitador', 'intervalos']], 'texto': 'E7M(13)'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'D7(#11)'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'D7(b13)'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'intervalos']], 'texto': 'D7M(13)'},
         {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'D7M(#11)'},
         {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
         {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'qualidade_acorde'], ['limitador', 'intervalos']], 'texto': 'Consigo ler as tablaturas mas não sei responder', 'tipo': 'nao_sei'}
     ]
     }
]
lista_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []
lista_contexto_limitadores = []
lista_contexto_capacidades = []
lista_interface_limitadores = []
lista_interface_capacidades = []
conexao_contexto_limitadores = []
conexao_contexto_capacidades = []
conexao_interface_limitadores = []
conexao_interface_capacidades = []
conexao_interface_contexto_limitadores = []
conexao_interface_contexto_capacidades = []

# Contadores para não repetir teste em nível já feito
ja_subiu_nivel = False
ja_desceu_nivel = False

# Função de subir nível
def subir_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Sobe de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    ja_subiu_nivel = True
    if nivel < 5:
        if not (ja_subiu_nivel and ja_desceu_nivel):
            nivel += 1
    else:
        print('Nível máximo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada, 4, ja_subiu_nivel, ja_desceu_nivel

# Função de descer nível
def descer_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Desce de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    ja_desceu_nivel = True
    if nivel > 2:
        if not (ja_subiu_nivel and ja_desceu_nivel):
            nivel -= 1
    else:
        nivel -= 1
        print('Nível mínimo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada, 4, ja_subiu_nivel, ja_desceu_nivel

# Criei as outras funções para que funcionem direto dentro da lista de regras de troca de nível
def mais_2(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Mais 2 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 2, ja_subiu_nivel, ja_desceu_nivel

def mais_4(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Mais 4 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 4, ja_subiu_nivel, ja_desceu_nivel

def confirma_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Confirma nível')
    print(f'Rodada: {rodada}\n')
    rodada = 4
    return nivel, rodada, 0, ja_subiu_nivel, ja_desceu_nivel

# Regras para subir, continuar, descer, confirmar nível, de acordo com cada rodada
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

# Definindo qual será a pergunta limite para cada rodada
rodada = 1
# limites = {1: 4, 2: 6, 3: 8}

# Definindo contadores de acertos, erros e total de perguntas
acertos = 0
erros = 0
total_perguntas = 0
perguntas_restantes = 4   # A primeira rodada sempre começará com 4 perguntas
ultima_pergunta = 0



# Autoavaliação de Nível
nivel_real = 0
autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
if autoavaliacao_nivel == 1:
    # Necessário pois as pessoas no nível 1 e 2 começarão pelo mesmo teste nível 2.
    nivel = 2
else:
    nivel = autoavaliacao_nivel

# São no máximo 3 rodadas de perguntas
while rodada < 4:
    # Definindo qual será a pergunta limite para cada rodada
    # pergunta_limite = limites[rodada]
    # Pega sempre o valor correspondente à chave e retorna zero caso a chave não exista
    # limite_anterior = limites.get(rodada - 1, 0)

    # Verifica se está voltando para um nível que já aconteceu. Interrompe caso verdadeiro.
    if ja_subiu_nivel == True and ja_desceu_nivel == True:
        break

    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')

    # Mostrar as perguntas, as alternativas, coletar e salvar as respostas e contabilizar acertos, erros e tags
    for questao in lista_perguntas:
        # Compara o nível definido pelo usuário para mostrar apenas perguntas de mesmo nível. Pula as perguntas repetidas na nova repetição.
        if questao['nível'] == nivel and questao['numero_pergunta'] > ultima_pergunta:
            # Mostra a pergunta
            print()
            print(f'Nível: {questao["nível"]}')
            print(questao['pergunta'])
            print()
            total_perguntas += 1
            perguntas_restantes -= 1
            ultima_pergunta = questao['numero_pergunta']

            # Cria listas com alternativas para embaralhar e outra com respostas 'não sei' para serem as últimas alternativas de todas
            alternativas_para_embaralhar = []
            alternativas_nao_sei = []

            for alternativa in questao['alternativas']:
                if alternativa.get('tipo') != 'nao_sei':
                    alternativas_para_embaralhar.append(alternativa)
                else:
                    alternativas_nao_sei.append(alternativa)
            # Embaralha as alternativas válidas
            # shuffle(alternativas_para_embaralhar)           # Desabilitar aqui para fazer as simulações
            alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


            # Dicionário onde vamos guardar as letras das alternativas (A, B, C, etc) com as tags certo/errado para poder contabilizar os acertos.
            mapa_respostas = {}

            # Mostra as alternativas da lista embaralhada com as letras em ordem
            for numero, resposta in enumerate(alternativas_para_mostrar):
                letra = lista_alternativas[numero]
                mapa_respostas[letra] = resposta
                print(f'{letra} - {resposta["texto"]}')
            # print(mapa_respostas)

            # Guarda a resposta do usuário - Aqui não vamos validar a resposta do usuário pois na versão final terão botões com as alternativas. Dessa forma não terá como inserir uma resposta inválida.
            resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

            #Corrige a resposta do usuário
            if mapa_respostas[resposta_usuario]['correção']:
                print('Você ACERTOU')
                acertos += 1
                # Guarda a tag e contexto correspondentes ao acerto do usuário
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    # Lista apenas de tags mais frequentes
                    lista_capacidades_respostas_usuario.append(tag)
                    # Para vincular tags com contexto
                    for contexto in questao['contexto']:
                        conexao_contexto_capacidades.append((tag, contexto))
                    # Para vincular tags com interface
                    for interface in questao['interface']:
                        conexao_interface_capacidades.append((tag, interface))
                        # Para vincular tags com interface e contexto
                        for contexto in questao['contexto']:
                            conexao_interface_contexto_capacidades.append((tag, contexto, interface))
                # Para listar apenas os contextos únicos de cada pergunta
                for contexto in questao['contexto']:
                    lista_contexto_capacidades.append(contexto)
                # Para listar apenas as interfaces únicas de cada pergunta
                for interface in questao['interface']:
                    lista_interface_capacidades.append(interface)

            else:
                print('Você ERROU')
                erros += 1
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    # Lista apenas de tags mais frequentes
                    lista_limitadores_respostas_usuario.append(tag)
                    # Para vincular tags com contexto
                    for contexto in questao['contexto']:
                        conexao_contexto_limitadores.append((tag, contexto))
                    # Para vincular tags com interface
                    for interface in questao['interface']:
                        conexao_interface_limitadores.append((tag, interface))
                        # Para vincular tags com interface e contexto
                        for contexto in questao['contexto']:
                            conexao_interface_contexto_limitadores.append((tag, contexto, interface))
                # Para listar apenas os contextos únicos de cada pergunta
                for contexto in questao['contexto']:
                    lista_contexto_limitadores.append(contexto)
                # Para listar apenas as interfaces únicas de cada pergunta
                for interface in questao['interface']:
                    lista_interface_limitadores.append(interface)

            # Conferir a pontuação caso chegue na pergunta limite da rodada - para saber se troca de nível, continua ou confirma
            # if questao['numero_pergunta'] == pergunta_limite:
            if perguntas_restantes <= 0:
                print('CONFERIR SCORE')
                taxa_acertos = (acertos / total_perguntas) * 100
                print(f'Taxa de acertos: {taxa_acertos:.1f}%')

                print(f'Você acertou {acertos} respostas de um total de {total_perguntas} perguntas. Você acertou {taxa_acertos:.1f}%.')
                print(f'Total erros: {erros}')

                print(f'Lista de capacidades do usuário (TAGS): {lista_capacidades_respostas_usuario}')
                print(f'Lista de limitadores do usuário (TAGS): {lista_limitadores_respostas_usuario}')

                print(f'Lista de capacidades do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_capacidades}')
                print(f'Lista de limitadores do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_limitadores}')

                print(f'Lista de contextos capacidades(CONTEXTO): {lista_contexto_capacidades}')
                print(f'Lista de contextos limitadores (CONTEXTO): {lista_contexto_limitadores}')

                # Para guardar os resultados e mostrar ao final do teste antes de zerar.
                acertos_final = acertos
                erros_final = erros
                total_perguntas_final = total_perguntas

                # Rodar as condições na lista de regras
                for condicao, acao in regras[rodada]:
                    if condicao(taxa_acertos):
                        nivel_anterior = nivel
                        nivel, rodada, perguntas_restantes, ja_subiu_nivel, ja_desceu_nivel = acao(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel)
                        if nivel != nivel_anterior:
                            # Zera o número de acertos e erros apenas quando troca de nível
                            acertos = 0
                            erros = 0
                            total_perguntas = 0
                            ultima_pergunta = 0
                        break
                break
    else:
        break

# Confirmando o nível real da pessoa
nivel_real = nivel

print(f'Nível real confirmado: {nivel_real}')
print(f'Nível autoavaliação: {autoavaliacao_nivel}')

# CONTABILIZANDO RESULTADOS ===============================================================================================================================================================
# =========================================================================================================================================================================================

print(f'{" CONSTRUÇÃO DE DIAGNÓSTICO ":=^150}')
# Leitura dos dados
print(f'Taxa de acertos: {taxa_acertos:.1f}%')

print(f'Você acertou {acertos_final} respostas de um total de {total_perguntas_final} perguntas. Você acertou {taxa_acertos:.1f}%.')
print(f'Total erros: {erros_final}')

print('\n\nLISTAS DE TAGS E CONTEXTOS')

print(f'Lista de limitadores do usuário (TAGS): {lista_limitadores_respostas_usuario}')
print(f'Lista de capacidades do usuário (TAGS): {lista_capacidades_respostas_usuario}')

print(f'Lista de contextos limitadores (CONTEXTO): {lista_contexto_limitadores}')
print(f'Lista de contextos capacidades(CONTEXTO): {lista_contexto_capacidades}')

print(f'Lista de interfaces limitadores (INTERFACES): {lista_interface_limitadores}')
print(f'Lista de interfaces capacidades(INTERFACES): {lista_interface_capacidades}')

print(f'Lista de limitadores do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_limitadores}')
print(f'Lista de capacidades do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_capacidades}')

print(f'Lista de limitadores do usuário em interface (TAGS + INTERFACES): {conexao_interface_limitadores}')
print(f'Lista de capacidades do usuário em interface (TAGS + INTERFACES): {conexao_interface_capacidades}')

print(f'Lista de limitadores do usuário em contexto e interface (TAGS + CONTEXTO + INTERFACES): {conexao_interface_contexto_limitadores}')
print(f'Lista de capacidades do usuário em contexto e interface (TAGS + CONTEXTO + INTERFACES): {conexao_interface_contexto_capacidades}')


# Contabiliza a quantidade que cada tag apareceu
contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)
contador_contexto_limitadores = Counter(lista_contexto_limitadores)
contador_contexto_capacidades = Counter(lista_contexto_capacidades)
contador_interface_limitadores = Counter(lista_interface_limitadores)
contador_interface_capacidades = Counter(lista_interface_capacidades)
contador_conexao_contexto_limitadores = Counter(conexao_contexto_limitadores)
contador_conexao_contexto_capacidades = Counter(conexao_contexto_capacidades)
contador_conexao_interface_limitadores = Counter(conexao_interface_limitadores)
contador_conexao_interface_capacidades = Counter(conexao_interface_capacidades)
contador_conexao_interface_contexto_limitadores = Counter(conexao_interface_contexto_limitadores)
contador_conexao_interface_contexto_capacidades = Counter(conexao_interface_contexto_capacidades)

print('\n\nCONTADORES')
print(f'Limitadores: {contador_limitadores}')
print(f'Capacidades: {contador_capacidades}')
print(f'Contexto Limitadores: {contador_contexto_limitadores}')
print(f'Contexto Capacidades: {contador_contexto_capacidades}')
print(f'Interface Limitadores: {contador_interface_limitadores}')
print(f'Interface Capacidades: {contador_interface_capacidades}')
print(f'Conexão Contexto Limitadores: {contador_conexao_contexto_limitadores}')
print(f'Conexão Contexto Capacidades: {contador_conexao_contexto_capacidades}')
print(f'Conexão Interface Limitadores: {contador_conexao_interface_limitadores}')
print(f'Conexão Interface Capacidades: {contador_conexao_interface_capacidades}')
print(f'Conexão Interface Contexto Limitadores: {contador_conexao_interface_contexto_limitadores}')
print(f'Conexão Interface Contexto Capacidades: {contador_conexao_interface_contexto_capacidades}')


# Pega apenas os valores dos dicionários contador_ e qual o valor máximo presente
maior_frequencia_limitadores = max(contador_limitadores.values(), default=0)
maior_frequencia_capacidades = max(contador_capacidades.values(), default=0)
maior_frequencia_contexto_limitadores = max(contador_contexto_limitadores.values(), default=0)
maior_frequencia_contexto_capacidades = max(contador_contexto_capacidades.values(), default=0)
maior_frequencia_interface_limitadores = max(contador_interface_limitadores.values(), default=0)
maior_frequencia_interface_capacidades = max(contador_interface_capacidades.values(), default=0)
maior_frequencia_conexao_contexto_limitadores = max(contador_conexao_contexto_limitadores.values(), default=0)
maior_frequencia_conexao_contexto_capacidades = max(contador_conexao_contexto_capacidades.values(), default=0)
maior_frequencia_conexao_interface_limitadores = max(contador_conexao_interface_limitadores.values(), default=0)
maior_frequencia_conexao_interface_capacidades = max(contador_conexao_interface_capacidades.values(), default=0)
maior_frequencia_conexao_interface_contexto_limitadores = max(contador_conexao_interface_contexto_limitadores.values(), default=0)
maior_frequencia_conexao_interface_contexto_capacidades = max(contador_conexao_interface_contexto_capacidades.values(), default=0)

print('\n\nMAIORES VALORES')
print(f'Limitadores: {maior_frequencia_limitadores}')
print(f'Capacidades: {maior_frequencia_capacidades}')
print(f'Contexto Limitadores: {maior_frequencia_contexto_limitadores}')
print(f'Contexto Capacidades: {maior_frequencia_contexto_capacidades}')
print(f'Interface Limitadores: {maior_frequencia_interface_limitadores}')
print(f'Interface Capacidades: {maior_frequencia_interface_capacidades}')
print(f'Conexão Contexto Limitadores: {maior_frequencia_conexao_contexto_limitadores}')
print(f'Conexão Contexto Capacidades: {maior_frequencia_conexao_contexto_capacidades}')
print(f'Conexão Interface Limitadores: {maior_frequencia_conexao_interface_limitadores}')
print(f'Conexão Interface Capacidades: {maior_frequencia_conexao_interface_capacidades}')
print(f'Conexão Interface Contexto Limitadores: {maior_frequencia_conexao_interface_contexto_limitadores}')
print(f'Conexão Interface Contexto Capacidades: {maior_frequencia_conexao_interface_contexto_capacidades}')


# Lista com os mais frequentes
limitadores_mais_frequentes = [item for item, quantidade in contador_limitadores.items() if (quantidade == maior_frequencia_limitadores and quantidade >= 2)]
capacidades_mais_frequentes = [item for item, quantidade in contador_capacidades.items() if (quantidade == maior_frequencia_capacidades and quantidade >= 2)]
contexto_limitadores_mais_frequentes = [item for item, quantidade in contador_contexto_limitadores.items() if (quantidade == maior_frequencia_contexto_limitadores and quantidade >= 2)]
contexto_capacidades_mais_frequentes = [item for item, quantidade in contador_contexto_capacidades.items() if (quantidade == maior_frequencia_contexto_capacidades and quantidade >= 2)]
interface_limitadores_mais_frequentes = [item for item, quantidade in contador_interface_limitadores.items() if (quantidade == maior_frequencia_interface_limitadores and quantidade >= 2)]
interface_capacidades_mais_frequentes = [item for item, quantidade in contador_interface_capacidades.items() if (quantidade == maior_frequencia_interface_capacidades and quantidade >= 2)]
conexao_contexto_limitadores_mais_frequentes = [item for item, quantidade in contador_conexao_contexto_limitadores.items() if (quantidade == maior_frequencia_conexao_contexto_limitadores and quantidade >= 2)]
conexao_contexto_capacidades_mais_frequentes = [item for item, quantidade in contador_conexao_contexto_capacidades.items() if (quantidade == maior_frequencia_conexao_contexto_capacidades and quantidade >= 2)]
conexao_interface_limitadores_mais_frequentes = [item for item, quantidade in contador_conexao_interface_limitadores.items() if (quantidade == maior_frequencia_conexao_interface_limitadores and quantidade >= 2)]
conexao_interface_capacidades_mais_frequentes = [item for item, quantidade in contador_conexao_interface_capacidades.items() if (quantidade == maior_frequencia_conexao_interface_capacidades and quantidade >= 2)]
conexao_interface_contexto_limitadores_mais_frequentes = [item for item, quantidade in contador_conexao_interface_contexto_limitadores.items() if (quantidade == maior_frequencia_conexao_interface_contexto_limitadores and quantidade >= 2)]
conexao_interface_contexto_capacidades_mais_frequentes = [item for item, quantidade in contador_conexao_interface_contexto_capacidades.items() if (quantidade == maior_frequencia_conexao_interface_contexto_capacidades and quantidade >= 2)]

print('\n\nITENS MAIS FREQUENTES')
print(f'O item mais frequente em Limitadores é: {limitadores_mais_frequentes}')
print(f'O item mais frequente em Capacidades é: {capacidades_mais_frequentes}')
print(f'O item mais frequente em Contexto - Limitadores é: {contexto_limitadores_mais_frequentes}')
print(f'O item mais frequente em Contexto - Capacidades é: {contexto_capacidades_mais_frequentes}')
print(f'O item mais frequente em Interface - Limitadores é: {interface_limitadores_mais_frequentes}')
print(f'O item mais frequente em Interface - Capacidades é: {interface_capacidades_mais_frequentes}')
print(f'O item mais frequente em Conexão - Limitadores - Contexto é: {conexao_contexto_limitadores_mais_frequentes}')
print(f'O item mais frequente em Conexão - Capacidades - Contexto é: {conexao_contexto_capacidades_mais_frequentes}')
print(f'O item mais frequente em Conexão - Limitadores - Interface é: {conexao_interface_limitadores_mais_frequentes}')
print(f'O item mais frequente em Conexão - Capacidades - Interface é: {conexao_interface_capacidades_mais_frequentes}')
print(f'O item mais frequente em Conexão - Limitadores - Contexto - Interface é: {conexao_interface_contexto_limitadores_mais_frequentes}')
print(f'O item mais frequente em Conexão - Capacidades - Contexto - Interface é: {conexao_interface_contexto_capacidades_mais_frequentes}')


# Montando a estrutura do diagnóstico =====================================================================================================================================================
# =========================================================================================================================================================================================
lista_diagnostico = {

    # =========================
    # TAGS (HABILIDADES)
    # =========================

    'leitura_cifras': {
        'descricao_capacidade': 'consegue entender cifras com clareza',
        'efeito_positivo': 'você reconhece rapidamente os acordes e consegue se orientar bem nas músicas',
        'descricao_limitacao': 'tem dificuldade em entender cifras e o que elas representam',
        'efeito_negativo': 'você pode acabar tocando acordes errados e depender muito mais da memória do que da leitura de cifras pra conseguir tocar acordes de uma música',
        'recomendacao': 'foque em associar o nome do acorde (ex: C, Dm, G7) com sua estrutura prática no instrumento'
    },

    'diagrama_braco': {
        'descricao_capacidade': 'consegue interpretar diagramas do braço com segurança',
        'efeito_positivo': 'você consegue aprender novos acordes e posições com mais facilidade e autonomia',
        'descricao_limitacao': 'tem dificuldade em entender diagramas do braço',
        'efeito_negativo': 'sua capacidade de aprender novos acordes e visualizar o braço da guitarra fica limitada',
        'recomendacao': 'foque em entender como os diagramas representam as cordas, casas e dedos no braço da guitarra'
    },

    'leitura_tablatura': {
        'descricao_capacidade': 'consegue ler tablaturas corretamente',
        'efeito_positivo': 'você consegue aprender músicas e trechos mais complexos como riffs e solos com mais precisão e autonomia',
        'descricao_limitacao': 'tem dificuldade em interpretar tablaturas',
        'efeito_negativo': 'tocar músicas com riffs e solos acaba sendo mais complicado, já que você precisa depender mais do ouvido',
        'recomendacao': 'foque em entender as relações entre linhas-cordas e números-casas da tablatura'
    },

    'fundamental_acorde': {
        'descricao_capacidade': 'consegue encontrar notas pelo braço da guitarra',
        'efeito_positivo': 'construir power chords, acordes tríades/tétrades com ou sem inversões por todo o braço fica muito mais fácil',
        'descricao_limitacao': 'tem dificuldade em encontrar notas pelo braço da guitarra',
        'efeito_negativo': 'você fica preso aos acordes mais básicos e acaba não conseguindo variar os acordes ao longo do braço',
        'recomendacao': 'foque em memorizar as notas por todo o braço da guitarra, principalmente nas cordas 6 e 5'
    },

    'qualidade_acorde': {
        'descricao_capacidade': 'consegue diferenciar os tipos de acordes (maior, menor, com sétima, etc) através de cifras, diagramas e tablaturas',
        'efeito_positivo': 'seus acordes fazem sentido musicalmente e você já tem um dos pilares para tirar músicas por conta própria',
        'descricao_limitacao': 'tem dificuldade em identificar ou diferenciar a qualidade dos acordes (maior, menor, com sétima, etc)',
        'efeito_negativo': 'você pode tocar acordes diferentes dos que estão escritos nas cifras, o que pode soar bem estranho',
        'recomendacao': 'foque em entender a diferença entre acorde maior, menor, com sétima, etc'
    },

    'intervalos': {
        'descricao_capacidade': 'consegue entender e identificar intervalos e extensões dos acordes',
        'efeito_positivo': 'você é capaz de ler e entender acordes mais complexos e consegue interpretá-los corretamente',
        'descricao_limitacao': 'tem dificuldade em entender intervalos e extensões',
        'efeito_negativo': 'acordes mais avançados se tornam confusos e você acaba ficando muito preso às cifras, sem entender o que toca',
        'recomendacao': 'foque em entender como as extensões (9, 11, 13) são construídas a partir do acorde base e como isso fica disposto pelo braço da guitarra'
    },

    'base': {
        'descricao_limitacao': 'não domina conceitos básicos do instrumento',
        'efeito_negativo': 'ler cifras, tablaturas e diagramas se torna mais difícil e evoluir acaba sendo muito difícil e demorado',
        'recomendacao': 'foque em aprender os fundamentos de leitura de cifras, diagramas e tablatura antes de avançar'
    },


    # =========================
    # CONTEXTOS
    # =========================

    'triades_simples': {
        'descricao_capacidade': 'consegue trabalhar bem com acordes básicos (maiores e menores)',
        'efeito_positivo': 'você é capaz de entender a maioria dos acordes mais simples sem muitos problemas',
        'descricao_limitacao': 'tem dificuldade com acordes básicos (maiores e menores)',
        'efeito_negativo': 'isso limita bastante o seu repertório e dificulta sua evolução',
        'recomendacao': 'foque em dominar tríades maiores e menores nas posições básicas e também em diferentes formatos pelo braço'
    },

    'tetrades_simples': {
        'descricao_capacidade': 'consegue entender e usar acordes com sétima',
        'efeito_positivo': 'você já começa a acessar um vocabulário harmônico mais rico',
        'descricao_limitacao': 'tem dificuldade com acordes com sétima (tétrades)',
        'efeito_negativo': 'isso limita sua compreensão de músicas mais completas harmonicamente',
        'recomendacao': 'foque em entender a construção e aplicação de acordes com sétima'
    },

    'power_chords': {
        'descricao_capacidade': 'consegue reconhecer e usar power chords no braço',
        'efeito_positivo': 'você consegue tocar bases simples e se movimentar com facilidade pelo braço',
        'descricao_limitacao': 'tem dificuldade em reconhecer e localizar power chords',
        'efeito_negativo': 'isso dificulta tocar bases simples e se localizar no braço',
        'recomendacao': 'foque em entender a estrutura dos power chords e sua movimentação no braço'
    },

    'inversoes': {
        'descricao_capacidade': 'consegue interpretar acordes com baixo invertido',
        'efeito_positivo': 'você entende melhor a função harmônica e o movimento do baixo',
        'descricao_limitacao': 'tem dificuldade em entender acordes com baixo invertido',
        'efeito_negativo': 'isso gera confusão na hora de interpretar cifras como C/E ou D/F#',
        'recomendacao': 'foque em entender que o acorde continua sendo o mesmo, mudando apenas o baixo'
    },

    'extensoes': {
        'descricao_capacidade': 'consegue interpretar acordes com extensões (9, 11, 13)',
        'efeito_positivo': 'você entende harmonias mais ricas e sofisticadas',
        'descricao_limitacao': 'tem dificuldade com acordes com extensões',
        'efeito_negativo': 'acordes mais complexos se tornam difíceis de entender',
        'recomendacao': 'foque em entender como esses acordes são construídos a partir das tétrades'
    },

    'shapes_caged_triades': {
        'descricao_capacidade': 'consegue reconhecer acordes em diferentes shapes do CAGED (tríades)',
        'efeito_positivo': 'você consegue se movimentar pelo braço mantendo o mesmo acorde',
        'descricao_limitacao': 'tem dificuldade em reconhecer acordes em diferentes shapes do CAGED',
        'efeito_negativo': 'você fica preso a poucas regiões do braço',
        'recomendacao': 'foque em conectar os shapes do CAGED para o mesmo acorde ao longo do braço'
    },

    'shapes_caged_tetrades': {
        'descricao_capacidade': 'consegue reconhecer tétrades nos shapes do CAGED',
        'efeito_positivo': 'você entende acordes completos ao longo de todo o braço',
        'descricao_limitacao': 'tem dificuldade em reconhecer tétrades nos shapes do CAGED',
        'efeito_negativo': 'isso limita sua compreensão de acordes mais completos no braço',
        'recomendacao': 'foque em estudar tétrades dentro do sistema CAGED'
    }
}
'''
lista_nivel = {
    'iniciante': [ # 3 opções para escolher uma usando random.choice
        'Você ainda está construindo os fundamentos do instrumento, e isso faz com que várias etapas da execução pareçam mais difíceis do que deveriam.',
        'Neste momento, seu foco precisa estar em consolidar a base, pois é ela que vai facilitar todo o resto do seu desenvolvimento.',
        'O seu momento pede mais atenção aos fundamentos, pois são eles que vão destravar sua evolução daqui pra frente.'
    ],
    'intermediario': [
        'Você já apresenta uma boa base no instrumento, mas ainda existem alguns pontos que quebram a fluidez da sua execução.',
        'Seu desenvolvimento já permite tocar com certa segurança, mas ainda há inconsistências que impactam o resultado final.',
        'Você já avançou além da base inicial, mas ainda precisa ajustar alguns pontos para alcançar mais consistência ao tocar.'
    ],
    'avancado': [
        'Você já apresenta um bom controle sobre os principais aspectos do instrumento, o que permite uma execução mais fluida e consistente.',
        'Seu nível atual já permite tocar com segurança e fluidez, mostrando um desenvolvimento sólido no instrumento.',
        'Você já construiu uma base consistente, e agora o foco está em refinar ainda mais a sua execução.'
    ]
}

# Criando diferentes perfis baseados nas combinações entre tags
perfis = {
    'perfil_equilibrado': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'},  # Diagnóstico: Desenvolvimento consistente, pronto para avançar - usando entre {} pois é um set, não depende de ordem
        'limitadores': set(),
        'descricao': 'Você já é um guitarrista bem equilibrado, capaz de tocar várias músicas com fluidez.'
    },
    'perfil_falso_avancado': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'}, # Consegue executar, mas sem entender 👉 Diagnóstico: Vai travar ao tentar evoluir
        'limitadores': {'base'},
        'descricao': 'Você consegue tocar músicas inteiras sem se perder, porém ainda tem lacunas nos conhecimentos de base e isso pode travar sua evolução logo mais.'
    },
    'perfil_ritmo_travado': {
        'capacidades': {'troca_de_acorde', 'montagem_de_acorde'}, # Toca bem os acordes, troca rápido, mas não encaixa na música
        'limitadores': {'ritmo'},
        'descricao': 'Você tem familiaridade com acordes e consegue trocar com rapidez, mas ainda não consegue acompanhar músicas pois falta base em ritmo.'
    },
    'perfil_quase_equilibrado_ritmo': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'}, # Toca bem os acordes, troca rápido, mas não encaixa na música
        'limitadores': {'ritmo'},
        'descricao': 'Você está quase tocando músicas de forma equilibrada e com fluidez. Porém ainda há pequenas dificuldades de ritmo em alguns momentos.'

    }
}
'''
# Lista de conectores de frases
conectores_cap = [
    'Você já ',
    'Você também ',
    'Além disso, você também ',
    'Também vale destacar que você ',
    'Outro ponto positivo é que você '
]

conectores_lim_original = [
    'Você ainda ',
    'Por outro lado, você ainda ',
    'Além disso, você ',
    'Também vale destacar que você ',
    'Importante ressaltar que você ainda '
]

conectores_causa_efeito = [
    '. Por conta disso, ',
    '. Como consequência disso, ',
    '. Acaba que por conta disso ',
]



# # Lista das principais tags. As outras são adicionais e entram como considerações adicionais
# limitadores_principais = ['base', 'troca_de_acorde', 'ritmo', 'montagem_de_acorde']
# capacidades_principais = ['troca_de_acorde', 'ritmo', 'montagem_de_acorde']


'''
# Definindo se iniciante, intermediário ou avançado baseado na diferença da quantidade de tags entre limitadores e capacidades
# Ainda fazer isso, mas agora ver se rola pelo número do nivel_real
nivel = ''
if (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) >= 2:
        nivel = 'iniciante'
elif abs(len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= 1:
        nivel = 'intermediario'
elif (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= -2:
        nivel = 'avancado'
'''

# Diagnóstico final
print()
print('=' * 100)
print(f'{"DIAGNÓSTICO FINAL":^100}')
print('=' * 100)
print()


# indicadores que irão alterar os inícios e conectores de frases
conectores_cap_contador = 0                              # Retirei os contadores pois agora irei utilizar itertools
# conectores_lim_contador = 0
iter_cap = chain(conectores_cap, repeat(conectores_cap[-1]))
alterar_lista = True

# alterando a lista de prefixos da lista conectores_lim após ter passado todas as capacidades
if alterar_lista:
    conectores_lim = conectores_lim_original.copy()
    if conectores_cap_contador == 0:  # Consegui simplificar bastante o uso dos conectores limitadores apenas tirando o conector certo dependendo se já foram mostradas capacidades ou não
        conectores_lim.pop(1)
    else:
        conectores_lim.pop(0)
    iter_lim = chain(conectores_lim, repeat(conectores_lim[-1]))
    alterar_lista = False


'''===============================================================
    REGRAS E ORDEM PARA SEGUIR A ANÁLISE
    
1 - BASE - SE A TAG DOMINA NEM PRECISA DO RESTO
    - Checar se tag 'base' domina dentro da lista de limitadores
2 - INTERFACE - VERIFICAR QUANTIDADE DE ERROS E ACERTOS NELA
    - Checar na lista interfaces a contagem de erros e acertos de cada interface (não somente do mais frequente). 
    - Comparar a habilidade/limitações entre interfaces.
        SE TIVER PARELHO ERROS E ACERTOS NA INTERFACE - possivelmente NÃO É PROBLEMA DE INTERFACE
        Se erra muito mais do que acerta - possível problema de interface
    - Após isso, checar pra cada interface, quais tags temos em cada uma delas através da lista tags+interface. Ignorar contextos nesse ponto?
    - gerar um diagnóstico parcial de interface
    - TIPO DE TAG DENTRO DA INTERFACE 
        - MUITAS TAGS NA MESMA INTERFACE - possível PROBLEMA DE INTERFACE
        - MESMA TAG NA MESMA OU DIFERENTES INTERFACES - possível PROBLEMA DE TAG
3 - TAG DOMINA EM VÁRIOS CONTEXTOS E INTERFACES - possível PROBLEMA DE TAG 
    - Checar na lista de tags a contagem de erros e acertos
        Se tem muito erro e pouco acerto - possível problema de tag
        Se tá parelho - possível problema de interface ou contexto
    - Checar na lista de tags mais frequentes (talvez pegar as 2 tags mais frequentes) quais os contextos e interfaces presentes, através da lista tags+contexto e tags+interface.
        Gerar um diagnóstico parcial de tags+interface e cruzar com diagnóstico parcial de interface. Gerar um diagnóstico parcial de tags+contexto
    - MUITAS TAGS IGUAIS OU DIFERENTES NO MESMO CONTEXTO - possível PROBLEMA DE CONTEXTO
4 - CONTEXTO - VER QUAL CONTEXTO MAIS FREQUENTE - QUAIS TAGS PRESENTES NELE
    - Checar na lista contexto a contagem de erros e acertos de cada contexto (não somente do mais frequente)
        Se tem muito erro e pouco acerto - possível problema de contexto
        Se fica parelho - Não é problema de contexto
    - Checar na lista de contexto mais frequente e ver quais tags tem junto com ele cruzando com tags+contexto. Gerar um diagnóstico parcial de contexto e cruzar com diagnóstico parcial de tags+contexto.
    - CONTEXTO COM MUITAS TAGS - possível PROBLEMA CONTEXTO
    - CONTEXTO COM TAGS REPETIDAS - possível PROBLEMA TAG
5 - OS DIAGNÓSTICOS PARCIAIS FAZEM SENTIDO?
    - cruzar resultados com a lista tags+contexto+interface
    - Criação de diagnóstico geral
'''




#
# 1 - BASE - SE A TAG DOMINA NEM PRECISA DO RESTO
#     - Checar se tag 'base' domina dentro da lista de limitadores - Primeiro Filtro - Se tem problema de base, ignora todo o resto
if 'base' in limitadores_mais_frequentes:
    print(next(iter_lim), end='')
    print(f'{lista_diagnostico["base"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["base"]["efeito_negativo"]}.')
    # exit()



'''
2 - INTERFACE - VERIFICAR QUANTIDADE DE ERROS E ACERTOS NELA
    - Checar na lista interfaces a contagem de erros e acertos de cada interface (não somente do mais frequente). 
    - Comparar a habilidade/limitações entre interfaces.
        SE TIVER PARELHO ERROS E ACERTOS NA INTERFACE - possivelmente NÃO É PROBLEMA DE INTERFACE
        Se erra muito mais do que acerta - possível problema de interface
    - Após isso, checar pra cada interface, quais tags temos em cada uma delas através da lista tags+interface. Ignorar contextos nesse ponto?
    - gerar um diagnóstico parcial de interface
    - TIPO DE TAG DENTRO DA INTERFACE 
        - MUITAS TAGS NA MESMA INTERFACE - possível PROBLEMA DE INTERFACE
        - MESMA TAG NA MESMA OU DIFERENTES INTERFACES - possível PROBLEMA DE TAG
'''


# REGRA 2 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2 - INTERFACE - VERIFICAR QUANTIDADE DE ERROS E ACERTOS NELA
#     - Checar na lista interfaces a contagem de erros e acertos de cada interface (não somente do mais frequente).
#     - Comparar a habilidade/limitações entre interfaces.
#         SE TIVER PARELHO ERROS E ACERTOS NA INTERFACE - possivelmente NÃO É PROBLEMA DE INTERFACE
#         Se erra muito mais do que acerta - possível problema de interface
#     - Após isso, checar pra cada interface, quais tags temos em cada uma delas através da lista tags+interface. Ignorar contextos nesse ponto?
#     - gerar um diagnóstico parcial de interface
#     - TIPO DE TAG DENTRO DA INTERFACE
#         - MUITAS TAGS NA MESMA INTERFACE - possível PROBLEMA DE INTERFACE
#         - MESMA TAG NA MESMA OU DIFERENTES INTERFACES - possível PROBLEMA DE TAG

#     - Checar na lista interfaces a contagem de erros e acertos de cada interface (não somente do mais frequente).

possivel_interface_limitador = []
possivel_interface_capacidade = []

for interface, quantidade in contador_interface_limitadores.items():
    print(interface)
    print(quantidade)
    cap = contador_interface_capacidades.get(interface, 0)
    print(cap)
    diferenca = quantidade - cap
    print(diferenca)
    if diferenca >= 3:
        possivel_interface_limitador.append(interface)
        print(f'Possível interface limitador {possivel_interface_limitador}')
    elif diferenca <= -3:
        possivel_interface_capacidade.append(interface)
        print(f'Possível interface capacidade {possivel_interface_capacidade}')
    else:
        print('Regra 2 - interface - inconclusivo')

print(f'\nComparação possível interface limitador com limitadores mais frequentes')
print(possivel_interface_limitador)
print(interface_limitadores_mais_frequentes)

for interface in conexao_interface_limitadores:
    print(interface)

# checar pra cada possível interface limitadora, quais tags temos em cada uma delas através da lista tags+interface
tags_interface_limitador = {}
for tag, interface in conexao_interface_limitadores:
    print(tag)
    if interface in possivel_interface_limitador:
        if interface not in tags_interface_limitador:
            tags_interface_limitador[interface] = []
        tags_interface_limitador[interface].append(tag)
print(f'Interface x variedade Tags: {tags_interface_limitador}')

resultado_parcial_interface = {}
# Checar a diversidade/dominância de tag dentro da lista de tags para cada possível interface limitadora
for interface, tags in tags_interface_limitador.items():
    print(f'\n\nPossível Interface limitadora {interface}')
    # Conta quantas tags tem na lista de possíveis interfaces limitadoras
    contador = Counter(tags)
    # Pega a tag mais frequente
    tag_mais_comum, freq = contador.most_common(1)[0]
    total = len(tags)
    print(contador)
    print(tag_mais_comum)
    print(freq)
    # Calcula a frequência da tag em porcentagem
    dominancia = freq / total
    # Quantidade de tags diferentes dentro de uma mesma interface limitadora
    diversidade = len(contador)
    print(dominancia)
    if diversidade >=3:
        # Trocar depois por True/False para o diagnóstico final
        resultado_parcial_interface[interface] = True
        # resultado_parcial_interface[interface] = f'Muitas TAGS em uma mesma interface: Possível problema de interface - {interface} '
        print(f'Muitas TAGS em uma mesma interface: Possível problema de interface - {interface} ')
    elif dominancia >= 0.7:
        resultado_parcial_interface[interface] = False
        # resultado_parcial_interface[interface] = f'Predominância de uma mesma tag na mesma interface: Não é problema de interface - Talvez seja tag - {tag_mais_comum}'
        print(f'Predominância de uma mesma tag na mesma interface: Não é problema de interface - Talvez seja tag - {tag_mais_comum}')
    else:
        resultado_parcial_interface[interface] = 'Inconclusivo'
        print('Inconclusivo')

# Diagnóstico parcial interface
print()
for interface, resultado in resultado_parcial_interface.items():
    print(f'Possível problema de {interface}: {resultado}')

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3 - TAG DOMINA EM VÁRIOS CONTEXTOS E INTERFACES - possível PROBLEMA DE TAG 
    - Checar na lista de tags a contagem de erros e acertos
        Se tem muito erro e pouco acerto - possível problema de tag
        Se tá parelho - possível problema de interface ou contexto
    - Checar na lista de tags mais frequentes (talvez pegar as 2 tags mais frequentes) quais os contextos e interfaces presentes, através da lista tags+contexto e tags+interface.
        Gerar um diagnóstico parcial de tags+interface e cruzar com diagnóstico parcial de interface. Gerar um diagnóstico parcial de tags+contexto
    - MUITAS TAGS IGUAIS OU DIFERENTES NO MESMO CONTEXTO - possível PROBLEMA DE CONTEXTO
'''

possivel_tag_limitador = []
possivel_tag_capacidade = []




print()
#     - Checar na lista de tags a contagem de erros e acertos de cada TAG (não somente do mais frequente).
for tags, quantidade in contador_limitadores.items():
    print(tags)
    print(quantidade)
    cap = contador_capacidades.get(tags, 0)
    print(cap)
    diferenca = quantidade - cap
    print(diferenca)
    if diferenca >= 2:
        possivel_tag_limitador.append(tags)
        print(f'Possível Tag limitador {possivel_tag_limitador}')
    elif diferenca <= -2:
        possivel_tag_capacidade.append(tags)
        print(f'Possível Tag capacidade {possivel_tag_capacidade}')
    else:
        print('Regra 3 - Tag - inconclusivo')
print(f'\nComparação possível tag limitador com limitadores mais frequentes')
print(possivel_tag_limitador)
print(limitadores_mais_frequentes)




# checar pra cada possível tag limitadora, quais interfaces/contextos temos em cada uma delas através da lista tags+interface e tags+contexto
print('\nConexão Interface Limitadores')
for interface in conexao_interface_limitadores:
    print(interface)

print('\nConexão Contexto Limitadores')
for interface in conexao_contexto_limitadores:
    print(interface)

print()
tags_limitador_interface = {}
tags_limitador_contexto = {}

for tag, interface in conexao_interface_limitadores:
    print(tag)
    if tag in possivel_tag_limitador:
        if tag not in tags_limitador_interface:
            tags_limitador_interface[tag] = []
        tags_limitador_interface[tag].append(interface)
print(f'Tag x variedade Interfaces: {tags_limitador_interface}')

for tag, contexto in conexao_contexto_limitadores:
    print(tag)
    if tag in possivel_tag_limitador:
        if tag not in tags_limitador_contexto:
            tags_limitador_contexto[tag] = []
        tags_limitador_contexto[tag].append(contexto)
print(f'Tag x variedade Contextos: {tags_limitador_contexto}')


print()
resultado_parcial_tag_interface = {}
resultado_parcial_tag_contexto = {}

# Checar a diversidade/dominância de interface dentro da lista de interfaces para cada possível tag limitadora
for tags, interface in tags_limitador_interface.items():
    print(f'\n\nPossível Tag limitadora {tags}')
    # Conta quantas interfaces tem na lista de possíveis tags limitadoras
    contador = Counter(interface)
    # Pega a interface mais frequente
    interface_mais_comum, freq = contador.most_common(1)[0]
    total = len(interface)
    print(contador)
    print(interface_mais_comum)
    print(freq)
    # Calcula a frequência da tag em porcentagem
    dominancia = freq / total
    # Quantidade de tags diferentes dentro de uma mesma interface limitadora
    diversidade = len(contador)
    print(dominancia)
    if diversidade >=3:
        # Trocar depois por True/False para o diagnóstico final
        resultado_parcial_tag_interface[tags] = True
        # resultado_parcial_interface[interface] = f'Muitas INTERFACES em uma mesma TAG: Possível problema de interface - {interface} '
        print(f'Muitas INTERFACES em uma mesma TAG: Possível problema de TAG - {tags} ')
    elif dominancia >= 0.7:
        resultado_parcial_tag_interface[tags] = False
        # resultado_parcial_interface[interface] = f'Predominância de uma mesma tag na mesma interface: Não é problema de interface - Talvez seja tag - {contexto_mais_comum}'
        print(f'Predominância de uma mesma interface na mesma tag: Não é problema de tag - Talvez seja interface - {interface_mais_comum}')
    else:
        resultado_parcial_tag_interface[tags] = 'Inconclusivo'
        print('Inconclusivo')

# Checar a diversidade/dominância de contexto dentro da lista de contextos para cada possível tag limitadora
for tags, contexto in tags_limitador_contexto.items():
    print(f'\n\nPossível Tag limitadora {tags}')
    # Conta quantas interfaces tem na lista de possíveis tags limitadoras
    contador = Counter(contexto)
    # Pega a interface mais frequente
    contexto_mais_comum, freq = contador.most_common(1)[0]
    total = len(contexto)
    print(contador)
    print(contexto_mais_comum)
    print(freq)
    # Calcula a frequência da tag em porcentagem
    dominancia = freq / total
    # Quantidade de tags diferentes dentro de uma mesma interface limitadora
    diversidade = len(contador)
    print(dominancia)
    if diversidade >=3:
        # Trocar depois por True/False para o diagnóstico final
        resultado_parcial_tag_contexto[tags] = True
        # resultado_parcial_interface[interface] = f'Muitos CONTEXTOS em uma mesma TAG: Possível problema de contexto - {interface} '
        print(f'Muitos CONTEXTOS em uma mesma TAG: Possível problema de TAG - {tags} ')
    elif dominancia >= 0.7:
        resultado_parcial_tag_contexto[tags] = False
        # resultado_parcial_interface[interface] = f'Predominância de uma mesma tag na mesma interface: Não é problema de contexto - Talvez seja tag - {contexto_mais_comum}'
        print(f'Predominância de uma mesma interface na mesma tag: Não é problema de tag - Talvez seja contexto - {contexto_mais_comum}')
    else:
        resultado_parcial_tag_contexto[tags] = 'Inconclusivo'
        print('Inconclusivo')



# Diagnóstico parcial tag x interface
print()
for tag, resultado in resultado_parcial_tag_interface.items():
    print(f'Possível problema de {tag}: {resultado}')

# Diagnóstico parcial tag x contexto
print()
for tag, resultado in resultado_parcial_tag_contexto.items():
    print(f'Possível problema de {tag}: {resultado}')


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4 - CONTEXTO - VER QUAL CONTEXTO MAIS FREQUENTE - QUAIS TAGS PRESENTES NELE
    - Checar na lista contexto a contagem de erros e acertos de cada contexto (não somente do mais frequente)
        Se tem muito erro e pouco acerto - possível problema de contexto
        Se fica parelho - Não é problema de contexto
    - Checar na lista de contexto mais frequente e ver quais tags tem junto com ele cruzando com tags+contexto. Gerar um diagnóstico parcial de contexto e cruzar com diagnóstico parcial de tags+contexto.
    - CONTEXTO COM MUITAS TAGS - possível PROBLEMA CONTEXTO
    - CONTEXTO COM TAGS REPETIDAS - possível PROBLEMA TAG
'''
possivel_contexto_limitador = []
possivel_contexto_capacidade = []

for contexto, quantidade in contador_contexto_limitadores.items():
    print(contexto)
    print(quantidade)
    cap = contador_contexto_capacidades.get(contexto, 0)
    print(cap)
    diferenca = quantidade - cap
    print(diferenca)
    if diferenca >= 2:
        possivel_contexto_limitador.append(contexto)
        print(f'Possível contexto limitador {possivel_contexto_limitador}')
    elif diferenca <= -2:
        possivel_contexto_capacidade.append(contexto)
        print(f'Possível contexto capacidade {possivel_contexto_capacidade}')
    else:
        print('Regra 4 - contexto - inconclusivo')

print(f'\nComparação possível contexto limitador com limitadores mais frequentes')
print(possivel_contexto_limitador)
print(contexto_limitadores_mais_frequentes)

for contexto in conexao_contexto_limitadores:
    print(contexto)

# checar pra cada possível interface limitadora, quais tags temos em cada uma delas através da lista tags+interface
tags_contexto_limitador = {}
for tag, contexto in conexao_contexto_limitadores:
    print(tag)
    if contexto in possivel_contexto_limitador:
        if contexto not in tags_contexto_limitador:
            tags_contexto_limitador[contexto] = []
        tags_contexto_limitador[contexto].append(tag)
print(f'Contexto x variedade Tags: {tags_contexto_limitador}')

resultado_parcial_contexto = {}
# Checar a diversidade/dominância de tag dentro da lista de tags para cada possível interface limitadora
for contexto, tags in tags_contexto_limitador.items():
    print(f'\n\nPossível Contexto limitador {contexto}')
    # Conta quantas tags tem na lista de possíveis interfaces limitadoras
    contador = Counter(tags)
    # Pega a tag mais frequente
    tag_mais_comum, freq = contador.most_common(1)[0]
    total = len(tags)
    print(contador)
    print(tag_mais_comum)
    print(freq)
    # Calcula a frequência da tag em porcentagem
    dominancia = freq / total
    # Quantidade de tags diferentes dentro de uma mesma interface limitadora
    diversidade = len(contador)
    print(dominancia)
    if diversidade >=3:
        # Trocar depois por True/False para o diagnóstico final
        resultado_parcial_contexto[contexto] = True
        # resultado_parcial_interface[interface] = f'Muitas TAGS em uma mesma interface: Possível problema de interface - {interface} '
        print(f'Muitas TAGS em um mesmo contexto: Possível problema de contexto - {contexto} ')
    elif dominancia >= 0.7:
        resultado_parcial_contexto[contexto] = False
        # resultado_parcial_interface[interface] = f'Predominância de uma mesma tag na mesma interface: Não é problema de interface - Talvez seja tag - {tag_mais_comum}'
        print(f'Predominância de uma mesma tag no mesmo contexto: Não é problema de contexto - Talvez seja tag - {tag_mais_comum}')
    else:
        resultado_parcial_contexto[contexto] = 'Inconclusivo'
        print('Inconclusivo')

# Diagnóstico parcial contexto
print()
print('Diagnóstico parcial CONTEXTO')
for contexto, resultado in resultado_parcial_contexto.items():
    print(f'{contexto}: Possível problema de contexto: {resultado}')


'''5 - OS DIAGNÓSTICOS PARCIAIS FAZEM SENTIDO?
    - cruzar resultados com a lista tags+contexto+interface
    - Criação de diagnóstico geral'''




print(f'Interface x variedade Tags: {tags_interface_limitador}')
print(f'Tag x variedade Interfaces: {tags_limitador_interface}')
print(f'Tag x variedade Contextos: {tags_limitador_contexto}')
print(f'Contexto x variedade Tags: {tags_contexto_limitador}')

# Diagnóstico parcial interface
print()
print('Diagnóstico parcial INTERFACE')
for interface, resultado in resultado_parcial_interface.items():
    print(f'{interface}: Possível problema de interface: {resultado}')


# Diagnóstico parcial tag x interface
print()
print('Diagnóstico parcial TAG x INTERFACE')
for tag, resultado in resultado_parcial_tag_interface.items():
    print(f'Possível problema de {tag}: {resultado}')

# Diagnóstico parcial tag x contexto
print()
print('Diagnóstico parcial TAG x CONTEXTO')
for tag, resultado in resultado_parcial_tag_contexto.items():
    print(f'Possível problema de {tag}: {resultado}')

# Diagnóstico parcial contexto
print()
print('Diagnóstico parcial CONTEXTO')
for contexto, resultado in resultado_parcial_contexto.items():
    print(f'{contexto}: Possível problema de contexto: {resultado}')



#
# # Terceiro filtro - Validar contexto - Contexto tem que aparecer em moda lim e moda contexto lim para ser considerado válido. Além disso deve aparecer mais em lim e pouco (ou nenhuma) em cap.
# # Talvez tirar contexto válido 1.
# contexto_valido_1 = [item for item in contexto_limitadores_mais_frequentes if any(item in conexao for conexao in conexao_contexto_limitadores_mais_frequentes)]
# contexto_valido_2 = []
# for item in contexto_limitadores_mais_frequentes:
#     # print(item)
#     lim = contador_contexto_limitadores.get(item, 0)
#     cap = contador_contexto_capacidades.get(item, 0)
#     diferenca = lim - cap
#     if diferenca >= 2:
#         contexto_valido_2.append(item)
#
# # Mostrando contexto
# if (contexto_valido_1 and contexto_valido_2) and (contexto_valido_1 == contexto_valido_2):
#     for item in contexto_valido_1:
#         # print(item)
#         print(next(iter_lim), end='')
#         print(f'{lista_diagnostico[item]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico[item]["efeito_negativo"]}.')
# # FAZER O MESMO PARA CAPACIDADES


'''
# Primeiro Filtro - Se tem problema de base, ignora todo o resto
# Diagnóstico baseado em perfis
perfil = ''
for tipo, descricao in perfis.items():
    if descricao['capacidades'] == set(capacidades_mais_frequentes) and descricao['limitadores'] == set(limitadores_mais_frequentes):
        perfil = tipo
        print('\n1 - PERFIS ----------------\n')
        print(descricao['descricao'])   # Exemplo: 'Você já é um guitarrista bem equilibrado, capaz de tocar várias músicas com fluidez.'


# Considerações adicionais
print('\n3 - CONSIDERAÇÕES ADICIONAIS PARTE 1------------------\n')
if 'resistencia' in lista_capacidades_respostas_usuario:
    print(next(iter_cap), end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_positivo"]}.')
    conectores_cap_contador += 1
if 'continuidade' in lista_capacidades_respostas_usuario:
    print(next(iter_cap), end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_positivo"]}.')
    conectores_cap_contador += 1




# Caso não se encaixe em nenhum perfil
print('\n2 - DIAGNÓSTICOS ISOLADOS -----------------------\n')
if perfil == '':
    for capacidade in capacidades_mais_frequentes:
        print(next(iter_cap), end='')
        print(f'{lista_diagnostico[capacidade]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico[capacidade]["efeito_positivo"]}.')
        conectores_cap_contador += 1
    # alterando a lista de prefixos da lista conectores_lim após ter passado todas as capacidades
    if alterar_lista:
        conectores_lim = conectores_lim_original.copy()
        if conectores_cap_contador == 0:  # Consegui simplificar bastante o uso dos conectores limitadores apenas tirando o conector certo dependendo se já foram mostradas capacidades ou não
            conectores_lim.pop(1)
        else:
            conectores_lim.pop(0)
        iter_lim = chain(conectores_lim, repeat(conectores_lim[-1]))
        alterar_lista = False
    #frase combinação e causa/efeito
    if 'montagem_de_acorde' in limitadores_mais_frequentes and 'troca_de_acorde' in limitadores_mais_frequentes:
        print(next(iter_lim), end='')
        print('está consolidando a montagem dos acordes, o que impacta diretamente na velocidade de troca. A dificuldade na troca vem da montagem dos acordes ainda não estar automática.')
    elif 'montagem_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(next(iter_lim), end='')
        print('tem dificuldade na montagem dos acordes e isso acaba interferindo no seu ritmo.')
    elif 'troca_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(next(iter_lim), end='')
        print('tem dificuldade tanto na troca de acordes quanto em manter o ritmo, o que faz você se perder facilmente nas músicas. Você perde o ritmo pois ainda tem dificuldades na troca de acordes.')
    else:
        for limitador in limitadores_mais_frequentes:
            print(next(iter_lim), end='')
            print(f'{lista_diagnostico[limitador]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico[limitador]["efeito_negativo"]}.')

# Se não passar pelo bloco 2 - diagnósticos isolados (perfil != '') trocamos os prefixos da lista conectores_lim aqui
if alterar_lista:
    conectores_lim = conectores_lim_original.copy()
    if conectores_cap_contador == 0:  # Consegui simplificar bastante o uso dos conectores limitadores apenas tirando o conector certo dependendo se já foram mostradas capacidades ou não
        conectores_lim.pop(1)
    else:
        conectores_lim.pop(0)
    iter_lim = chain(conectores_lim, repeat(conectores_lim[-1]))
    alterar_lista = False

# Considerações adicionais
print('\n3 - CONSIDERAÇÕES ADICIONAIS PARTE 2------------------\n')
if 'resistencia' in lista_limitadores_respostas_usuario:
    print(next(iter_lim), end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_negativo"]}.')
if 'nao_consegue_pestana' in lista_limitadores_respostas_usuario:
    print(next(iter_lim), end='')
    print(f'{lista_diagnostico["nao_consegue_pestana"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["nao_consegue_pestana"]["efeito_negativo"]}.')
if 'continuidade' in lista_limitadores_respostas_usuario:
    print(next(iter_lim), end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_negativo"]}.')




# Diagnóstico do nível
print('\n4 - NÍVEL ------------\n')
print('Considerando seus pontos fortes e limitações, você se encontra no seguinte estágio:')
print(choice(lista_nivel[nivel]))




'''
