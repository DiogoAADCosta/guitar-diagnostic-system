"""
Version 10 — Context Score Evaluation and Adaptive Question Flow

This version introduces adaptive behavior within the context-based test.

The system now evaluates user performance during execution,
using intermediate accuracy to control the number of questions.

The context test now includes:

- Partial score calculation (accuracy rate)
- Rule-based decision system (rodar_condicoes)
- Dynamic question extension based on performance
- Structured result collection (general and per context)

Note:
- Context switching is not implemented yet
- Level progression logic exists but is not fully active
- The system evaluates one context per execution
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
            print(f"{letras_alternativas[numero]} - {alternativa['texto']}")
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa
        return mapa_respostas

# Execute interface test
def executar_teste_interface(lista_perguntas, tipo_teste):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_interface = []
    erros_interface = []
    acertos = 0
    erros = 0
    for pergunta in lista_perguntas:
        print(pergunta['pergunta'])

        # DUPLICATION (temporary)
        # This block replicates the logic from mostrar_alternativas.
        # It was implemented before the function was reused here.
        # Will be refactored in future versions to avoid duplication.
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

        resultado, acertos_interface, erros_interface = executar_teste_interface(lista_perguntas, tipo_teste)

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


lista_contextos = [
    'power_chords',
    'triades_simples'
]

# Execute context-based test with adaptive question flow and tag collection
def executar_teste_contexto_unico(lista_contextos, nivel, ja_subiu_nivel, ja_desceu_nivel):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_por_contexto = []
    erros_por_contexto = []
    acertos_geral = []
    erros_geral = []
    acertos = 0
    erros = 0
    perguntas_restantes = 4
    total_perguntas = 0
    indice_contexto = 0
    rodada = 1
    contexto = lista_contextos[indice_contexto]
    lista_perguntas = lista_perguntas_teste_contexto

    for pergunta in lista_perguntas:
        if pergunta['contexto'][0] == contexto:
            print(f"Contexto: {pergunta['contexto']} - {pergunta['pergunta']}")
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
                print('Você acertou!')
                acertos += 1
                acertos_geral.append(guardar)
                acertos_por_contexto.append(guardar)
            else:
                print('Você errou')
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

                nivel, rodada, perguntas_restantes, ja_subiu_nivel, ja_desceu_nivel, = rodar_condicoes(taxa_acertos, rodada, nivel, ja_subiu_nivel, ja_desceu_nivel)
                if perguntas_restantes == 0:
                    break

    return acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto

# LEGACY (from previous versions)
# These functions were reused from earlier versions.
# Not all of them are actively used in v010.
# They are kept temporarily for compatibility with progression logic.
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

# Helper functions used by rule-based progression system
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

# Rule set for progression decisions based on accuracy and round
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

# Execute rule set based on accuracy and current round
def rodar_condicoes(taxa_acertos, rodada, nivel, ja_subiu_nivel, ja_desceu_nivel):
    for condicao, acao in regras[rodada]:
        if condicao(taxa_acertos):
            nivel_anterior = nivel
            nivel, rodada, perguntas_restantes, ja_subiu_nivel, ja_desceu_nivel = acao(nivel, rodada, ja_subiu_nivel, ja_desceu_nivel)
            # LIMITATION (v010)
            # This block handles level transitions, but level change is not active in this version.
            # The logic is preserved for future implementation.
            if nivel != nivel_anterior:
                # Reset counters when level changes
                acertos = 0
                erros = 0
                total_perguntas = 0
                ultima_pergunta = 0
            return nivel, rodada, perguntas_restantes, ja_subiu_nivel, ja_desceu_nivel



nivel = definir_nivel()

# Flags to control level transition state
ja_subiu_nivel = False
ja_desceu_nivel = False

# Run interface test with fallback from simplified to complete
acertos_interface, erros_interface = rodar_teste_interface(nivel)

print(acertos_interface)
print(erros_interface)

# Calculate interface reading ability based on errors
sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura = calcular_score_teste_completo(erros_interface)

# Display interface test results
print(f'\nSabe ler cifra: {sabe_ler_cifra}\nSabe ler diagrama: {sabe_ler_diagrama}\nSabe ler tablatura: {sabe_ler_tablatura}')

# Execute context-based test with tag collection
acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto = executar_teste_contexto_unico(lista_contextos, nivel, ja_subiu_nivel, ja_desceu_nivel)

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

print('\n\nAcertos Gerais')
for item in resumo_acertos:
    print(item)
print('\n\nErros Gerais')
for item in resumo_erros:
    print(item)
