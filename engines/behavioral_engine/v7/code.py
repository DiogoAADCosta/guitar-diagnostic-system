# Version 7 - Attempted Connector Abstraction
#
# Goal:
# Attempt to reduce code repetition by abstracting connector logic into functions.
#
# In this version:
# - Introduced functions to handle sentence connectors
# - Attempted to centralize connector selection logic
# - Partial reduction of direct conditional usage
#
# Additionally:
# - Debug statements were added to track connector behavior
# - A hybrid approach was used (functions + manual conditions)
#
# Limitation:
# - Connector counters do not update outside function scope
# - The abstraction does not work as intended
# - Code complexity increased instead of decreasing
#
# Focus:
# Experiment with abstraction → exposes limitations in state management

from collections import Counter
from random import choice


lista_perguntas = [
     {'id': 1,
     'pergunta': '1 - Quando monta um acorde, você: ',
     'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não consigo montar nenhum acorde'},                       
                    {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Monta um dedo de cada vez'},
                    {'resposta': 'C', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Monta em blocos (2 dedos + o resto)'},
                    {'resposta': 'D', 'tag': [['capacidade', 'troca_de_acorde']], 'texto': 'Consegue encaixar todos os dedos de uma vez'}
                    ]
    },
    {'id': 2,
     'pergunta': '2 - Tocando com uma música ou metrônomo, você consegue trocar os acordes sem atrasar o ritmo?',
    'respostas':  [{'resposta': 'A', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo nem começar a tocar com a música'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Preciso parar o ritmo para trocar o acorde'},
                   {'resposta': 'C', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo me manter no ritmo'},
                   {'resposta': 'D', 'tag': [['capacidade', 'ritmo']], 'texto': 'Consigo me manter no ritmo, mas escapando às vezes'},
                   {'resposta': 'E', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'O ritmo continua normal'}
                   ]
    },
    {'id': 3,
     'pergunta': '3 - Quando monta um acorde qualquer, sem pestana, e toca uma corda de cada vez: ',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Há duas ou mais cordas que o som não sai'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Há uma única corda que o som não sai'},
                   {'resposta': 'D', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Você consegue ouvir bem o som de cada corda'}
                   ]
     },
    {'id': 4,
     'pergunta': '4 - Diagramas Lá maior Shape de A e Shape de E ',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei ler esse diagrama e montar os acordes'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Sei ler o diagrama mas não consigo tocar nenhum'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Toco apenas um e o som não sai legal'},
                   {'resposta': 'D', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Toco apenas um e o som sai legal'},
                   {'resposta': 'E', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Toco os dois e o som não sai legal'},
                   {'resposta': 'F', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Toco os dois sem dificuldade'}
                   ]
     },
    {'id': 5,
     'skip_if': 'nao_sabe_pestana',   # Skip this question if the user does not know what a barre chord is
     'pergunta': '5 - Ao fazer um Fá maior com pestana, você consegue ouvir o som das cordas 1, 2, 3?',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'base']], 'texto': 'Não sei quais são as cordas 1, 2, 3'},
                   {'resposta': 'C', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Não ouço as cordas 1, 2, 3'},
                   {'resposta': 'D', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Ouço apenas uma das cordas'},
                   {'resposta': 'E', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Ouço apenas duas das cordas (uma corda ainda fica com som abafado)'},
                   {'resposta': 'F', 'tag': [['capacidade', 'montagem_de_acorde']], 'texto': 'Ouço claramente todas as cordas'}
                   ]
     },
    {'id': 6,
     'pergunta': '6 - Em uma música aparecem os seguintes acordes: C Am F G. Você:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sabe montar todos os acordes'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Demora pra trocar os acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'troca_de_acorde'], ['capacidade', 'ritmo']], 'texto': 'Tem uma certa dificuldade na hora de trocar de acorde mas ainda consegue acompanhar'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'Consegue trocar de acordes rápido, mas tem dificuldade para se manter no ritmo'},
                   {'resposta': 'E', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']], 'texto': 'Acha fácil e consegue tocar sem problemas'}
                   ]
     },
    {'id': 7,
     'skip_if': 'nao_sabe_pestana',                         # Skip this question if the user does not know what a barre chord is
     'pergunta': '7 - Tocando uma música inteira com muitos acordes com pestana:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'base']], 'texto': 'Não sei o que é pestana'},
                   {'resposta': 'B', 'tag': [['limitador', 'montagem_de_acorde'], ['limitador', 'nao_consegue_pestana']], 'texto': 'Não consigo ainda fazer pestana'},
                   {'resposta': 'C', 'tag': [['limitador', 'resistencia']], 'texto': 'Cansa/dói a mão'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo']], 'texto': 'Perco o ritmo'},
                   {'resposta': 'E', 'tag': [['limitador', 'resistencia'], ['capacidade', 'ritmo']], 'texto': 'Cansa a mão um pouco mas toco inteira'},
                   {'resposta': 'F', 'tag': [['capacidade', 'resistencia'], ['capacidade', 'ritmo']], 'texto': 'Toco sem problema'}
                   ]
     },
    {'id': 8,
     'pergunta': '8 - Se você erra durante uma música, você:',
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'ritmo']], 'texto': 'Não consigo ainda acompanhar músicas'},
                   {'resposta': 'B', 'tag': [['limitador', 'continuidade']], 'texto': 'Preciso parar a música e voltar para uma parte específica para conseguir voltar a tocar junto'},
                   {'resposta': 'C', 'tag': [['limitador', 'continuidade']], 'texto': 'Consigo voltar a tocar com a música sem parar, mas demoro um  pouco esperando uma parte específica'},
                   {'resposta': 'D', 'tag': [['capacidade', 'continuidade']], 'texto': 'Consigo voltar a tocar com a música quase que imediatamente após o erro'}
                   ]
     },
    {'id': 9,
     'pergunta': '9 - O que você acha mais difícil?',      # This question supports multiple answers (handled in frontend / JavaScript)
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Montar os acordes e soar limpos'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Trocas rápidas de acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'base']], 'texto': 'Ler cifras e tablaturas'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo']], 'texto': 'Tocar junto com a música'}
                   ]
     }
]

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

