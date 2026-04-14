# Version 4 - Diagnostic Generation and Conditional Flow
#
# Goal:
# Generate a structured diagnosis based on user responses.
#
# In this version:
# - A diagnosis system is introduced using tag frequency
# - The most frequent limitations and strengths are mapped to predefined messages
# - A diagnostic text is dynamically generated
#
# Additionally:
# - Conditional question flow is introduced using 'skip_if'
# - Some questions are skipped based on previous answers to avoid redundancy
from collections import Counter

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
     'skip_if': 'nao_sabe_pestana',  
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
     'skip_if': 'nao_sabe_pestana',                        
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
                   {'resposta': 'B', 'tag': [['limitador', 'ritmo']], 'texto': 'Preciso parar a música e voltar para uma parte específica para conseguir voltar a tocar junto'},
                   {'resposta': 'C', 'tag': [['limitador', 'ritmo']], 'texto': 'Consigo voltar a tocar com a música sem parar, mas demoro um  pouco esperando uma parte específica'},
                   {'resposta': 'D', 'tag': [['capacidade', 'continuidade']], 'texto': 'Consigo voltar a tocar com a música quase que imediatamente após o erro'}
                   ]
     },
    {'id': 9,
     'pergunta': '9 - O que você acha mais difícil?',     
     'respostas': [{'resposta': 'A', 'tag': [['limitador', 'montagem_de_acorde']], 'texto': 'Montar os acordes e soar limpos'},
                   {'resposta': 'B', 'tag': [['limitador', 'troca_de_acorde']], 'texto': 'Trocas rápidas de acordes'},
                   {'resposta': 'C', 'tag': [['limitador', 'base']], 'texto': 'Ler cifras e tablaturas'},
                   {'resposta': 'D', 'tag': [['capacidade', 'ritmo']], 'texto': 'Tocar junto com a música'}
                   ]
     }
]

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

# Detects if the user lacks fundamental knowledge (barre chord)
# This affects subsequent question flow
nao_sabe_pestana = False


for questao in lista_perguntas:

    # Skip logic:
    # If the user does not know what a barre chord is,
    # some questions are skipped and base limitation is assumed
    if nao_sabe_pestana == True and questao.get('skip_if') == 'nao_sabe_pestana':
        lista_limitadores_respostas_usuario.append('base')
        continue    

    print()
    print(questao['pergunta'])
    print()

    for alternativa in questao['respostas']:
        print(f'{alternativa["resposta"]} - {alternativa["texto"]}')

    # Capture user input
    resposta_usuario = input('\nSua Resposta: ').strip().upper()

    if (questao['id'] == 3 and resposta_usuario == 'A') or (questao['id'] == 5 and resposta_usuario == 'A'):
        nao_sabe_pestana = True


    for alternativa in questao['respostas']:
        if resposta_usuario == alternativa['resposta']:

            for tipo, tag in alternativa['tag']:

                if tipo == 'limitador':
                    lista_limitadores_respostas_usuario.append(tag)

                elif tipo == 'capacidade':
                    lista_capacidades_respostas_usuario.append(tag)

# Collected raw results
print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')





# Diagnostic mapping:
# Each tag is associated with descriptive text used to build the final diagnosis
lista_diagnostico = {
    'montagem_de_acorde': {
        'descricao_capacidade': 'Você já consegue montar acordes com clareza',
        'efeito_positivo': 'Seus acordes soam “limpos”',
        'descricao_limitacao': 'Você ainda tem dificuldade em montar os acordes com clareza',
        'efeito_negativo': 'Algumas cordas saem abafadas e, com isso, os acordes soam “sujos”',
        'recomendacao': 'Foque em montar os acordes sem encostar os dedos em cordas vizinhas, para não abafar cordas que devem soar'
    },
    'troca_de_acorde': {
        'descricao_capacidade': 'Você já consegue trocar acordes com uma boa base de fluidez',
        'efeito_positivo': 'Isso te ajuda muito a manter o ritmo',
        'descricao_limitacao': 'Você ainda tem dificuldade para trocar os acordes',
        'efeito_negativo': 'Isso quebra a fluidez da execução',
        'recomendacao': 'Foque em tentar construir os acordes posicionando todos os dedos ao mesmo tempo'
    },
    'ritmo': {
        'descricao_capacidade': 'Você já consegue manter o ritmo em boa parte do tempo',
        'efeito_positivo': 'Isso te ajuda a tocar músicas do início ao fim sem se perder',
        'descricao_limitacao': 'Você ainda tem dificuldade em manter o ritmo constante',
        'efeito_negativo': 'Isso faz com que a música perca continuidade',
        'recomendacao': 'Foque em tocar músicas sem perder o ritmo. Sacrifique acordes “limpos” neste momento. Se você conseguir se manter no ritmo com acordes “sujos”, o problema realmente é a velocidade na troca de acordes. Senão é um problema de ritmo mais profundo, que deve ser trabalhado desde o zero'
    },
    'resistencia': {
        'descricao_capacidade': 'Você já consegue sustentar acordes com pestana por mais tempo sem perder qualidade',
        'efeito_positivo': 'Isso amplia o leque de músicas que você é capaz de tocar',
        'descricao_limitacao': 'Sua mão ainda não está totalmente preparada para sustentar acordes com pestana por muito tempo',
        'efeito_negativo': 'Isso pode impactar sua consistência dependendo da música',
        'recomendacao': 'Foque em tocar músicas com muitos acordes com pestana. Apenas usando bastante esses acordes você fortalecerá sua mão e será capaz de tocar pestana sem cansar/doer a mão'
    },
    'continuidade': {
        'descricao_capacidade': 'Você já consegue se manter na música mesmo após pequenos erros',
        'efeito_positivo': 'Isso te faz ser capaz de tocar com uma banda',
    },
    'base': {
        'descricao_limitacao': 'Você ainda não domina conceitos básicos do instrumento',
        'efeito_negativo': 'Isso faz com que várias etapas do processo fiquem difíceis',
        'recomendacao': 'Foque ainda em dominar a base. Saber ler cifras, tablaturas, e conceitos básicos te farão conseguir dar o próximo passo com muito mais facilidade'
    },
    'nao_consegue_pestana': {
        'descricao_limitacao': 'Você ainda não consegue fazer acordes com pestana',
        'efeito_negativo': 'Isso limita bastante o seu repertório e te deixa preso a uma única região do braço da guitarra',
        'recomendacao': 'Foque em tentar tocar acordes com pestana, mesmo que não saiam 100%. Apenas assim você vai conseguir dar esse próximo passo'
    },
}


