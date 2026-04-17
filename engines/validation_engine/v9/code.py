"""
Version 9 — Context-Based Test Implementation

This version extends the test pipeline by introducing
the context-based evaluation stage.

The system now includes:

- Context test based on predefined contexts
- Structured question model:
    - etapa (interface / contexto)
    - interface
    - contexto
- Collection of:
    - interface results
    - context-based results (general and per context)

Note:
Context progression logic is not implemented yet.
The test currently evaluates a single context per execution.
"""

from random import shuffle


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
        'id': '1-1',
        'nivel': 1,
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
        'id': '1-2',
        'nivel': 1,
        'numero_pergunta': 2,
        'etapa': 'contexto',
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
        'id': '1-3',
        'nivel': 1,
        'numero_pergunta': 3,
        'etapa': 'contexto',
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
        'id': '1-4',
        'nivel': 1,
        'numero_pergunta': 4,
        'etapa': 'contexto',
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
        'id': '1-5',
        'nivel': 1,
        'numero_pergunta': 5,
        'etapa': 'contexto',
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
        'id': '1-6',
        'nivel': 1,
        'numero_pergunta': 6,
        'etapa': 'contexto',
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
        'id': '1-7',
        'nivel': 1,
        'numero_pergunta': 7,
        'etapa': 'contexto',
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
        'id': '1-8',
        'nivel': 1,
        'numero_pergunta': 8,
        'etapa': 'contexto',
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
        'id': '1-9',
        'nivel': 1,
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
        'id': '1-10',
        'nivel': 1,
        'numero_pergunta': 2,
        'etapa': 'contexto',
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
        'id': '1-11',
        'nivel': 1,
        'numero_pergunta': 3,
        'etapa': 'contexto',
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
        'id': '1-12',
        'nivel': 1,
        'numero_pergunta': 4,
        'etapa': 'contexto',
        'contexto': ['triades_simples'],
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
        'id': '1-13',
        'nivel': 1,
        'numero_pergunta': 5,
        'etapa': 'contexto',
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
        'id': '1-14',
        'nivel': 1,
        'numero_pergunta': 6,
        'etapa': 'contexto',
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
        'id': '1-15',
        'nivel': 1,
        'numero_pergunta': 7,
        'etapa': 'contexto',
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
        'id': '1-16',
        'nivel': 1,
        'numero_pergunta': 8,
        'etapa': 'contexto',
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
]

# User self-assessment of level
def definir_nivel():
    autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
    if autoavaliacao_nivel == 1:
        # Levels 1 and 2 start from the same entry point (level 2 test)
        return 2
    else:
        return autoavaliacao_nivel


# Determine whether to use complete or simplified interface test
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
        # Separate alternatives to keep "I don't know" at the end (not shuffled)
        alternativas_para_embaralhar =[]
        alternativas_nao_sei = []
        for alternativa in pergunta['alternativas']:
            if alternativa.get('tipo') == 'nao_sei':
                alternativas_nao_sei.append(alternativa)
            else:
                alternativas_para_embaralhar.append(alternativa)
        shuffle(alternativas_para_embaralhar)
        alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


        mapa_respostas = {}
        for numero, alternativa in enumerate(alternativas_para_mostrar):
            print(f"{letras_alternativas[numero]} - {alternativa['texto']}")
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa
        return mapa_respostas
  
# Execute interface test and collect performance data
# Note:
# Alternative handling logic (shuffle + mapping) is duplicated here.
# This was intentionally kept during development,
# as the abstraction was first implemented for the context stage.
# Refactoring to reuse mostrar_alternativas() will be done in a future version.
def executar_teste_interface(lista_perguntas, tipo_teste):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_interface = []
    erros_interface = []
    # Counters reserved for future accuracy calculations (not used yet)
    acertos = 0
    erros = 0
    for pergunta in lista_perguntas:
        print(pergunta['pergunta'])

        alternativas_para_embaralhar =[]
        alternativas_nao_sei = []
        for alternativa in pergunta['alternativas']:
            if alternativa.get('tipo') == 'nao_sei':
                alternativas_nao_sei.append(alternativa)
            else:
                alternativas_para_embaralhar.append(alternativa)
        shuffle(alternativas_para_embaralhar)
        alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


        mapa_respostas = {}
        for numero, alternativa in enumerate(alternativas_para_mostrar):
            print(f"{letras_alternativas[numero]} - {alternativa['texto']}")
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa

        resposta_usuario = input('Resposta: ').strip().upper()

        # Extract only tag names (discard category: capability/limitation)
        tag = [tag['tag'] for tag in mapa_respostas[resposta_usuario]['tag']]
        # Store interface and extracted tags from the answer
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
            # If the user fails the simplified test, switch to complete test
            erros_interface.append(guardar)
            if tipo_teste == 'simplificado':
                return 'erro no teste simplificado', acertos_interface, erros_interface
    return 'teste ok', acertos_interface, erros_interface


# Run interface test dynamically:
# if the user fails the simplified test, automatically switch to complete test
def rodar_teste_interface(nivel):
    tipo_teste = tipo_teste_interface(nivel)

    # Repeat test if fallback from simplified to complete is required
    while True:
        lista_perguntas = lista_de_perguntas(tipo_teste)

        resultado, acertos_interface, erros_interface = executar_teste_interface(lista_perguntas, tipo_teste)

        if resultado == 'erro no teste simplificado':
            tipo_teste = 'completo'
            continue

        return acertos_interface, erros_interface

# Calculate interface proficiency based on errors per interface
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


lista_contextos = [
    'power_chords',
    'triades_simples'
]

# Execute context-based test and collect results (general and per context)
def executar_teste_contexto_unico(lista_contextos):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_por_contexto = []
    erros_por_contexto = []
    acertos_geral = []
    erros_geral = []
    # Counters reserved for future accuracy calculations (not used yet)
    acertos = 0
    erros = 0
    indice_contexto = 0
    # Current version evaluates only one context (first in list)
    contexto = lista_contextos[indice_contexto]
    lista_perguntas = lista_perguntas_teste_contexto

    for pergunta in lista_perguntas:
        # Filter questions by current context
        if pergunta['contexto'][0] == contexto:
            print(f"Contexto: {pergunta['contexto']} - {pergunta['pergunta']}")
            mapa_respostas = mostrar_alternativas(pergunta, letras_alternativas)

            resposta_usuario = input('Resposta: ').strip().upper()

            # Extract only tag names (discard category: capability/limitation)
            tag = [tag['tag'] for tag in mapa_respostas[resposta_usuario]['tag']]
            # Store interface, context, and extracted tags from the answer
            guardar = {
                'interface': pergunta['interface'][0],
                'contexto': pergunta['contexto'][0],
                'tag': tag
            }
            if mapa_respostas[resposta_usuario]['correcao']:
                print('Você acertou!')
                acertos += 1
                acertos_geral.append(guardar)
                acertos_por_contexto.append(guardar)
            else:
                print('Você errou')
                erros += 1
                erros_geral.append(guardar)
                erros_por_contexto.append(guardar)

    return acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto


nivel = definir_nivel()

acertos_interface, erros_interface = rodar_teste_interface(nivel)

print(acertos_interface)
print(erros_interface)

sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura = calcular_score_teste_completo(erros_interface)

# Display interface results
print(f'\nSabe ler cifra: {sabe_ler_cifra}\nSabe ler diagrama: {sabe_ler_diagrama}\nSabe ler tablatura: {sabe_ler_tablatura}')

# Run context-based test
acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto = executar_teste_contexto_unico(lista_contextos)

print(acertos_geral)
print(erros_geral)