nao_sabe_pestana = False

for questao in lista_perguntas:

    if nao_sabe_pestana == True and questao.get('skip_if') == 'nao_sabe_pestana':
        lista_limitadores_respostas_usuario.append('base')
        continue    

    print()
    print(questao['pergunta'])
    print()

    for alternativa in questao['respostas']:
        print(f'{alternativa['resposta']} - {alternativa['texto']}')


    resposta_usuario = input('\nSua Resposta: ').strip().upper()


    if (questao['id'] == 3 and resposta_usuario == 'A') or (questao['id'] == 5 and resposta_usuario == 'A'):
        nao_sabe_pestana = True

    for alternativa in questao['respostas']:
        if questao['id'] == 9:
            if alternativa['resposta'] in resposta_usuario:
                lista_limitadores_respostas_usuario.append(alternativa['tag'][0][1])
        else:
            if resposta_usuario == alternativa['resposta']:
                for tipo, tag in alternativa['tag']:

                    if tipo == 'limitador':
                        lista_limitadores_respostas_usuario.append(tag)

                    elif tipo == 'capacidade':
                        lista_capacidades_respostas_usuario.append(tag)


# Diagnostic structure definition
lista_diagnostico = {
    'montagem_de_acorde': {
        'descricao_capacidade': 'consegue montar acordes com clareza',
        'efeito_positivo': 'seus acordes soam “limpos”',
        'descricao_limitacao': 'tem dificuldade em montar os acordes com clareza. Algumas cordas saem abafadas',
        'efeito_negativo': 'os acordes soam “sujos”',
        'recomendacao': 'foque em montar os acordes sem encostar os dedos em cordas vizinhas, para não abafar cordas que devem soar'
    },
    'troca_de_acorde': {
        'descricao_capacidade': 'consegue trocar acordes em uma velocidade boa',
        'efeito_positivo': 'é muito mais difícil você se perder no ritmo de uma música',
        'descricao_limitacao': 'tem dificuldade para trocar os acordes',
        'efeito_negativo': 'a fluidez da execução fica prejudicada, ou seja, você toca a música "aos tropeços", não consegue tocar a música sem ficar parando',
        'recomendacao': 'foque em tentar construir os acordes posicionando todos os dedos ao mesmo tempo'
    },
    'ritmo': {
        'descricao_capacidade': 'consegue manter o ritmo em boa parte do tempo',
        'efeito_positivo': 'você é capaz tocar músicas do início ao fim sem se perder',
        'descricao_limitacao': 'tem dificuldade em manter o ritmo constante',
        'efeito_negativo': 'você se perde bastante tocando uma música',
        'recomendacao': 'foque em tocar músicas sem perder o ritmo. Sacrifique acordes “limpos” neste momento. Se você conseguir se manter no ritmo com acordes “sujos”, o problema realmente é a velocidade na troca de acordes. Senão é um problema de ritmo mais profundo, que deve ser trabalhado desde o zero'
    },
    'resistencia': {
        'descricao_capacidade': 'consegue sustentar acordes com pestana por mais tempo sem perder qualidade',
        'efeito_positivo': 'você é capaz de tocar um leque maior de músicas',
        'descricao_limitacao': 'tem dificuldade para sustentar acordes com pestana por muito tempo. Sua mão ainda não está fortalecida o suficiente para isso',
        'efeito_negativo': 'você tem que fazer mini pausas de descanso durante uma música, perdendo consistência',
        'recomendacao': 'foque em tocar músicas com muitos acordes com pestana. Apenas usando bastante esses acordes você fortalecerá sua mão e será capaz de tocar pestana sem cansar/doer a mão'
    },
    'continuidade': {
        'descricao_capacidade': 'consegue se manter na música mesmo após pequenos erros',
        'efeito_positivo': 'você já é capaz de tocar com uma banda',
        'descricao_limitacao': 'tem dificuldade em se reencontrar na música após cometer um erro',
        'efeito_negativo': 'você se perde e precisa parar de tocar antes de conseguir voltar, dificultando tocar do início ao fim com fluidez'
    },
    'base': {
        'descricao_limitacao': 'não domina conceitos básicos do instrumento',
        'efeito_negativo': 'várias etapas do processo ficam difíceis',
        'recomendacao': 'foque ainda em dominar a base. Saber ler cifras, tablaturas, e conceitos básicos te farão conseguir dar o próximo passo com muito mais facilidade'
    },
    'nao_consegue_pestana': {
        'descricao_limitacao': 'não consegue fazer acordes com pestana',
        'efeito_negativo': 'o seu repertório fica bem limitado e você fica preso a uma única região do braço da guitarra',
        'recomendacao': 'foque em tentar tocar acordes com pestana, mesmo que não saiam 100%. Apenas assim você vai conseguir dar esse próximo passo'
    }
}

