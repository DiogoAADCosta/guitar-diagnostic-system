'''====================================================================================================================================================================================================
Versão 8 - Reformulando perguntas e pipeline do teste para isolar habilidades de forma progressiva e facilitar o diagnóstico. Criando primeiro teste de interface
====================================================================================================================================================================================================
'''

from random import shuffle, choice
from collections import Counter
from itertools import chain, repeat



def lim(tag):
    return {'categoria': 'limitador', 'tag': tag}
def cap(tag):
    return {'categoria': 'capacidade', 'tag': tag}

perguntas_teste_interface_completo = [
    {
        'id': '1-1',
        'nivel': 1,
        'numero_pergunta': 1,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_cifras'],
        'pergunta': 'O que representa a letra G?',     # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True,  'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},    # Sabe relacionar nota com cifra
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
        'pergunta': 'O que significa Dm?',         # Pipeline: Ler Cifra > identificar nota e qualidade acorde
        'alternativas': [
            {'correcao': True,  'tag': [cap('qualidade_acorde')], 'texto': 'Ré menor'},    # Sabe diferenciar a cifra de acorde maior e menor
            {'correcao': False, 'tag': [lim('qualidade_acorde')], 'texto': 'Ré maior'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Dó menor'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Sol menor'},
            {'correcao': False, 'tag': [lim('fundamental_acorde')], 'texto': 'Lá menor'},
            {'correcao': False, 'tag': [lim('fundamental_acorde'),
                                        lim('qualidade_acorde')], 'texto': 'Dó maior'},
            {'correcao': False, 'tag': [lim('fundamental_acorde'),
                                        lim('qualidade_acorde')], 'texto': 'Sol maior'},
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
        'pergunta': '(DIAGRAMA C SHAPE A) Qual corda NÃO está sendo apertada nesse acorde?',  # Pipeline: Ler Diagrama > identificar posição cordas no diagrama
        'alternativas': [
            {'correcao': True, 'tag': [cap('diagrama_braco')], 'texto': 'A mais grossa'},  # Sabe a posição e ordem das cordas no diagrama
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'A mais fina'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Alguma corda do meio'},
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
        'pergunta': '(DIAGRAMA NOTA NA CORDA 3) A nota está em qual corda?',        # Pipeline: Ler Diagrama > identificar numeração das cordas no diagrama
        'alternativas': [
            {'correcao': True, 'tag': [cap('diagrama_braco')], 'texto': 'Corda 3'},           # Sabe a numeração das cordas no diagrama
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 1'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 2'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 4'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 5'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 6'},
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
        'pergunta': '(DIAGRAMA NOTAS CASAS 2 E 3) As notas estão em quais casas?',                          # Pipeline: Ler Diagrama > identificar número da casa no braço
        'alternativas': [
            {'correcao': True, 'tag': [cap('diagrama_braco')], 'texto': '2 e 3'},                        # Sabe interpretar casas no diagrama
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': '2 e 4'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': '1 e 3'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': '1 e 4'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': '2 e 5'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
    {
        'id': '1-5',
        'nivel': 1,
        'numero_pergunta': 5,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_tablatura'],
        'pergunta': '(TABLATURA COM MELODIA NA CORDA 1) Em qual corda essa melodia é tocada?',          # Pipeline: Ler Tablatura > identificar posição das cordas
        'alternativas': [
            {'correcao': True, 'tag': [cap('leitura_tablatura')], 'texto': 'Na mais fina'},             # Sabe a posição das cordas na tablatura
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Na mais grossa'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Em alguma corda do meio'},
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
        'pergunta': '(TABLATURA COM MELODIA NA CORDA 1) Em qual corda essa melodia é tocada?',          # Pipeline: Ler Tablatura > identificar posição das cordas
        'alternativas': [
            {'correcao': True, 'tag': [cap('leitura_tablatura')], 'texto': 'Na mais fina'},             # Sabe a posição das cordas na tablatura
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 3'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 4'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 5'},
            {'correcao': False, 'tag': [lim('diagrama_braco')], 'texto': 'Corda 6'},
            {'correcao': False, 'tag': [lim('base')], 'texto': 'Não sei', 'tipo': 'nao_sei'}
        ]
    },
]


lista_perguntas_teste_interface_completo = [
    {
        'id': '1-1',
        'nivel': 1,
        'numero_pergunta': 1,
        'etapa': 'interface',
        'contexto': [],
        'interface': ['leitura_cifras'],
        'pergunta': 'Pergunta_1?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_2?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_3?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_4?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_5?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_6?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Pergunta_7?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Simplificado Pergunta_1?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},            # Sabe relacionar nota com cifra
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
        'pergunta': 'Simplificado Pergunta_2?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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
        'pergunta': 'Simplificado Pergunta_3?',  # Pipeline: Ler Cifra > identificar nota
        'alternativas': [
            {'correcao': True, 'tag': [cap('fundamental_acorde')], 'texto': 'Nota Sol'},
            # Sabe relacionar nota com cifra
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


# Autoavaliação de Nível
def definir_nivel():
    autoavaliacao_nivel = int(input('Qual seu nível (1 a 5)? '))
    if autoavaliacao_nivel == 1:
        # Necessário pois as pessoas no nível 1 e 2 começarão pelo mesmo teste nível 2.
        return 2
    else:
        return autoavaliacao_nivel


# Define se faz teste interface completo ou simplificado
def tipo_teste_interface(nivel):
    if nivel <= 3:
        return 'completo'
    else:
        return 'simplificado'

# Define qual lista de perguntas utilizar
def lista_de_perguntas(tipo_teste):
    if tipo_teste == 'completo':
        return lista_perguntas_teste_interface_completo.copy()
    else:
        return lista_perguntas_teste_interface_simplificado.copy()

def mostrar_alternativas(pergunta, letras_alternativas):
        # Embaralhar alternativas
        alternativas_para_embaralhar =[]
        alternativas_nao_sei = []
        for alternativa in pergunta['alternativas']:
            if alternativa.get('tipo') == 'nao_sei':
                alternativas_nao_sei.append(alternativa)
            else:
                alternativas_para_embaralhar.append(alternativa)
        # shuffle(alternativas_para_embaralhar)
        alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


        mapa_respostas = {}
        # Mostrar alternativas
        for numero, alternativa in enumerate(alternativas_para_mostrar):
            print(f'{letras_alternativas[numero]} - {alternativa['texto']}')
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa
        return mapa_respostas

# Executa o teste de interface
def executar_teste_interface(lista_perguntas, tipo_teste):
    letras_alternativas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    acertos_interface = []
    erros_interface = []
    acertos = 0
    erros = 0
    # Mostrar pergunta
    for pergunta in lista_perguntas:
        print(pergunta['pergunta'])

        # Embaralhar alternativas
        alternativas_para_embaralhar =[]
        alternativas_nao_sei = []
        for alternativa in pergunta['alternativas']:
            if alternativa.get('tipo') == 'nao_sei':
                alternativas_nao_sei.append(alternativa)
            else:
                alternativas_para_embaralhar.append(alternativa)
        # shuffle(alternativas_para_embaralhar)
        alternativas_para_mostrar = alternativas_para_embaralhar + alternativas_nao_sei


        mapa_respostas = {}
        # Mostrar alternativas
        for numero, alternativa in enumerate(alternativas_para_mostrar):
            print(f'{letras_alternativas[numero]} - {alternativa['texto']}')
            letra = letras_alternativas[numero]
            mapa_respostas[letra] = alternativa
            # Guardar resposta

        resposta_usuario = input('Resposta: ').strip().upper()

        # Guardar_acertos_erros_interface()
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
            # Se erra no teste simplificado é direcionado para o teste completo
            erros_interface.append(guardar)
            if tipo_teste == 'simplificado':
                return 'erro no teste simplificado', acertos_interface, erros_interface
    return 'teste ok', acertos_interface, erros_interface


# Rodar o teste de interface dinâmico, ou seja, se a pessoa errar no teste simplificado, é direcionada imediatamente para o completo.
def rodar_teste_interface(nivel):
    # Define se faz teste interface completo ou simplificado
    tipo_teste = tipo_teste_interface(nivel)

    while True:
        # Define qual lista de perguntas utilizar
        lista_perguntas = lista_de_perguntas(tipo_teste)

        # Executa o teste de interface
        resultado, acertos_interface, erros_interface = executar_teste_interface(lista_perguntas, tipo_teste)

        if resultado == 'erro no teste simplificado':
            tipo_teste = 'completo'
            continue

        return acertos_interface, erros_interface

# Calcular_score()
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



# def calcular_score_teste_simplificado:
# Resultado_interface()


# Autoavaliação de Nível
nivel = definir_nivel()
# nivel = 2



# Rodar o teste de interface dinâmico, ou seja, se a pessoa errar no teste simplificado, é direcionada imediatamente para o completo.
acertos_interface, erros_interface = rodar_teste_interface(nivel)

print(acertos_interface)
print(erros_interface)

# Calcular_score()
sabe_ler_cifra, sabe_ler_diagrama, sabe_ler_tablatura = calcular_score_teste_completo(erros_interface)

# Mostrar resultados de Interface
print(f'\nSabe ler cifra: {sabe_ler_cifra}\nSabe ler diagrama: {sabe_ler_diagrama}\nSabe ler tablatura: {sabe_ler_tablatura}')

# acertos_geral, erros_geral, acertos_por_contexto, erros_por_contexto = executar_teste_contexto_unico(lista_contextos)

print(acertos_geral)
print(erros_geral)


