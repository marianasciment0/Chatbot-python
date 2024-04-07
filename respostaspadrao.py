def get_respostasPadrao():
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
    
    despedidas = [
        [
            r"xau|tchau|xauzinho|tiau|encerrar|sair|adeus",
            ["Obrigado por conversar comigo. Qualquer dúvida, estou por aqui. Até mais!"]
        ]
    ]

    afirmacao = [
        r"sim|yes|s|yep|confirmo"
    ]
    
    negacao = [
        r"não|nao|n|nop|no|não confirmo"
    ]
    
    return saudacoes, despedidas, afirmacao, negacao