lista_nivel = {
    'iniciante': [ # Multiple phrasing options for randomized feedback
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

# Profile definitions based on tag combinations
perfis = {
    'perfil_equilibrado': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'},  
        'limitadores': set(),
        'descricao': 'Você já é um guitarrista bem equilibrado, capaz de tocar várias músicas com fluidez.'
    },
    'perfil_falso_avancado': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'}, 
        'limitadores': {'base'},
        'descricao': 'Você consegue tocar músicas inteiras sem se perder, porém ainda tem lacunas nos conhecimentos de base e isso pode travar sua evolução logo mais.'
    },
    'perfil_ritmo_travado': {
        'capacidades': {'troca_de_acorde', 'montagem_de_acorde'}, 
        'limitadores': {'ritmo'},
        'descricao': 'Você tem familiaridade com acordes e consegue trocar com rapidez, mas ainda não consegue acompanhar músicas pois falta base em ritmo.'
    },
    'perfil_quase_equilibrado_ritmo': {
        'capacidades': {'troca_de_acorde', 'ritmo', 'montagem_de_acorde'}, 
        'limitadores': {'ritmo'},
        'descricao': 'Você está quase tocando músicas de forma equilibrada e com fluidez. Porém ainda há pequenas dificuldades de ritmo em alguns momentos.'

    }
}

# Sentence connectors
conectores_cap = [
    'Você já ',
    'Você também ',
    'Além disso, você também ',
    'Também vale destacar que você ',
    'Outro ponto positivo é que você '
]

conectores_lim = [
    'Você ainda ',
    'Por outro lado, você ainda ',
    'Além disso, você ',
    'Também vale destacar que você ',
    'Importante ressaltar que você ainda '
]

conectores_causa_efeito = [
    '. Por conta disso, ',
    '. Com isso, ',
    '. Por isso ',
    '. Acaba que ',
    '. Como consequência disso, '
]

contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)

maior_frequencia_limitadores = max(contador_limitadores.values(), default=0)
maior_frequencia_capacidades = max(contador_capacidades.values(), default=0)

# Primary tags (others are handled as additional observations)
limitadores_principais = ['base', 'troca_de_acorde', 'ritmo', 'montagem_de_acorde']
capacidades_principais = ['troca_de_acorde', 'ritmo', 'montagem_de_acorde']

# Build list of most frequent tags (dominant signals)
limitadores_mais_frequentes = []
for item, quantidade in contador_limitadores.items():
    if quantidade == maior_frequencia_limitadores and quantidade >= 2 and item in limitadores_principais:  # Filter only primary limitation tags (others handled later)
        limitadores_mais_frequentes.append(item)
capacidades_mais_frequentes = []
for item, quantidade in contador_capacidades.items():
    if quantidade == maior_frequencia_capacidades and quantidade >= 2 and item in capacidades_principais: # Same logic applied to capabilities
        capacidades_mais_frequentes.append(item)

# Determine user level based on balance of limitations vs capabilities
nivel = ''
if (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) >= 2:
        nivel = 'iniciante'
