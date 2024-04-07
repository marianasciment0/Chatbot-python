import nltk
from nltk.chat.util import Chat, reflections
import re
import random


saudacoes = [
    [
        r"oi|olá|ola|oii|e aí",
        ["Olá! Digite e envie o número da questão para que eu possa te ajudar", "Oi! Digite e envie o número da questão para que eu possa te ajudar"]
    ],
    [
        r"qual é o seu nome?|qual o seu nome?|seu nome é?|seu nome",
        ["Eu sou o ADABot, um chatbot feito só para te ajudar!"]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado! E você?", "Estou ótimo!"]
    ]
]

# Dicionário de questões e opções de dúvida
questoes = {
    "5": {
        "mensagem": "Certo! Escolha entre essas opções qual a que corresponde a sua dúvida!\n 1 - Compreensão\n 2 - Variaveis\n 3 - Calculo\n 4 - Outra dúvida",
        "opcoes": {
            "1": "Vamos lá! Primeiramente será necessário calcular o volume da piscina, após isso, descobrir a quantidade de litros da piscina e por último, a quantidade de mls de produto que serão necessários para a piscina.",
            "2": """Precisaremos criar 6 variáveis para resolver esse problema\n
            Cada variável será responsável por alguma coisa, anota aí!\n
                • Uma responsável por armazenar a largura da piscina;\n
                • Outra responsável por armazenar a profundidade da piscina;\n
                • Mais uma será responsável por calcular e armazenar o volume total da água na piscina;\n
                • Mais uma será responsável por fazer a conversão da profundidade da piscina;\n
                • E mais uma que será responsável por calcular e armazenar a quantidade do produto que deve ser adicionada à piscina.""",
            "3": """Agora, entendendo o nosso problema melhor, nós sabemos que precisaremos fazer 3 cálculos principais:\n 
                Volume da piscina: Aqui, nós vamos precisar multiplicar a largura pela altura e depois pelo comprimento. Volume = Largura x Comprimento x Altura.\n
                Quantidade de mililitros: Após descobrirmos o volume da psicina, teremos que  multiplicar esse volume pelo valor recomendado de mililitros de produto por litro de água.\n
                Quantidade de litros da piscina: Ao multiplicarmos o volume da piscina por 1000, obtemos quantos litros são necessários para encher a piscina.""",
            "4": "Digite a sua dúvida que um professor ou monitor irá de ajudar!"
        }
    }
}

def chatbot():
    print("Olá! Sou o AdaBot. Para que eu possa te ajudar, a qualquer momento, você pode digitar e enviar o número da questão relacionada a sua dúvida, tá bem?")
    while True:
        entrada = input(">> ")

        if any(re.match(pattern, entrada.lower()) for pattern, _ in saudacoes):
            for pattern, respostas in saudacoes:
                if re.match(pattern, entrada.lower()):
                    print(random.choice(respostas))
                    break
        elif any(word in entrada.lower() for word in ["adeus", "tchau", "sair"]):
            print("Obrigado por utilizar o ADABot. Espero que tenha gostado. Até mais!")
            break
        elif entrada in questoes:
            print(questoes[entrada]["mensagem"])
            opcao_selecionada = input(">> ")
            
            if opcao_selecionada in questoes[entrada]["opcoes"]:
                print(questoes[entrada]["opcoes"][opcao_selecionada])
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
        else:
            print("Desculpe, não entendi. Por favor, digite o número de uma questão válida.")

chatbot()