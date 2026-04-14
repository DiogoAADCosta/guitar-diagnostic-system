'''
======================================================================================================================================================================================================
======================================================================================================================================================================================================
Versão 1 - Aqui o objetivo é construir o motor que vai possibilitar o teste de ser executado. Nessa primeira parte vamos primeiro mostrar as perguntas e alternativas na tela
e depois capturar a resposta do usuário. Cada alternativa tem uma tag associada a ela. Quando o usuário responde, nós guardamos a tag associada e salvamos em uma lista, como
limitador ou capacidade.'''

'''
lista_perguntas = [
    {'pergunta': 'Pergunta 1',
     'respostas':  [{'resposta': 'A', 'tag': ['limitador', 'base']},
                    {'resposta': 'B', 'tag': ['limitador', 'troca_de_acorde']},
                    {'resposta': 'C', 'tag': ['limitador', 'troca_de_acorde']},
                    {'resposta': 'D', 'tag': ['capacidade', 'troca_de_acorde']}
                    ]
    },
    {'pergunta': 'Pergunta 2',
         'respostas':  [{'resposta': 'A', 'tag': ['limitador', 'ritmo']},
                        {'resposta': 'B', 'tag': ['limitador', 'troca_de_acorde']},
                        {'resposta': 'C', 'tag': ['limitador', 'ritmo']},
                        {'resposta': 'D', 'tag': [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']]}
                        ]
    }
]

lista_limitadores_respostas_usuario = []
lista_capacidades_respostas_usuario = []

# Para cada questão na lista de perguntas
for questao in lista_perguntas:
    print()
    # Mostre a pergunta
    print(questao['pergunta'])

    for alternativa in questao['respostas']:
        # Mostre as alternativas
        print(alternativa['resposta'])

    # Capta a resposta do usuário - aqui não estou preocupado com validar a resposta pois na versão final o usuário não digitará. Ele clicará em uma das opções na tela. Será feito provavelmente em JavaScript
    resposta_usuario = input('\nSua Resposta: ').strip().upper()

# Compara a resposta do usuário com as alternativas de cada questão para guardar a tag correspondente daquela alternativa
    for alternativa in questao['respostas']:
        if resposta_usuario == alternativa['resposta']:
            # Varre todos os primeiros termos das tags para ver se são limitadores ou capacidades, para então guardar nas listas de limitadores ou capacidades
            for i in range(0, len(alternativa['tag'])):
                # Lista limitadores
                if alternativa['tag'][i] == 'limitador':
                    lista_limitadores_respostas_usuario.append(alternativa['tag'][1])
                elif alternativa['tag'][i][0] == 'limitador':
                    lista_limitadores_respostas_usuario.append(alternativa['tag'][i][1])

                # Lista capacidades
                if alternativa['tag'][i] == 'capacidade':
                    lista_capacidades_respostas_usuario.append(alternativa['tag'][1])
                elif alternativa['tag'][i][0] == 'capacidade':
                    lista_capacidades_respostas_usuario.append(alternativa['tag'][i][1])


print(f'Lista de Limitadores: {lista_limitadores_respostas_usuario}')
print(f'Lista de Capacidades: {lista_capacidades_respostas_usuario}')
'''
