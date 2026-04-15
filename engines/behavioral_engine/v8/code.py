# Version 8 - Dynamic Connector Control and Narrative Flow Adjustment
#
# Goal:
# Improve sentence flow by refining connector logic,
# ensuring more natural transitions between strengths and limitations.
#
# In this version:
# - Refined connector behavior using existing counters
# - Introduced contextual adjustment of limitation connectors based on prior output
# - Improved narrative flow between strengths and limitations
# - Simplified connector handling without using function abstraction
# - Stabilized sentence construction after failed abstraction attempt (Version 7)
# - Adjusted limitation connectors to avoid unnatural sentence openings (e.g., avoiding contrast without prior context)
#
# Focus:
# Failed abstraction → Direct control → Stable and coherent narrative flow

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
     'skip_if': 'nao_sabe_pestana',   # Pula essa pergunta se a pessoa não sabe pestana
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
     'skip_if': 'nao_sabe_pestana',                          # Pula essa pergunta se a pessoa não sabe pestana
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
     'pergunta': '9 - O que você acha mais difícil?',      # Essa pergunta permitirá mais de uma resposta. Não farei a lógica pra isso aqui em python, apenas em JavaScript
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Montar os acordes e soar limpos'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Trocas rápidas de acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'base']], 'texto': 'Ler cifras e tablaturas'},
                   {'resposta': 'D', 'tag': [['limitador', 'ritmo']], 'texto': 'Tocar junto com a música'}
                   ]
     }
]

# Listas que guardarão as tags de cada resposta do usuário
lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

# Variável que será ativada quando o usuário não souber o que é pestana (Resposta A na pergunta 3 ou A na pergunta 5)
nao_sabe_pestana = False

# Para cada questão na lista de perguntas
for questao in lista_perguntas:

    # Se o usuário não sabe o que é pestana, as perguntas 5 e 7 não aparecem pois assume-se que as respostas seriam as mesmas. Dessa forma a tag 'base' é adicionada automaticamente na lista limitadores.
    # O questao.get verifica se há um 'skip_if' nos dados para comparar. Se tiver ele compara. Se não tiver ele continua, sem dar erro.
    if nao_sabe_pestana == True and questao.get('skip_if') == 'nao_sabe_pestana':
        lista_limitadores_respostas_usuario.append('base')
        continue    # Pula para a próxima iteração do loop. Ou seja, vai para a próxima questao em lista_perguntas.

    # Mostre a pergunta
    print()
    print(questao['pergunta'])
    print()

    for alternativa in questao['respostas']:
        # Mostre as alternativas
        print(f'{alternativa['resposta']} - {alternativa['texto']}')

    # Capta a resposta do usuário - aqui não estou preocupado com validar a resposta pois na versão final o usuário não digitará. Ele clicará em uma das opções na tela. Será feito provavelmente em JavaScript
    resposta_usuario = input('\nSua Resposta: ').strip().upper()


    # Se o usuário responde que não sabe o que é pestana nas perguntas 3 ou 5, ele ativa a variável nao_sabe_pestana, para evitar
    if (questao['id'] == 3 and resposta_usuario == 'A') or (questao['id'] == 5 and resposta_usuario == 'A'):
        nao_sabe_pestana = True

# Compara a resposta do usuário com as alternativas de cada questão para guardar a tag correspondente daquela alternativa
    for alternativa in questao['respostas']:
        # Aqui a questão 9 pode receber mais de uma resposta, logo guarda mais de uma tag.
        if questao['id'] == 9:
            if alternativa['resposta'] in resposta_usuario:
                lista_limitadores_respostas_usuario.append(alternativa['tag'][0][1])
        else:
            if resposta_usuario == alternativa['resposta']:

                # Varre todos os primeiros termos das tags para ver se são limitadores ou capacidades, para então guardar nas listas de limitadores ou capacidades
                # Simplifiquei a forma de varrer os itens dentro da tag, não mais por índices [0], [1], etc
                for tipo, tag in alternativa['tag']:

                    # Lista limitadores
                    if tipo == 'limitador':
                        lista_limitadores_respostas_usuario.append(tag)

                    # Lista capacidades
                    elif tipo == 'capacidade':
                        lista_capacidades_respostas_usuario.append(tag)

# RESULTADOS
print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')





