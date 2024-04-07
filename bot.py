import nltk
import random
import re
from respostaspadrao import get_respostasPadrao
from questoes import questoes

def chatbot():
    print("Olá! Sou o AdaBot. Para que eu possa te ajudar, a qualquer momento, você pode digitar e enviar o número da questão relacionada a sua dúvida, tá bem?")
    while True:
        entrada = input(">> ")

        saudacoes, despedidas, afirmacao, negacao = get_respostasPadrao()
        if any(re.match(pattern, entrada.lower()) for pattern, respostas in saudacoes):
            for pattern, respostas in saudacoes:
                if re.match(pattern, entrada.lower()):
                    print(random.choice(respostas))
                    break
        elif any(re.match(pattern, entrada.lower()) for pattern, respostas in despedidas):
            for pattern, respostas in despedidas:
                if re.match(pattern, entrada.lower()):
                    print(random.choice(respostas))
                    return
        elif entrada in questoes:
            while True:
                print(questoes[entrada]["mensagem"])
                opcao_selecionada = input(">> ")
                
                if opcao_selecionada in questoes[entrada]["opcoes"]:
                    print(questoes[entrada]["opcoes"][opcao_selecionada])
                    outraDuvida = input("Você tem outra dúvida? (sim/não) ").lower()
                    if any(re.match(pattern, outraDuvida) for pattern in afirmacao):
                        continue
                    else:
                        print("Você pode digitar e enviar o número da questão relacionada a sua dúvida, tá bem?")
                        break
                else:
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        else:
            print("Desculpe, não entendi. Por favor, digite o número de uma questão válida.")

chatbot()