# Count how many times each tag appears
contador_limitadores = Counter(lista_limitadores_respostas_usuario)
contador_capacidades = Counter(lista_capacidades_respostas_usuario)
print(f'Limitadores: {contador_limitadores}')
print(f'Capacidades: {contador_capacidades}')

# Identify the most frequent tag in each list
limitadores_mais_frequentes = contador_limitadores.most_common(1)
capacidades_mais_frequentes = contador_capacidades.most_common(1)

print(f'O item mais frequente em limitadores é {limitadores_mais_frequentes}')
print(f'O item mais frequente em capacidades é {capacidades_mais_frequentes}')

# Extract most frequent tags to map into diagnostic messages
if limitadores_mais_frequentes:
    limitador = limitadores_mais_frequentes[0][0]
else:
    limitador = 'Sem limitador'
if capacidades_mais_frequentes:
    capacidade = capacidades_mais_frequentes[0][0]
else:
    capacidade = 'Sem capacidade'


# Build diagnostic output based on most frequent tags
# Combines strengths and limitations into readable feedback
if limitador == 'Sem limitador' and capacidade != 'Sem capacidade':
    print(f'{lista_diagnostico[capacidade]["descricao_capacidade"]}.')
    print(f'Na prática, {lista_diagnostico[capacidade]["efeito_positivo"].lower()}.')
elif limitador != 'Sem limitador' and capacidade == 'Sem capacidade':
    print(f'{lista_diagnostico[limitador]["descricao_limitacao"]}.')
    print(f'Na prática, {lista_diagnostico[limitador]["efeito_negativo"].lower()}.')
    print(f'{lista_diagnostico[limitador]["recomendacao"]}.')
elif limitador != 'Sem limitador' and capacidade != 'Sem capacidade':
    print(f'{lista_diagnostico[capacidade]["descricao_capacidade"]}. Por conta disso {lista_diagnostico[capacidade]["efeito_positivo"].lower()}.')
    print(f'Porém, {lista_diagnostico[limitador]["descricao_limitacao"].lower()}, e {lista_diagnostico[limitador]["efeito_negativo"].lower()}.')


# Additional signals:
# Some tags trigger extra feedback regardless of frequency
if 'resistencia' in lista_limitadores_respostas_usuario:
    print(f'\n{lista_diagnostico["resistencia"]["descricao_limitacao"]}. {lista_diagnostico["resistencia"]["efeito_negativo"]}')
if 'nao_consegue_pestana' in lista_limitadores_respostas_usuario:
    print(f'\n{lista_diagnostico["nao_consegue_pestana"]["descricao_limitacao"]}. {lista_diagnostico["nao_consegue_pestana"]["efeito_negativo"]}')
if 'resistencia' in lista_capacidades_respostas_usuario:
    print(f'\n{lista_diagnostico["resistencia"]["descricao_capacidade"]}. {lista_diagnostico["resistencia"]["efeito_positivo"]}')
if 'continuidade' in lista_capacidades_respostas_usuario:
    print(f'\n{lista_diagnostico["continuidade"]["descricao_capacidade"]}. {lista_diagnostico["continuidade"]["efeito_positivo"]}')