# Montando a estrutura do diagnóstico
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
    '. Com isso, ',
    '. Por isso ',
    '. Acaba que ',
    '. Como consequência disso, '
]

# Contabiliza a quantidade que cada tag apareceu
contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)
print(f'Limitadores: {contador_limitadores}')
print(f'Capacidades: {contador_capacidades}')

# Pega apenas os valores dos dicionários contador_ e qual o valor máximo presente
maior_frequencia_limitadores = max(contador_limitadores.values(), default=0)
maior_frequencia_capacidades = max(contador_capacidades.values(), default=0)

# Lista das principais tags. As outras são adicionais e entram como considerações adicionais
limitadores_principais = ['base', 'troca_de_acorde', 'ritmo', 'montagem_de_acorde']
capacidades_principais = ['troca_de_acorde', 'ritmo', 'montagem_de_acorde']

# Cria uma lista com as tags correspondentes aos maiores valores. Ou seja, as tags que mais apareceram na lista
limitadores_mais_frequentes = []
for item, quantidade in contador_limitadores.items():
    if quantidade == maior_frequencia_limitadores and quantidade >= 2 and item in limitadores_principais:  # Aqui eu estou limpando os limitadores que não são principais, pois entram como considerações adicionais mais abaixo.
        limitadores_mais_frequentes.append(item)
capacidades_mais_frequentes = []
for item, quantidade in contador_capacidades.items():
    if quantidade == maior_frequencia_capacidades and quantidade >= 2 and item in capacidades_principais: # Mesma coisa das considerações adicionais mas agora com capacidades.
        capacidades_mais_frequentes.append(item)

#Outro jeito de fazer o passo anterior - Resgatar apenas os itens de maior frequência na lista de limitadores e capacidades
# limitadores_mais_frequentes_alternativa = [item for item, quantidade in contador_limitadores.items() if quantidade == maior_frequencia_limitadores]
# print(limitadores_mais_frequentes_alternativa)
# capacidades_mais_frequentes_alternativa = [item for item, quantidade in contador_capacidades.items() if quantidade == maior_frequencia_capacidades]
# print(capacidades_mais_frequentes_alternativa)

#Mostra os itens mais frequentes de cada lista - Apenas para conferência
print(f'O item mais frequente em limitadores é {limitadores_mais_frequentes}')
print(f'O item mais frequente em capacidades é {capacidades_mais_frequentes}')

# Definindo se iniciante, intermediário ou avançado baseado na diferença da quantidade de tags entre limitadores e capacidades
nivel = ''
if (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) >= 2:
        nivel = 'iniciante'
