#Incluindo a classe Chatbot do arquivo chatbot.py
from chatbot import Chatbot

#Incluindo aquivo com edições de prints coloridos
from printf import print_color

#Nomeando e inciando o bot (outro nome gera outro novo)
novo = ''
nome = ''
while novo == '':
    print_color('\nVOCÊ DESEJA CRIAR UM BOT NOVO E ENSINÁ-LO DO INICIO? [S/N]: ', 'yellow_end')
    novo = input()
while nome == '':
    print_color('\nDIGITE O NOME DO BOT DESEJADO [bot]: ', 'yellow_end')
    nome = input()
Bot = Chatbot(nome, novo)

#Ficha par pegar dados do usuario
user_name = Bot.ficha()

#Loop de chat até que bot diga frase de despedida
out = False
while out is False:

    frase = Bot.escuta(user_name)

    resp = Bot.pensa(frase, user_name)

    if resp == '--despedida--':
        out = True
    else:
        Bot.fala(resp)

print_color("\n            [END CHAT]", 'red')
