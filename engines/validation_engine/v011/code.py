'''====================================================================================================================================================================================================
Versão 11 - Adicionando lógica do teste de contexto para analisar score intermediário, trocando de contexto para cima ou para baixo
====================================================================================================================================================================================================
'''

from random import shuffle, choice
from collections import Counter
from itertools import chain, repeat



def lim(tag):
    return {'categoria': 'limitador', 'tag': tag}
def cap(tag):
    return {'categoria': 'capacidade', 'tag': tag}

lista_perguntas_teste_interface_completo = [
    {
        'id': '1-1',
        'nivel': 1,
        'numero_pergunta': 1,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-2',
        'nivel': 1,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_2?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-3',
        'nivel': 1,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_3?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-4',
        'nivel': 1,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_4?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-5',
        'nivel': 1,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_5?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},     
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-6',
        'nivel': 1,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_6?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-7',
        'nivel': 1,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_7?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
]

lista_perguntas_teste_interface_simplificado = [
    {
        'id': '1-1',
        'nivel': 1,
        'numero_pergunta': 1,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_cifras'],
        'pergunta': 'Simplificado Pergunta_1?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-2',
        'nivel': 1,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['diagrama_braco'],
        'pergunta': 'Simplificado Pergunta_2?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-3',
        'nivel': 1,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Simplificado Pergunta_3?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
]

lista_perguntas_teste_contexto = [
    {
        'id': '2-1',
        'nivel': 2,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['power_chords'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-2',
        'nivel': 2,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_2?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-3',
        'nivel': 2,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_3?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},     
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-4',
        'nivel': 2,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_4?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-5',
        'nivel': 2,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_5?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-6',
        'nivel': 2,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_6?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},      
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-7',
        'nivel': 2,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_7?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-8',
        'nivel': 2,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['power_chords'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_8?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},      
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-9',
        'nivel': 2,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['triades_simples'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_9?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-10',
        'nivel': 2,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-11',
        'nivel': 2,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-12',
        'nivel': 2,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            # 
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-13',
        'nivel': 2,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-14',
        'nivel': 2,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},     
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-15',
        'nivel': 2,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '2-16',
        'nivel': 2,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['triades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
{
        'id': '3-1',
        'nivel': 3,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['tetrades_simples'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-2',
        'nivel': 3,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-3',
        'nivel': 3,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-4',
        'nivel': 3,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-5',
        'nivel': 3,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-6',
        'nivel': 3,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-7',
        'nivel': 3,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},      
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '3-8',
        'nivel': 3,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['tetrades_simples'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
{
        'id': '4-1',
        'nivel': 4,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['shapes_caged_triades'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-2',
        'nivel': 4,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-3',
        'nivel': 4,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-4',
        'nivel': 4,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-5',
        'nivel': 4,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-6',
        'nivel': 4,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-7',
        'nivel': 4,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-8',
        'nivel': 4,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['shapes_caged_triades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},     
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
{
        'id': '4-9',
        'nivel': 4,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['inversoes'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-10',
        'nivel': 4,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},    
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-11',
        'nivel': 4,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},    
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-12',
        'nivel': 4,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-13',
        'nivel': 4,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-14',
        'nivel': 4,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-15',
        'nivel': 4,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '4-16',
        'nivel': 4,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['inversoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
{
        'id': '5-1',
        'nivel': 5,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-2',
        'nivel': 5,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-3',
        'nivel': 5,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-4',
        'nivel': 5,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-5',
        'nivel': 5,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-6',
        'nivel': 5,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-7',
        'nivel': 5,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-8',
        'nivel': 5,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['shapes_caged_tetrades'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},        
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
{
        'id': '5-9',
        'nivel': 5,
        'numero_pergunta': 1,
        'etapa': 'contexto',
        'contexto': ['extensoes'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-10',
        'nivel': 5,
        'numero_pergunta': 2,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_10?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},       
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-11',
        'nivel': 5,
        'numero_pergunta': 3,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_11?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},     
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-12',
        'nivel': 5,
        'numero_pergunta': 4,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_12?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},           
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-13',
        'nivel': 5,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['diagrama_braco'],
        'pergunta': 'Pergunta_13?', 
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},         
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-14',
        'nivel': 5,
        'numero_pergunta': 6,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_14?',
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-15',
        'nivel': 5,
        'numero_pergunta': 7,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_15?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '5-16',
        'nivel': 5,
        'numero_pergunta': 8,
        'etapa': 'interface',
        'contexto': ['extensoes'],
        'interface': ['leitura_tablatura'],
        'pergunta': 'Pergunta_16?',  
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},          
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Dó'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Ré'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Mi'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Fá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Lá'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Nota Si'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    }
]

# User self-assessment of level
def definir_nivel():
    autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
    if autoavaliacao_nivel == 1:
        # Level 1 is adjusted to level 2 to align with test entry point
        return 2
    else:
        return autoavaliacao_nivel


# Define whether to run complete or simplified interface test
def tipo_teste_interface(nivel):
    if nivel <= 3:
        return 'completo'
    else:
        return 'simplificado'

# Select question list based on test type
def lista_de_perguntas(tipo_teste):
    if tipo_teste == 'completo':
        return lista_perguntas_teste_interface_completo.copy()
    else:
        return lista_perguntas_teste_interface_simplificado.copy()

def mostrar_alternativas(pergunta, letras_alternativas):
        # Separate "nao_sei" option and shuffle remaining alternatives
        alternativas_para_embaralhar =[]
        alternativas_nao_sei = []
        for alternativa in pergunta['alternativas']:
            if alternativa.get('tipo') == 'nao_sei':
                alternativas_nao_sei.append(alternativa)
            else:
                alternativas_para_embaralhar.append(alternativa)
        shuffle(alternativas_para_embaralhar)
        alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei

        # Map displayed letters to alternatives for user input validation
        mapa_respostas = {}
        for numero, alternativa in enumerate(alternativas_para_mostrar):
            print(f'{letras_alternativas[numero]} - {alternativa['texto']}')
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa
        return mapa_respostas

# Execute interface test
def executar_teste_interface(lista_perguntas, tipo_teste,  nivel):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_interface = []
    erros_interface = []
    acertos = 0
    erros = 0
    for pergunta in lista_perguntas:
        print(f'Nível: {nivel} - Interface: {pergunta['interface']} - {pergunta['pergunta']}')

        #Agora sim, tirei a duplicação e direcionei para a função. Duplicação está como comentário logo abaixo
        mapa_respostas = mostrar_alternativas(pergunta, letras_alternativas)

        # # Embaralhar alternativas
        # alternativas_para_embaralhar =[]
        # alternativas_nao_sei = []
        # for alternativa in pergunta['alternativas']:
        #     if alternativa.get('tipo') == 'nao_sei':
        #         alternativas_nao_sei.append(alternativa)
        #     else:
        #         alternativas_para_embaralhar.append(alternativa)
        # # shuffle(alternativas_para_embaralhar)
        # alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei
        #
        #
        # mapa_respostas = {}
        # # Mostrar alternativas
        # for numero, alternativa in enumerate(alternativas_para_mostrar):
        #     print(f'{letras_alternativas[numero]} - {alternativa['texto']}')
        #     letra = letras_alternativas[numero]
        #     mapa_respostas[letra] = alternativa

        resposta_usuario = input('Resposta: ').strip().upper()

        # Extract tags from selected answer and store result
        tag = [tag['tag'] for tag in mapa_respostas[resposta_usuario]['tag']]
        guardar = {
            'interface': pergunta['interface'][0],
            'tag': tag
        }
        if mapa_respostas[resposta_usuario]['correcao']:
            print('Você acertou!')
            acertos += 1
            acertos_interface.append(guardar)
        else:
            print('Você errou')
            erros += 1
            # If user fails simplified test, switch to complete test
            erros_interface.append(guardar)
            if tipo_teste == 'simplificado':
                return 'erro no teste simplificado', acertos_interface, erros_interface
    return 'teste ok', acertos_interface, erros_interface


# Run interface test with fallback from simplified to complete
def rodar_teste_interface(nivel):
    tipo_teste = tipo_teste_interface(nivel)

    while True:
        lista_perguntas = lista_de_perguntas(tipo_teste)

        resultado, acertos_interface, erros_interface = executar_teste_interface(lista_perguntas, tipo_teste, nivel)

        if resultado == 'erro no teste simplificado':
            tipo_teste = 'completo'
            continue

        return acertos_interface, erros_interface

# Calculate interface reading ability based on errors
def calcular_score_teste_completo(erros_interface):
    cont_cifra = 0
    cont_diagrama = 0
    cont_tablatura = 0
    if len(erros_interface) == 0:
        sabe_ler_cifra = True
        sabe_ler_diagrama = True
        sabe_ler_tablatura = True
        return sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura
    else:
        for erro in erros_interface:
            if erro['interface'] == 'leitura_cifras':
                cont_cifra += 1
            if erro['interface'] == 'diagrama_braco':
                cont_diagrama += 1
            if erro['interface'] == 'leitura_tablatura':
                cont_tablatura += 1
    sabe_ler_cifra = True if cont_cifra == 0 else False
    sabe_ler_diagrama = True if cont_diagrama == 0 else False
    sabe_ler_tablatura = True if cont_tablatura == 0 else False
    return sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura


# Execute context-based test with adaptive question flow and tag collection
def executar_teste_contexto_unico(nivel, acertos_geral, erros_geral, contexto):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_por_contexto = []
    erros_por_contexto = []
    acertos = 0
    erros = 0
    perguntas_restantes = 4
    total_perguntas = 0
    rodada = 1
    lista_perguntas = lista_perguntas_teste_contexto

    for pergunta in lista_perguntas:
        if pergunta['contexto'][0] == contexto:
            print(f'Rodada: {rodada}')
            print(f'Nível: {nivel} - Contexto: {pergunta['contexto']} - {pergunta['pergunta']}')
            perguntas_restantes -= 1
            total_perguntas += 1
            mapa_respostas = mostrar_alternativas(pergunta, letras_alternativas)

            resposta_usuario = input('Resposta: ').strip().upper()

            # Extract tags and store result (context + interface + tag)
            tag = [tag['tag'] for tag in mapa_respostas[resposta_usuario]['tag']]
            guardar = {
                'interface': pergunta['interface'][0],
                'contexto': pergunta['contexto'][0],
                'tag': tag
            }
            if mapa_respostas[resposta_usuario]['correcao']:
                print('Você acertou!\n')
                acertos += 1
                acertos_geral.append(guardar)
                acertos_por_contexto.append(guardar)
            else:
                print('Você errou\n')
                erros += 1
                erros_geral.append(guardar)
                erros_por_contexto.append(guardar)
                
            # Trigger intermediate evaluation to decide next action (adaptive flow)
            if perguntas_restantes <= 0:
                print('CONFERIR SCORE INTERMEDIÁRIO')
                taxa_acertos = (acertos / total_perguntas) * 100
                print(f'Taxa de acertos: {taxa_acertos:.1f}%')

                # NOT USED YET (reserved for final result summary before reset)
                acertos_final = acertos
                erros_final = erros
                total_perguntas_final = total_perguntas

                nivel, rodada, perguntas_restantes = rodar_condicoes(taxa_acertos, rodada, nivel)
                if perguntas_restantes <= 0:
                    return acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto, taxa_acertos
                    break

# Execute rule set based on accuracy and current round
def rodar_condicoes(taxa_acertos, rodada, nivel):
    for condicao, acao in regras[rodada]:
        if condicao(taxa_acertos):
            nivel, rodada, perguntas_restantes = acao(nivel, rodada)
            return nivel, rodada, perguntas_restantes

# Função para trocar de contexto antecipadamente dependendo da pontuação
def altera_contexto(nivel, rodada):
    print('Alterando contexto...')
    print(f'Rodada: {rodada}\n')
    return nivel, rodada, 0

# Mais 2 perguntas no teste de contexto
def mais_2(nivel, rodada):
    print('Mais 2 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 2

# Mais 4 perguntas no teste de contexto
def mais_4(nivel, rodada):
    print('Mais 4 perguntas')
    print(f'Rodada: {rodada}\n')
    rodada += 1
    return nivel, rodada, 4

# Confirma o nível no teste de contexto
def confirma_nivel(nivel, rodada):
    print('Confirma nível')
    print(f'Rodada: {rodada}\n')
    rodada = 4
    return nivel, rodada, 0


# Executa o teste de contexto em todos os contextos de um único nível e salva as estatísticas
def executar_teste_contexto_em_nivel_unico(nivel, dicionario_contextos, estatisticas_por_contexto, acertos_geral, erros_geral):
    for contexto in dicionario_contextos[nivel]:
        (acertos_geral,
         erros_geral,
         acertos_por_contexto,
         erros_por_contexto,
         taxa_acertos) = executar_teste_contexto_unico(nivel,
                                                    acertos_geral,
                                                    erros_geral,
                                                    contexto)
        estatisticas['pontuação'] = taxa_acertos
        estatisticas['acertos'] = acertos_por_contexto
        estatisticas['erros'] = erros_por_contexto
        estatisticas_por_contexto[contexto] = estatisticas.copy()
    return estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto

# Função de subir nível
def subir_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Sobe de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    if nivel < 5:
        nivel += 1
        ja_subiu_nivel = True
    else:
        print('Nível máximo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada, ja_subiu_nivel, ja_desceu_nivel

# Função de descer nível
def descer_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel):
    print('Desce de nível')
    print(f'Rodada: {rodada}\n')
    rodada = 1
    if nivel > 2:
        nivel -= 1
        ja_desceu_nivel = True
    else:
        nivel -= 1
        print('Nível mínimo atingido')
        print('Confirma nível')
        rodada = 4
    return nivel, rodada, ja_subiu_nivel, ja_desceu_nivel

# Rule set for progression decisions based on accuracy and round
regras = {
    1: [
        (lambda t: t >= 80, altera_contexto),
        (lambda t: t > 50, mais_2),
        (lambda t: t > 35, mais_4),
        (lambda t: t > 0, mais_2),
        (lambda t: True, altera_contexto)
    ],
    2: [
        (lambda t: t >= 75, altera_contexto),
        (lambda t: t > 65, mais_2),
        (lambda t: t >= 35, confirma_nivel),
        (lambda t: True, altera_contexto)
    ],
    3: [
        (lambda t: t >= 75, altera_contexto),
        (lambda t: t >= 35, confirma_nivel),
        (lambda t: True, altera_contexto)
    ]
}

# Executar troca de nível dos testes
def executar_teste_contexto_com_troca_de_niveis(nivel, dicionario_contextos, ja_subiu_nivel, ja_desceu_nivel, estatisticas_por_contexto, acertos_geral, erros_geral, rodada):
    while rodada < 4:
        (estatisticas_por_contexto,
         acertos_geral,
         erros_geral,
         acertos_por_contexto,
         erros_por_contexto) = executar_teste_contexto_em_nivel_unico(nivel,
                                                                      dicionario_contextos,
                                                                      estatisticas_por_contexto,
                                                                      acertos_geral,
                                                                      erros_geral)

        # Análise para subir, descer ou confirmar nível
        pontuacao = []
        for contexto in dicionario_contextos[nivel]:
            pontuacao.append(estatisticas_por_contexto[contexto]['pontuação'])
        print(pontuacao)
        if min(pontuacao) >= 75:
            nivel, rodada, ja_subiu_nivel, ja_desceu_nivel = subir_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel)
            # Evitar voltar para níveis repetidos
            if ja_subiu_nivel and ja_desceu_nivel:
                break
            continue
        elif max(pontuacao) < 35:
            nivel, rodada, ja_subiu_nivel, ja_desceu_nivel = descer_nivel(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel)
            # Evitar voltar para níveis repetidos
            if ja_subiu_nivel and ja_desceu_nivel:
                break
            continue
        else:
            nivel, rodada, perguntas_restantes = confirma_nivel(nivel, rodada)
            break


    return estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto, nivel





# Flags to control level transition state
ja_subiu_nivel = False
ja_desceu_nivel = False

dicionario_contextos = {
    2: ['power_chords', 'triades_simples'],
    3: ['tetrades_simples'],
    4: ['shapes_caged_triades', 'inversoes'],
    5: ['shapes_caged_tetrades', 'extensoes']
}

rodada = 1

acertos_geral = []
erros_geral = []

estatisticas_por_contexto = {}
estatisticas = {}


def main(estatisticas_por_contexto, acertos_geral, erros_geral):
    # Autoavaliação de Nível
    nivel = definir_nivel()

# Run interface test with fallback from simplified to complete
    acertos_interface, erros_interface = rodar_teste_interface(nivel)

    print(acertos_interface)
    print(erros_interface)

    # Calculate interface reading ability based on errors
    sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura = calcular_score_teste_completo(erros_interface)

    # Display interface test results
    print(f'\nSabe ler cifra: {sabe_ler_cifra}\nSabe ler diagrama: {sabe_ler_diagrama}\nSabe ler tablatura: {sabe_ler_tablatura}')

    # Executa o teste de contexto completo, com trocas de contextos e trocas de níveis
    (estatisticas_por_contexto,
     acertos_geral,
     erros_geral,
     acertos_por_contexto,
     erros_por_contexto,
     nivel) = executar_teste_contexto_com_troca_de_niveis(nivel,
                                                          dicionario_contextos,
                                                          ja_subiu_nivel,
                                                          ja_desceu_nivel,
                                                          estatisticas_por_contexto,
                                                          acertos_geral,
                                                          erros_geral,
                                                          rodada)
    return estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto

def visualizar_resultados(estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto):
    # Visualização de resultados
    print(estatisticas_por_contexto)
    print(acertos_geral)
    print(erros_geral)


    # Convert structured results into simplified lists for display/debugging
    resumo_acertos = []
    resumo_erros = []

    for item in acertos_geral:
        guardar = [valor for chave, valor in item.items()]
        resumo_acertos.append(guardar)
    for item in erros_geral:
        guardar = [valor for chave, valor in item.items()]
        resumo_erros.append(guardar)

    print(resumo_acertos)

    print('\n\nAcertos Gerais')
    for item in resumo_acertos:
        print(item)

    # Extraindo lista de acertos - interface, contexto, tag - para ficar visualmente mais fácil de analisar - Com isso eu posso apagar resumo_acertos, resumo_erros, acertos_geral, erros_geral ->
    # Eles continuarão existindo apenas a título de checar os resultados durante a fase de testes.
    print('\n\nAcertos Gerais - vindo do dicionário de estatísticas')
    lista_interface_contexto_tag_acertos = [[acerto['interface'], acerto['contexto'], acerto['tag']]
        for item in estatisticas_por_contexto.values()
        for acerto in item['acertos']
        ]

    # O jeito mais bruto de fazer o passo acima:
    # lista = []
    # for contexto, item in estatisticas_por_contexto.items():
    #     # print(item['acertos'])
    #     for grupo in item['acertos']:
    #         # print(grupo)
    #         for tipo, resultado in grupo.items():
    #             # print(resultado)
    #             lista.append(resultado)
    #         # print(lista)
    #         lista2.append(list(lista))
    #         lista = []
    # # print(lista2)

    for item in lista_interface_contexto_tag_acertos:
        print(item)

    print('\n\nErros Gerais')
    for item in resumo_erros:
        print(item)

    print('\n\nAcertos do último Contexto')
    for item in acertos_por_contexto:
        print(item)

    print('\n\nErros do último Contexto')
    for item in erros_por_contexto:
        print(item)

    for k,v in estatisticas_por_contexto.items():
        print(k)
        print (v)


estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto = main(estatisticas_por_contexto, acertos_geral, erros_geral)
visualizar_resultados(estatisticas_por_contexto, acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto)
'''
