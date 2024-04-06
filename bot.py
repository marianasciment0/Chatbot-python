import nltk
from nltk.chat.util import Chat, reflections

saudacoes = [
    [
        r"oi|olá|hey|hello!",
        ["Olá!", "Oi!", "Hey!"]
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é Chatbot.", "Eu sou o Chatbot!"]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado! E você?", "Estou ótimo!"]
    ],
    [
        r"adeus|tchau",
        ["Tchau!", "Até mais!", "Até a próxima!"]
    ]
]

def chatbot():
    print("Olá! Sou o Chatbot. Como posso ajudá-lo hoje?")
    chat = Chat(saudacoes, reflections)
    while True:
        try:
            resposta = chat.respond(input(">> "))
            print(resposta)
        except KeyboardInterrupt:
            break
        
chatbot()
