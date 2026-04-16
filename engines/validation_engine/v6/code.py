# Version 6 - Frequency-Based Diagnostic Engine

# Introduces:
# - Refined tagging system with more precise musical distinctions
# - Frequency analysis using Counter for tags, contexts, and tag–context relationships
# - Identification of dominant signals (capabilities and limitations)
# - Support for multiple dominant elements (ties)
# - Context analysis (where each skill or limitation appears)
# - Mapping between tags and their musical contexts

# Only elements with frequency >= 2 are considered relevant
# to filter out isolated or non-recurring signals and highlight consistent patterns

# This version transforms collected response data into structured diagnostic signals,
# identifying consistent patterns in user performance

from random import shuffle
from collections import Counter


lista_perguntas = [
    {'id': '2-1',
    'nível': 2,
    'numero_pergunta': 1,
    'pergunta': 'Numa música temos os seguintes acordes: G e Bm. Que acordes são esses? ',       
    'contexto': ['triades_simples'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'Sol Maior e Si Menor'},
                     {'correção': False, 'tag': [['capacidade', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'Sol Menor e Si Maior'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Dó Maior e Si Menor'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Lá Maior e Mi Maior'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Dó Maior e Ré Menor'},
                     {'correção': False, 'tag': [['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}           
                     ]
    },
    {'id': '2-2',
    'nível': 2,
    'numero_pergunta': 2,
    'pergunta': '(Figura do Braço - Am D) Quais cifras correspondem a esses acordes? ',          
    'contexto': ['triades_simples', 'diagrama_braco'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'Am, D'}, 
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'A, Dm'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'A, D'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Lá Menor e Ré Maior'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Consigo ler as figuras, mas não sei quais os acordes', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-3',
     'nível': 2,
     'numero_pergunta': 3,
     'pergunta': 'Qual das opções representa um Power Chord B5? (DIAGRAMA BRAÇO NAS RESPOSTAS)',   
     'contexto': ['power_chords', 'diagrama_braco'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'fundamental_acorde']], 'texto': 'B5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_cifras']], 'texto': 'Bb5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_cifras']], 'texto': 'C5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_cifras']], 'texto': 'G5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'leitura_cifras']], 'texto': 'F#5'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras mas não sei qual é o acorde', 'tipo': 'nao_sei'}
                     ]
     },
    {'id': '2-4',
    'nível': 2,
    'numero_pergunta': 4,
    'pergunta': '(Tablatura com notas na corda 6) Você toca isso em qual corda? (TABLATURA)',      
    'contexto': ['leitura_tablatura'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_tablatura']], 'texto': 'Na mais grossa'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura']], 'texto': 'Na mais fina'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura']], 'texto': 'Em alguma corda do meio'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-5',
    'nível': 2,
    'numero_pergunta': 5,
    'pergunta': 'Qual das opções representa um Dó Maior e um Ré Menor? (GRAFIA CIFRAS)',   
    'contexto': ['triades_simples'],
    'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'C, Dm'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'C, D'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'G, Dm'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'B, Fm'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'E, Am'},
                     {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                     ]
    },
    {'id': '2-6',
     'nível': 2,
     'numero_pergunta': 6,
     'pergunta': '(Figura do Braço - dois acordes - menor maior) Esses acordes são, respectivamente: (DIAGRAMA BRAÇO)',  
     'contexto': ['triades_simples', 'diagrama_braco'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde']], 'texto': 'Menor, Maior'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Menor, Menor'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Maior, Maior'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Maior, Menor'},
                     {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler a figura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                     ]
     },
    {'id': '2-7',
     'nível': 2,
     'numero_pergunta': 7,
     'pergunta': 'Qual das opções temos um acorde Menor? (DIAGRAMA  BRAÇO NAS RESPOSTAS)',  
     'contexto': ['triades_simples', 'diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde']], 'texto': 'Diagrama do braço - Am'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Diagrama do braço - E'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Diagrama do braço - D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Diagrama do braço - C'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Diagrama do braço - G'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler essas figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '2-8',
     'nível': 2,
     'numero_pergunta': 8,
     'pergunta': '(Tablatura do acorde F5) Que Power Chord é esse? (TABLATURA)',   
     'contexto': ['power_chords', 'leitura_tablatura'],
     'alternativas': [
                     {'correção': True, 'tag': [['capacidade', 'leitura_tablatura'], ['capacidade', 'fundamental_acorde']], 'texto': 'F5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'E5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'G5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'C5'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'A5'},
                     {'correção': False, 'tag': [['limitador', 'leitura_tablatura'], ['limitador', 'base']], 'texto': 'Não sei ler tablatura', 'tipo': 'nao_sei'},
                     {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler a tablatura mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                    ]
     },
    {'id': '3-1',
     'nível': 3,
     'numero_pergunta': 1,
     'pergunta': 'Quais cifras correspondem aos acordes Si Bemol Menor e Fá Sustenido Maior? (GRAFIA CIFRAS)',  
     'contexto': ['triades_simples'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'Bbm, F#'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Bb, F#m'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'Bbm, G#'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Bb, G#m'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-2',
     'nível': 3,
     'numero_pergunta': 2,
     'pergunta': '(Figura do Braço - C7M, Dm7 - shapes simples) Quais cifras correspondem a esses acordes? (DIAGRAMA BRAÇO)',   
     'contexto': ['tetrades_simples', 'diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'leitura_cifras']], 'texto': 'C7M, Dm7'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'C7M, Em7'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'C7, E7M'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Dó Maior com sétima maior, Ré menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Dó menor com sétima, Mi menor com sétima'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'], ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras, mas não sei quais os acordes', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras'], ['limitador', 'base']], 'texto': 'Consigo ler as figuras, sei os acordes, mas não sei as cifras', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '3-3',
     'nível': 3,
     'numero_pergunta': 3,
     'pergunta': 'Marque a opção que temos o mesmo acorde representado de maneiras diferentes (DIAGRAMA BRAÇO NAS RESPOSTAS)', 
     'contexto': ['triades_simples', 'diagrama_braco', 'leitura_tablatura'],
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
     'pergunta': 'Qual das opções representa um D7M? (TABLATURA)',   
     'contexto': ['tetrades_simples', 'leitura_tablatura'],
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
     'pergunta': '(Figura do Braço - G7, Am7) Esses diagramas representam acordes: (DIAGRAMA BRAÇO)', 
     'contexto': ['tetrades_simples', 'diagrama_braco'],
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
     'pergunta': 'Em qual opção temos os acordes F7M e Fm7? (TABLATURA)',  
     'contexto': ['leitura_tablatura', 'tetrades_simples'],
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
     'pergunta': 'O acorde Cm7 pode ser escrito como: (DIAGRAMA BRAÇO NAS RESPOSTAS)', 
     'contexto': ['tetrades_simples', 'diagrama_braco'],
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
     'numero_pergunta': 8,                   
     'pergunta': '(Tablatura G7M shape E) Partindo do acorde na tablatura - 1. Que acorde é esse? 2. Qual corda devemos mudar a nota para ter um acorde Maior com sétima? (TABLATURA)',
     'contexto': ['tetrades_simples', 'leitura_tablatura'],
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
     'numero_pergunta': 1,                     
     'pergunta': 'Você está tocando uma música junto com um baixista e de repente aparece na cifra o acorde D/C. Você toca qual acorde?',
     'contexto': ['inversoes'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'leitura_cifras']], 'texto': 'D'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'C'},
                      {'correção': False, 'tag': [['limitador', 'leitura_cifras']], 'texto': 'Não sei', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-2',
     'nível': 4,
     'numero_pergunta': 2,
     'pergunta': 'Quais outras opções para tocar esse mesmo acorde? (Figura do braço com C shape C)',  
     'contexto': ['shapes_caged_triades', 'diagrama_braco'],
     'alternativas': [{'correção': True, 'tag': [['capacidade', 'diagrama_braco'], ['capacidade', 'qualidade_acorde'], ['capacidade', 'fundamental_acorde']], 'texto': 'C shape A, C shape G, C shape D'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'C shape E, C shape D, B shape A'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde']], 'texto': 'C shape G, G shape E, D shape C'},
                      {'correção': False, 'tag': [['limitador', 'fundamental_acorde'], ['limitador', 'qualidade_acorde']], 'texto': 'A shape A, Cm shape E, F shape D'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde']], 'texto': 'Cm, shape A, Cm shape E, Cm shape D'},
                      {'correção': False, 'tag': [['limitador', 'diagrama_braco'],  ['limitador', 'base']], 'texto': 'Não sei ler as figuras', 'tipo': 'nao_sei'},
                      {'correção': False, 'tag': [['limitador', 'qualidade_acorde'], ['limitador', 'fundamental_acorde']], 'texto': 'Consigo ler as figuras mas não sei interpretar as alternativas', 'tipo': 'nao_sei'}
                      ]
     },
    {'id': '4-3',
     'nível': 4,
     'numero_pergunta': 3,
     'pergunta': '(Diagrama do braço - Lá maior com pestana e corda solta) Esses dois shapes representam quais acordes?',  
     'contexto': ['shapes_caged_triades', 'diagrama_braco'],
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
     'pergunta': '(Tab com bend, slide e hammer-on) Qual dessas opções descreve corretamente a execução dessa frase??',   
     'contexto': ['leitura_tablatura'],
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
     'pergunta': 'Na cifra aparece E/G#. O que isso significa? ',    
     'contexto': ['inversoes'],
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
     'pergunta': '(Diagrama braço - Ab shape G, F# shape C) Que acordes são esses?',  
     'contexto': ['shapes_caged_triades', 'diagrama_braco'],
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
     'pergunta': 'Qual das opções corresponde aos acordes Eb, Fm e Bm(b5)',  
     'contexto': ['shapes_caged_triades', 'diagrama_braco'],
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
     'pergunta': 'Qual dessas posições representa C/E e Dm/C?',    
     'contexto': ['inversoes', 'leitura_tablatura'],
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
     'pergunta': 'Você está tocando sozinho em casa e se depara com a cifra F/G. Qual acorde você toca?',  
     'contexto': ['inversoes', 'extensoes'],
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
     'pergunta': '(Figura do braço = F#7M(#11)) Este acorde possui:',      
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
     'pergunta': 'Qual opção corresponde ao acorde C7(9) e G7(13)?  (DIAGRAMA BRAÇO NAS RESPOSTAS)',  
     'contexto': ['extensoes', 'diagrama_braco'],
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
     'pergunta': '(Tablatura - acorde D meio diminuto shape C) Que acorde é esse?',   
     'contexto': ['shapes_caged_tetrades', 'leitura_tablatura'],
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
     'pergunta': '(Figura do braço - Am7(9)/C  x35200) Qual cifra corresponde a esse acorde?',    
     'contexto': ['inversoes', 'extensoes', 'diagrama_braco'],
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
     'pergunta': 'Qual desses acordes possui 9 maior e 13 maior?',  
     'contexto': ['extensoes', 'diagrama_braco'],
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
     'pergunta': 'Em qual opção temos apenas o acorde D7?',    
     'contexto': ['shapes_caged_tetrades', 'diagrama_braco'],
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
     'pergunta': '(tablatura E7M(#11) shape C) Qual cifra corresponde a esse acorde?',  
     'contexto': ['shapes_caged_tetrades', 'extensoes', 'leitura_tablatura'],
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
conexao_contexto_capacidades = []
conexao_contexto_limitadores = []

# Prevent level oscillation (avoid repeating levels already visited)
ja_subiu_nivel = False
ja_desceu_nivel = False

# Handle level-up transition
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

# Handle level-down transition
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

# Rule engine: defines progression logic based on accuracy thresholds
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



# Initial user self-assessment to define starting level
nivel_real = 0
autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
if autoavaliacao_nivel == 1:
    # Levels 1 and 2 share the same starting point (level 2)
    nivel = 2
else:
    nivel = autoavaliacao_nivel

# Maximum of 3 evaluation rounds
while rodada < 4:

    # Stop execution if both upward and downward transitions occurred
    if ja_subiu_nivel == True and ja_desceu_nivel == True:
        break

    print(f'{" INICIANDO NÍVEL " + str(nivel) + " ":=^50}')

    for questao in lista_perguntas:
        # Filter questions by current level and avoid repetition
        if questao['nível'] == nivel and questao['numero_pergunta'] > ultima_pergunta:
            print()
            print(f'Nível: {questao["nível"]}')
            print(questao['pergunta'])
            print()
            total_perguntas += 1
            perguntas_restantes -= 1
            ultima_pergunta = questao['numero_pergunta']

            # Separate normal answers from "I don't know" options
            alternativas_para_embaralhar = []
            alternativas_nao_sei = []

            for alternativa in questao['alternativas']:
                if alternativa.get('tipo') != 'nao_sei':
                    alternativas_para_embaralhar.append(alternativa)
                else:
                    alternativas_nao_sei.append(alternativa)

            shuffle(alternativas_para_embaralhar)          
            alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


            mapa_respostas = {}

            for numero, resposta in enumerate(alternativas_para_mostrar):
                letra = lista_alternativas[numero]
                mapa_respostas[letra] = resposta
                print(f'{letra} - {resposta["texto"]}')

            # Capture user response (UI will handle validation in final version)
            resposta_usuario = input('\nQual a resposta certa? ').strip().upper()

            if mapa_respostas[resposta_usuario]['correção']:
                print('Você ACERTOU')
                acertos += 1
                # Store tags and their associated contexts
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    lista_capacidades_respostas_usuario.append(tag)
                    # Map tag-to-context relationships
                    for contexto in questao['contexto']:
                        conexao_contexto_capacidades.append((tag, contexto))
                for contexto in questao['contexto']:
                    lista_contexto_capacidades.append(contexto)
            else:
                print('Você ERROU')
                erros += 1
                for tipo, tag in mapa_respostas[resposta_usuario]['tag']:
                    lista_limitadores_respostas_usuario.append(tag)
                    # Map tag-to-context relationships
                    for contexto in questao['contexto']:
                        conexao_contexto_limitadores.append((tag, contexto))
                for contexto in questao['contexto']:
                    lista_contexto_limitadores.append(contexto)

            ## Evaluate performance at round checkpoint
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

                # Apply rule engine to determine next action
                for condicao, acao in regras[rodada]:
                    if condicao(taxa_acertos):
                        nivel_anterior = nivel
                        nivel, rodada, perguntas_restantes, ja_subiu_nivel, ja_desceu_nivel = acao(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel)
                        if nivel != nivel_anterior:
                            # Reset counters when level changes
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

# -------------------- DIAGNOSTIC CONSTRUCTION --------------------
print(f'{" CONSTRUÇÃO DE DIAGNÓSTICO ":=^150}')
print(f'Taxa de acertos: {taxa_acertos:.1f}%')

print(f'Você acertou {acertos_final} respostas de um total de {total_perguntas_final} perguntas. Você acertou {taxa_acertos:.1f}%.')
print(f'Total erros: {erros_final}')

print('\n\nLISTAS DE TAGS E CONTEXTOS')

print(f'Lista de limitadores do usuário (TAGS): {lista_limitadores_respostas_usuario}')
print(f'Lista de capacidades do usuário (TAGS): {lista_capacidades_respostas_usuario}')

print(f'Lista de contextos limitadores (CONTEXTO): {lista_contexto_limitadores}')
print(f'Lista de contextos capacidades(CONTEXTO): {lista_contexto_capacidades}')

print(f'Lista de limitadores do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_limitadores}')
print(f'Lista de capacidades do usuário em contexto (TAGS + CONTEXTO): {conexao_contexto_capacidades}')


# Count frequency of tags, contexts, and tag-context relationships
contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)
contador_contexto_limitadores = Counter(lista_contexto_limitadores)
contador_contexto_capacidades = Counter(lista_contexto_capacidades)
contador_conexao_contexto_limitadores = Counter(conexao_contexto_limitadores)
contador_conexao_contexto_capacidades = Counter(conexao_contexto_capacidades)

print('\n\nCONTADORES')
print(f'Limitadores: {contador_limitadores}')
print(f'Capacidades: {contador_capacidades}')
print(f'Contexto Limitadores: {contador_contexto_limitadores}')
print(f'Contexto Capacidades: {contador_contexto_capacidades}')
print(f'Conexão Contexto Limitadores: {contador_conexao_contexto_limitadores}')
print(f'Conexão Contexto Capacidades: {contador_conexao_contexto_capacidades}')


# Identify highest frequency values for each category
maior_frequencia_limitadores = max(contador_limitadores.values(), default=0)
maior_frequencia_capacidades = max(contador_capacidades.values(), default=0)
maior_frequencia_contexto_limitadores = max(contador_contexto_limitadores.values(), default=0)
maior_frequencia_contexto_capacidades = max(contador_contexto_capacidades.values(), default=0)
maior_frequencia_conexao_contexto_limitadores = max(contador_conexao_contexto_limitadores.values(), default=0)
maior_frequencia_conexao_contexto_capacidades = max(contador_conexao_contexto_capacidades.values(), default=0)

print('\n\nMAIORES VALORES')
print(f'Limitadores: {maior_frequencia_limitadores}')
print(f'Capacidades: {maior_frequencia_capacidades}')
print(f'Contexto Limitadores: {maior_frequencia_contexto_limitadores}')
print(f'Contexto Capacidades: {maior_frequencia_contexto_capacidades}')
print(f'Conexão Contexto Limitadores: {maior_frequencia_conexao_contexto_limitadores}')
print(f'Conexão Contexto Capacidades: {maior_frequencia_conexao_contexto_capacidades}')


# Extract dominant elements (frequency >= 2 and equal to max)
limitadores_mais_frequentes = [item for item, quantidade in contador_limitadores.items() if (quantidade == maior_frequencia_limitadores and quantidade >= 2)]
capacidades_mais_frequentes = [item for item, quantidade in contador_capacidades.items() if (quantidade == maior_frequencia_capacidades and quantidade >= 2)]
contexto_limitadores_mais_frequentes = [item for item, quantidade in contador_contexto_limitadores.items() if (quantidade == maior_frequencia_contexto_limitadores and quantidade >= 2)]
contexto_capacidades_mais_frequentes = [item for item, quantidade in contador_contexto_capacidades.items() if (quantidade == maior_frequencia_contexto_capacidades and quantidade >= 2)]
conexao_contexto_limitadores_mais_frequentes = [item for item, quantidade in contador_conexao_contexto_limitadores.items() if (quantidade == maior_frequencia_conexao_contexto_limitadores and quantidade >= 2)]
conexao_contexto_capacidades_mais_frequentes = [item for item, quantidade in contador_conexao_contexto_capacidades.items() if (quantidade == maior_frequencia_conexao_contexto_capacidades and quantidade >= 2)]

print('\n\nITENS MAIS FREQUENTES')
print(f'O item mais frequente em Limitadores é: {limitadores_mais_frequentes}')
print(f'O item mais frequente em Capacidades é: {capacidades_mais_frequentes}')
print(f'O item mais frequente em Contexto - Limitadores é: {contexto_limitadores_mais_frequentes}')
print(f'O item mais frequente em Contexto - Capacidades é: {contexto_capacidades_mais_frequentes}')
print(f'O item mais frequente em Conexão - Contexto - Limitadores é: {conexao_contexto_limitadores_mais_frequentes}')
print(f'O item mais frequente em Conexão - Contexto - Capacidades é: {conexao_contexto_capacidades_mais_frequentes}')