elif abs(len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= 1:
        nivel = 'intermediario'
elif (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= -2:
        nivel = 'avancado'

print()
print('=' * 100)
print(f'{"DIAGNÓSTICO FINAL":^100}')
print('=' * 100)
print()


# Counters controlling sentence connector selection
conectores_cap_contador = 0
conectores_lim_contador = 0


# Connector selection functions (attempted abstraction)
def conector_cap(conectores_cap_contador):
    conector = conectores_cap[min(conectores_cap_contador, len(conectores_cap) - 1)]      # Prevent index overflow by capping at last connector
    return conector

def conector_lim(conectores_lim_contador):
     # Depends on external counter (design limitation in this version)
    if conectores_cap_contador == 0 and conectores_lim_contador == 0:
        conector = conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)]
        return conector
    elif conectores_cap_contador != 0 and conectores_lim_contador == 0:
        conectores_lim_contador += 1
        conector = conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)]
        return conector
    elif conectores_cap_contador == 0 and conectores_lim_contador == 1:
        # Note: counter changes here do not persist outside the function (scope limitation)
        conectores_lim_contador += 1
        conector = conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)]
        return conector
    else:
        conector = conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)]
        return conector
        

# Profile-based diagnosis
perfil = ''
for tipo, descricao in perfis.items():
    if descricao['capacidades'] == set(capacidades_mais_frequentes) and descricao['limitadores'] == set(limitadores_mais_frequentes):
        perfil = tipo
        print('\n1 - PERFIS ----------------\n')
        print(descricao['descricao'])   
        conectores_cap_contador += 1


# Additional observations (capabilities)
print('\n2 - CONSIDERAÇÕES ADICIONAIS PARTE 1------------------\n')
if 'resistencia' in lista_capacidades_respostas_usuario:
    print(conector_cap(conectores_cap_contador), end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_positivo"]}.')
    conectores_cap_contador += 1
if 'continuidade' in lista_capacidades_respostas_usuario:
    print(conector_cap(conectores_cap_contador), end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_positivo"]}.')
    conectores_cap_contador += 1




# Fallback: no profile matched
print('\n3 - DIAGNÓSTICOS ISOLADOS -----------------------\n')
if perfil == '':
    for capacidade in capacidades_mais_frequentes:
        print(conector_cap(conectores_cap_contador), end='')
        print(f'{lista_diagnostico[capacidade]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico[capacidade]["efeito_positivo"]}.')
        conectores_cap_contador += 1
    if 'montagem_de_acorde' in limitadores_mais_frequentes and 'troca_de_acorde' in limitadores_mais_frequentes:
        print(conector_lim(conectores_lim_contador), end='')
        print('está consolidando a montagem dos acordes, o que impacta diretamente na velocidade de troca. A dificuldade na troca vem da montagem dos acordes ainda não estar automática.')
        conectores_lim_contador += 1
    elif 'montagem_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(conector_lim(conectores_lim_contador), end='')
        print('tem dificuldade na montagem dos acordes e isso acaba interferindo no seu ritmo.')
        conectores_lim_contador += 1
    elif 'troca_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(conector_lim(conectores_lim_contador), end='')
        print('tem dificuldade tanto na troca de acordes quanto em manter o ritmo, o que faz você se perder facilmente nas músicas. Você perde o ritmo pois ainda tem dificuldades na troca de acordes.')
        conectores_lim_contador += 1
    else:
        for limitador in limitadores_mais_frequentes:
            print(conector_lim(conectores_lim_contador), end='')
            print(f'{lista_diagnostico[limitador]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico[limitador]["efeito_negativo"]}.')
            conectores_lim_contador += 1


# Additional observations (limitations)
print('\n4 - CONSIDERAÇÕES ADICIONAIS PARTE 2------------------\n')
if 'resistencia' in lista_limitadores_respostas_usuario:
    print(conector_lim(conectores_lim_contador), end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_negativo"]}.')
    conectores_lim_contador += 1
if 'nao_consegue_pestana' in lista_limitadores_respostas_usuario:
    print(conector_lim(conectores_lim_contador), end='')
    print(f'{lista_diagnostico["nao_consegue_pestana"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["nao_consegue_pestana"]["efeito_negativo"]}.')
    conectores_lim_contador += 1
if 'continuidade' in lista_limitadores_respostas_usuario:
    print(conector_lim(conectores_lim_contador), end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_negativo"]}.')
    conectores_lim_contador += 1




# Level diagnosis
print('\n5 - NÍVEL ------------\n')
print('Considerando seus pontos fortes e limitações, você se encontra no seguinte estágio:')
print(choice(lista_nivel[nivel]))