elif abs(len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= 1:
        nivel = 'intermediario'
elif (len(lista_limitadores_respostas_usuario) - len(lista_capacidades_respostas_usuario)) <= -2:
        nivel = 'avancado'

# Diagnóstico final
print()
print('=' * 100)
print(f'{"DIAGNÓSTICO FINAL":^100}')
print('=' * 100)
print()


# indicadores que irão alterar os inícios e conectores de frases
conectores_cap_contador = 0
conectores_lim_contador = 0
alterar_lista = True

# o que eu quero é: se não tiver aparecido nenhuma capacidade, ele começa as limitações com 'você ainda não consegue fazer tal coisa'. Continuando aqui,
# o próximo item da lista não pode ser 'por outro lado você...', senão parece que vou falar sobre as capacidades agora. Sendo assim o próximo item da lista
# teria que ser 'além disso, você', ou seja, pula o 'por outro lado você'. Agora se já tiver aparecido capacidades no diagnóstico, a primeira frase das limitações
# deve começar com 'por outro lado você', justamente para dar a entender que agora vêm limitações. E a partir daí segue a lista normal de conectores_lim




# Diagnóstico baseado em perfis
perfil = ''
for tipo, descricao in perfis.items():
    if descricao['capacidades'] == set(capacidades_mais_frequentes) and descricao['limitadores'] == set(limitadores_mais_frequentes):
        perfil = tipo
        print('\n1 - PERFIS ----------------\n')
        print(descricao['descricao'])   # Exemplo: 'Você já é um guitarrista bem equilibrado, capaz de tocar várias músicas com fluidez.'
        conectores_cap_contador += 1


# Considerações adicionais
print('\n3 - CONSIDERAÇÕES ADICIONAIS PARTE 1------------------\n')
if 'resistencia' in lista_capacidades_respostas_usuario:
    print(conectores_cap[min(conectores_cap_contador, len(conectores_cap) - 1)], end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_positivo"]}.')
    conectores_cap_contador += 1
if 'continuidade' in lista_capacidades_respostas_usuario:
    print(conectores_cap[min(conectores_cap_contador, len(conectores_cap) - 1)], end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_positivo"]}.')
    conectores_cap_contador += 1




# Caso não se encaixe em nenhum perfil
print('\n2 - DIAGNÓSTICOS ISOLADOS -----------------------\n')
if perfil == '':
    for capacidade in capacidades_mais_frequentes:
        print(conectores_cap[min(conectores_cap_contador, len(conectores_cap) - 1)], end='')
        print(f'{lista_diagnostico[capacidade]["descricao_capacidade"]}{choice(conectores_causa_efeito)}{lista_diagnostico[capacidade]["efeito_positivo"]}.')
        conectores_cap_contador += 1
    # alterando a lista de prefixos da lista conectores_lim após ter passado todas as capacidades
    if alterar_lista:
        conectores_lim = conectores_lim_original.copy()
        if conectores_cap_contador == 0:  # Consegui simplificar bastante o uso dos conectores limitadores apenas tirando o conector certo dependendo se já foram mostradas capacidades ou não
            conectores_lim.pop(1)
            alterar_lista = False
        else:
            conectores_lim.pop(0)
            alterar_lista = False
    #frase combinação e causa/efeito
    if 'montagem_de_acorde' in limitadores_mais_frequentes and 'troca_de_acorde' in limitadores_mais_frequentes:
        print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
        print('está consolidando a montagem dos acordes, o que impacta diretamente na velocidade de troca. A dificuldade na troca vem da montagem dos acordes ainda não estar automática.')
        conectores_lim_contador += 1
    elif 'montagem_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
        print('tem dificuldade na montagem dos acordes e isso acaba interferindo no seu ritmo.')
        conectores_lim_contador += 1
    elif 'troca_de_acorde' in limitadores_mais_frequentes and 'ritmo' in limitadores_mais_frequentes:
        print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
        print('tem dificuldade tanto na troca de acordes quanto em manter o ritmo, o que faz você se perder facilmente nas músicas. Você perde o ritmo pois ainda tem dificuldades na troca de acordes.')
        conectores_lim_contador += 1
    else:
        for limitador in limitadores_mais_frequentes:
            print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
            print(f'{lista_diagnostico[limitador]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico[limitador]["efeito_negativo"]}.')
            conectores_lim_contador += 1

# Se não passar pelo bloco 2 - diagnósticos isolados (perfil != '') trocamos os prefixos da lista conectores_lim aqui
if alterar_lista:
    conectores_lim = conectores_lim_original.copy()
    if conectores_cap_contador == 0:  # Consegui simplificar bastante o uso dos conectores limitadores apenas tirando o conector certo dependendo se já foram mostradas capacidades ou não
        conectores_lim.pop(1)
        alterar_lista = False
    else:
        conectores_lim.pop(0)
        alterar_lista = False

# Considerações adicionais
print('\n3 - CONSIDERAÇÕES ADICIONAIS PARTE 2------------------\n')
if 'resistencia' in lista_limitadores_respostas_usuario:
    print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
    print(f'{lista_diagnostico["resistencia"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["resistencia"]["efeito_negativo"]}.')
    conectores_lim_contador += 1
if 'nao_consegue_pestana' in lista_limitadores_respostas_usuario:
    print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
    print(f'{lista_diagnostico["nao_consegue_pestana"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["nao_consegue_pestana"]["efeito_negativo"]}.')
    conectores_lim_contador += 1
if 'continuidade' in lista_limitadores_respostas_usuario:
    print(conectores_lim[min(conectores_lim_contador, len(conectores_lim) - 1)], end='')
    print(f'{lista_diagnostico["continuidade"]["descricao_limitacao"]}{choice(conectores_causa_efeito)}{lista_diagnostico["continuidade"]["efeito_negativo"]}.')
    conectores_lim_contador += 1




# Diagnóstico do nível
print('\n4 - NÍVEL ------------\n')
print('Considerando seus pontos fortes e limitações, você se encontra no seguinte estágio:')
print(choice(lista_nivel[nivel]))
'''
