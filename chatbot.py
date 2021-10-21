import json
import random
import printf
import ficha
import menu
import learn
import tratamento
import time
import os
import sys


# Classe que defina o chatbot
class Chatbot:

    def __init__(self, name, novo):
        # Nome do bot é salvo com e sem tratamento
        self.name_bot = name
        self.name_bot_trat = tratamento.trata_key(name)

        # Atributos em array para o bot entender quando é sim e não mais facilmente
        self.lista_sim = ['Sim', 'SIM', 's', 'S', 'YES', 'yes', 'Y', 'y', 'SI', 'si', 'sim', 'SiM', 'siM', 'sIm', 'Yes']
        self.lista_nao = ['Nao', 'NAO', 'n', 'N', 'NO', 'no', 'NÃO', 'Não', 'não', 'nao', 'NaO', 'naO', 'nAo', 'NãO','nãO', 'nÃo']

        if novo[0] in self.lista_nao or novo[0:2] in self.lista_nao or novo[0:3] in self.lista_nao:
            self.novo_bot = 'N'
        elif novo[0] in self.lista_sim or novo[0:2] in self.lista_sim or novo[0:3] in self.lista_sim:
            self.novo_bot = 'S'
        else:
            self.novo_bot = 'S'

        # Confere se diretorios do bot existem
        if not os.path.exists('bots_files/' + self.name_bot_trat):
            if self.novo_bot == 'N':
                sys.exit('[ ERRO - Bot não foi encontrado ]')
            else:
                os.makedirs('bots_files/' + self.name_bot_trat)

        # Confere se diretorio do bot que guarda info prontas existe
        if not os.path.exists('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas'):
            os.makedirs('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas')

        # Confere se diretorio do bot que guarda info prontas existe
        if not os.path.exists('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado'):
            os.makedirs('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado')

        # Abre arquivo .json com nomes conhecidos do bot para leitura
        try:
            memoria_conhecidos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_conhecidos.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico do bot, ele criado e posto para leitura
            memoria_conhecidos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_conhecidos.json','w')
            memoria_conhecidos.write('["Fabio Lucas"]')
            memoria_conhecidos.close()
            memoria_conhecidos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_conhecidos.json','r')
        # Array de atributos do bot salva os nomes conecidos
        self.conhecidos = json.load(memoria_conhecidos)
        memoria_conhecidos.close()

        # Abre arquivo txt para escrever oq o bot não soube respoder
        not_know = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_not_know.txt','a')
        not_know.close()

        # Atributo para ensinar bot, iniciada com S
        self.ensinar = "S"

        # Atributos em array para o bot entender quando o usuario está se despedindo
        self.lista_despedida = ['Tchau', 'TCHAU', 'tchau', 'Adeus', 'ADEUS', 'adeus', 'Bye', 'BYE', 'bye']

        # Para salvar ultimas frases ditas ao bot e responder
        self.ultimas_frases = ['0', '1', '2']

        # Abre arquivo .json com nomes de pessoas que podem editar o bot
        try:
            memoria_security = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_security.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico do bot, ele criado e posto para leitura
            memoria_security = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_security.json','w')
            # Definição se o bot pode ser ensinado por todos ou não
            printf.print_color('\n--------------------- Defina quem pode ensinar o bot ---------------------', 'yellow')
            print('>> ', end="")
            printf.print_color('Todos poderão ensinar esse bot? [S/N]: ', 'yellow_end')
            s_n = input()
            if s_n == 'S' or 's' or 'Sim' or 'sim':
                # O bot não é ensinado por todos
                memoria_security.write('["livre"]')
                memoria_security.close()
                memoria_security = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_security.json','r')
            else:
                # Defini qum pode ensinar o bot
                print('>> ', end="")
                printf.print_color('Quantas Pessoas poderão editar o bot de 1 até 3?: ', 'yellow_end')
                resp = input()
                if resp > 3:
                    resp = 3
                if resp < 1:
                    resp = 1
                lista_secur_people = ['fechado', '1', '2', '3']

                for c in range(1, resp):
                    print('>> ', end="")
                    printf.print_color('Nome e Sobrenome da pessoas (Ex. Fabio Silva): ', 'yellow_end')
                    lista_secur_people[c] = input().capitalize()

                memoria_security.write('["' + lista_secur_people[0] + '","' + lista_secur_people[1] + '","' + lista_secur_people[2] + '","' + lista_secur_people[3] + '"]')
                memoria_security.close()
                memoria_security = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_security.json', 'r')
                print('>> ', end="")
                printf.print_color('NOMES LIBERADOS PARA EDIÇÃO: ' + lista_secur_people[1] + '", "' + lista_secur_people[2] + '", "' + lista_secur_people[3], 'yellow')
                print('>> ', end="")
                printf.print_color('SENHA PARA ENSINAR O BOT: ************', 'yellow')
            printf.print_color('------------------------------------------------------------------------', 'yellow')
        # Array salva os nomes de segurança e configs
        self.security = json.load(memoria_security)
        memoria_security.close()

        # Tenta encontrar o aquivo com as info de apresentação do bot para ler ele
        try:
            bots_info = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_info.json', 'r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            bots_info = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_info.json', 'w')
            lista_info = ['0', '1', '2', '3', '4']
            # Loop para pedir ao user as 5 possiveis formas do bot se apresentar
            printf.print_color('\n--------------- 5 frases para o bot dizer ao se apresentar ---------------', 'yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c+1) + '° frase para o seu bot dizer ao se apresentar : ', 'yellow_end')
                resp = input().capitalize()
                lista_info[c] = resp
            printf.print_color('------------------------------------------------------------------------', 'yellow')
            #escrevendo as info no arquivo
            bots_info.write('["'+lista_info[0]+'","'+lista_info[1]+'","'+lista_info[2]+'","'+lista_info[3]+'","'+lista_info[4]+'"]')
            bots_info.close()
            bots_info = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_info.json', 'r')
        # Salvando a informações como atributo do bot
        self.bots_info = json.load(bots_info)
        bots_info.close()

        # Abre ou cria arquivo de frases do bot depois fecha(so para garantir que exite)
        try:
            memoria_frases1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases1.json','r')
            memoria_frases2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases2.json','r')
            memoria_frases3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases3.json','r')
        except FileNotFoundError:
            # Caso arquivo não existe ele pede as 3 respostas basicas de oi para iniciar eles
            printf.print_color('\n-------------- Ensine ao bot 3 formas de responder ao "Oi" --------------', 'yellow')
            memoria_frases1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases1.json','w')
            print('>> ', end="")
            printf.print_color('1° frase para responder a "oi" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_frases1.write('{"OI" : "' + resp + '"}')
            memoria_frases1.close()

            memoria_frases2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases2.json','w')
            print('>> ', end="")
            printf.print_color('2° frase para responder a "oi" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_frases2.write('{"OI" : "' + resp + '"}')
            memoria_frases2.close()

            memoria_frases3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases3.json','w')
            print('>> ', end="")
            printf.print_color('3° frase para responder a "oi" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_frases3.write('{"OI" : "' + resp + '"}')
            memoria_frases3.close()
            memoria_frases1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases1.json','r')
            memoria_frases2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases2.json','r')
            memoria_frases3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases3.json','r')
            printf.print_color('------------------------------------------------------------------------', 'yellow')

        self.frases1 = json.load(memoria_frases1)
        self.frases2 = json.load(memoria_frases2)
        self.frases3 = json.load(memoria_frases3)

        memoria_frases1.close()
        memoria_frases2.close()
        memoria_frases3.close()

        # Abre ou cria arquivo de respostas do bot depois fecha(so para garantir que exite)
        try:
            memoria_perguntas1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas1.json','r')
            memoria_perguntas2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas2.json','r')
            memoria_perguntas3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas3.json','r')
        except FileNotFoundError:
            # Caso arquivo não existe ele pede as 3 respostas basicas da pergunta do nome para iniciar eles
            printf.print_color('\n------- Ensine ao bot 3 formas de responder a pergunta "Qual e o seu nome?" -------','yellow')
            memoria_perguntas1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas1.json','w')
            print('>> ', end="")
            printf.print_color('1° frase para responder a "Qual é o seu nome?" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_perguntas1.write('{"QUALEOSEUNOME?" : "' + resp + '"}')
            memoria_perguntas1.close()

            memoria_perguntas2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas2.json','w')
            print('>> ', end="")
            printf.print_color('2° frase para responder a "Qual é o seu nome?" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_perguntas2.write('{"QUALEOSEUNOME?" : "' + resp + '"}')
            memoria_perguntas2.close()

            memoria_perguntas3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas3.json','w')
            print('>> ', end="")
            printf.print_color('3° frase para responder a "Qual é o seu nome?" : ', 'yellow_end')
            resp = input().capitalize()
            memoria_perguntas3.write('{"QUALEOSEUNOME?" : "' + resp + '"}')
            memoria_perguntas3.close()
            memoria_perguntas1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas1.json','r')
            memoria_perguntas2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas2.json','r')
            memoria_perguntas3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas3.json','r')
            printf.print_color('-------------------------------------------------------------------------------------','yellow')

        self.perguntas1 = json.load(memoria_perguntas1)
        self.perguntas2 = json.load(memoria_perguntas2)
        self.perguntas3 = json.load(memoria_perguntas3)

        memoria_perguntas1.close()
        memoria_perguntas2.close()
        memoria_perguntas3.close()

        # Abre arquivos com os assuntos que o boto irá falar
        try:
            assunto = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_assunto.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            assunto = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_assunto.json','w')
            lista_assunto = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            printf.print_color('\n------------- Escolha 10 assuntos que o bot puxaria na conversa -------------','yellow')
            for c in range(10):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° assunto que o seu bot gostaria de puxar em uma palavra(EX1. Futebol)(EX2. Filme): ','yellow_end')
                lista_assunto[c] = input().capitalize()
            printf.print_color('-----------------------------------------------------------------------------','yellow')
            assunto.write('["' + lista_assunto[0] + '","' + lista_assunto[1] + '","' + lista_assunto[2] + '","' + lista_assunto[3] + '","' + lista_assunto[4] + '","' + lista_assunto[5] + '","' + lista_assunto[6] + '","' +lista_assunto[7] + '","' + lista_assunto[8] + '","' + lista_assunto[9] + '"]')
            assunto.close()
            assunto = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_assunto.json','r')
        self.assunto = json.load(assunto)
        assunto.close()

        # Abre arquivos com as formas que o bot irá puxar os assuntos
        try:
            frase_assuntos = open(
                'bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_frase_assuntos.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            frase_assuntos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_frase_assuntos.json','w')
            lista_frase_assuntos = ['0', '1', '2', '3', '4']
            printf.print_color('\n------------- Escolha 5 frases para encaixar nos assuntos escolhidos -------------','yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° frase para se encaixar com os assuntos escolhidos (EX. "Vamos falar de"): ','yellow_end')
                lista_frase_assuntos[c] = input().capitalize()
            printf.print_color('----------------------------------------------------------------------------------','yellow')
            frase_assuntos.write( '["' + lista_frase_assuntos[0] + '","' + lista_frase_assuntos[1] + '","' + lista_frase_assuntos[2] + '","' + lista_frase_assuntos[3] + '","' + lista_frase_assuntos[4] + '"]')
            frase_assuntos.close()
            frase_assuntos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_no_resp.json','r')
        self.frase_assuntos = json.load(frase_assuntos)
        frase_assuntos.close()

        # Abre arquivo com respostas caso o bot não entende a frase
        try:
            no_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_no_resp.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            no_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_no_resp.json','w')
            lista_no_resp = ['0', '1', '2', '3', '4']
            # Pede as 5 frases em um loop
            printf.print_color('\n------- Ensine 5 frases ao bot para caso ele não entenda oque o usuário disse -------', 'yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° frase, para responder caso o bot não entenda a frase : ', 'yellow_end')
                lista_no_resp[c] = input().capitalize()
            no_resp.write('["' + lista_no_resp[0] + '","' + lista_no_resp[1] + '","' + lista_no_resp[2] + '","' + lista_no_resp[3] + '","' + lista_no_resp[4] + '"]')
            no_resp.close()
            no_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_no_resp.json','r')
            printf.print_color('--------------------------------------------------------------------------------------','yellow')
        # Salva as frases com um atributo
        self.no_resp = json.load(no_resp)
        no_resp.close()

        # Abre arquivo com frases de respostas caso o user digite a mesma coisa
        try:
            repeat_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_repeat_resp.json', 'r')
        except FileNotFoundError:
            #Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            repeat_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_repeat_resp.json', 'w')
            lista_repeat_resp = ['0', '1', '2', '3', '4']
            printf.print_color('\n-------- Ensine 5 frases ao bot caso o usuário fique falando a mesma coisa --------','yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c + 1)+'° frase, para responder caso pessoa fique falando a mesma coisa varias vezes : ', 'yellow_end')
                lista_repeat_resp[c] = input().capitalize()
            repeat_resp.write('["'+lista_repeat_resp[0]+'","'+lista_repeat_resp[1]+'","'+lista_repeat_resp[2]+'","'+lista_repeat_resp[3]+'","'+lista_repeat_resp[4]+'"]')
            repeat_resp.close()
            repeat_resp = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_no_resp.json', 'r')
            printf.print_color('-------------------------------------------------------------------------------------','yellow')
        self.repeat_resp = json.load(repeat_resp)
        repeat_resp.close()

        # Abre o arquivo com respostas para inputs vazios
        try:
            vazio = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_vazio.json', 'r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            vazio = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_vazio.json', 'w')
            lista_vazio = ['0', '1', '2', '3', '4']
            printf.print_color('\n---------- Ensine 5 frases ao bot para caso  o usuário não digite nada ----------','yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c + 1)+'° frase, para responder caso pessoa não digite nada : ', 'yellow_end')
                lista_vazio[c] = input().capitalize()
            vazio.write('["'+lista_vazio[0]+'","'+lista_vazio[1]+'","'+lista_vazio[2]+'","'+lista_vazio[3]+'","'+lista_vazio[4]+'"]')
            vazio.close()
            vazio = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_vazio.json', 'r')
            printf.print_color('--------------------------------------------------------------------------------','yellow')
        self.vazio = json.load(vazio)
        vazio.close()

        # Tenta encontrar o aquivo com as frases de despedida do bot
        try:
            despedida = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_despedida.json', 'r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            despedida = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_despedida.json', 'w')
            lista_despedida = ['0', '1', '2', '3', '4']
            # Loop para pedir ao user as 5 possiveis formas de despedida do bot
            printf.print_color('\n--------------------- 5 frases de despedida do bot ---------------------', 'yellow')
            for c in range(5):
                print('>> ', end="")
                printf.print_color(str(c+1) + '° frase de despedida do bot : ', 'yellow_end')
                resp = input().capitalize()
                lista_despedida[c] = resp
            printf.print_color('------------------------------------------------------------------------', 'yellow')
            # escrevendo as info de despedida no arquivo
            despedida.write('["'+lista_despedida[0]+'","'+lista_despedida[1]+'","'+lista_despedida[2]+'","'+lista_despedida[3]+'","'+lista_despedida[4]+'"]')
            despedida.close()
            despedida = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_despedida.json', 'r')
        # Salvando a informações de despedida do bot
        self.despedida = json.load(despedida)
        despedida.close()

        # Tenta encontrar o aquivo com as frases de resposta para calculos
        try:
            calc = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_calc.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            calc = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_calc.json','w')
            lista_calc = ['0', '1', '2', '3']
            # Loop para pedir ao user as 4 possiveis formas de responder calc do bot
            printf.print_color('\n------------------------ 4 frases para o bot responder cálculos ------------------------', 'yellow')
            for c in range(4):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° frase de resposta de cálculo do bot (Ex. "O resultado da conta é"): ', 'yellow_end')
                resp = input().capitalize()
                lista_calc[c] = resp
            printf.print_color('----------------------------------------------------------------------------------------', 'yellow')
            # escrevendo as frases de calculo no arquivo
            calc.write('["' + lista_calc[0] + '","' + lista_calc[1] + '","' + lista_calc[2] + '","' +lista_calc[3] + '"]')
            calc.close()
            calc = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_calc.json', 'r')
        # Salvando as frases de calculo do bot
        self.calc = json.load(calc)
        calc.close()

        # Tenta encontrar o aquivo com as frases de resposta para afirmações verdadeiras
        try:
            true = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_true.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            true = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_true.json','w')
            lista_true = ['0', '1', '2', '3']
            # Loop para pedir ao user as 4 possiveis formas de responder calc do bot
            printf.print_color('\n--------------------- 4 frases para o bot responder cálculos ---------------------','yellow')
            for c in range(4):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° frase de resposta de afirmações verdadeiras (Ex. "Isso me parece verdade"): ', 'yellow_end')
                resp = input().capitalize()
                lista_true[c] = resp
            printf.print_color('------------------------------------------------------------------------', 'yellow')
            # escrevendo as frases de respostas verdadeiras no arquivo
            true.write('["' + lista_true[0] + '","' + lista_true[1] + '","' + lista_true[2] + '","' + lista_true[3] + '"]')
            true.close()
            true = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_true.json','r')
        # Salvando as frases de respostas de afirmações verdadeiras do bot
        self.true = json.load(true)
        true.close()

        # Tenta encontrar o aquivo com as frases de resposta para afirmações falsas
        try:
            false = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_false.json','r')
        except FileNotFoundError:
            # Caso nao ache esse arquivo especifico de info de bot, ele criado e posto para leitura
            false = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_false.json','w')
            lista_false = ['0', '1', '2', '3']
            # Loop para pedir ao user as 4 possiveis formas de responder frases falsas do bot
            printf.print_color('\n---------------- 4 frases para o bot responder afirmações falsas ----------------','yellow')
            for c in range(4):
                print('>> ', end="")
                printf.print_color(str(c + 1) + '° frase de resposta de afirmações falsas (Ex. "Essa frase me parece falsa"): ','yellow_end')
                resp = input().capitalize()
                lista_false[c] = resp
            printf.print_color('-----------------------------------------------------------------------------------', 'yellow')
            # escrevendo as frases de respostas falsas no arquivo
            false.write('["' + lista_false[0] + '","' + lista_false[1] + '","' + lista_false[2] + '","' + lista_false[3] + '"]')
            false.close()
            false = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_false.json','r')
        # Salvando as frases de respostas de afirmações falsas do bot
        self.false = json.load(false)
        false.close()

    # Parte de aprendizado do bot, onde se pega info e atualiza os JSON
    def learn(self, key):
        ultima = len(key)-1
        # Caso o ultimo caractere seja uma '?', os JSON de perguntas são atualizados
        if key[ultima] == '?':
            # O arquivo learn.py é usado nessa parte
            self.perguntas1[key] = learn.get_resp('1')
            memoria_perguntas1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas1.json', 'w')
            json.dump(self.perguntas1, memoria_perguntas1)
            memoria_perguntas1.close()

            self.perguntas2[key] = learn.get_resp('2')
            memoria_perguntas2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas2.json', 'w')
            json.dump(self.perguntas2, memoria_perguntas2)
            memoria_perguntas2.close()

            self.perguntas3[key] = learn.get_resp('3')
            memoria_perguntas3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas3.json', 'w')
            json.dump(self.perguntas3, memoria_perguntas3)
            memoria_perguntas3.close()
        # Caso o ultimo caractere não seja uma '?', os JSON de frases são atualizados
        else:
            # O arquivo learn.py é usado nessa parte
            self.frases1[key] = learn.get_resp('1')
            memoria_frases1 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases1.json', 'w')
            json.dump(self.frases1, memoria_frases1)
            memoria_frases1.close()

            self.frases2[key] = learn.get_resp('2')
            memoria_frases2 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases2.json', 'w')
            json.dump(self.frases2, memoria_frases2)
            memoria_frases2.close()

            self.frases3[key] = learn.get_resp('3')
            memoria_frases3 = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases3.json', 'w')
            json.dump(self.frases3, memoria_frases3)
            memoria_frases3.close()

    # Função de menu, para ensinar e pedir ajuda
    def menu(self, frase , nome_completo):
        # Comando usado para ensinar o bot mais rapidamente
        if frase == '~LEARN':
            if self.security[0] == 'livre' or nome_completo == self.security[1] or nome_completo == self.security[2] or nome_completo == self.security[3]:
                key = menu.command_learn()
                self.learn(key)
                return 'Então vamos continuar a conversa.'
            else:
                return 'Acho que você não tem autorizção para editar esse bot.'

        # Comando usado para pedir ajuda nos comandos e infos
        elif frase == '~HELP':
            menu.command_help()
            return 'Esses são os camndos atuais'
        # Caso o comando não seja entendido
        else:
            menu.command_erro()
            return 'Vamos continuar de onde paramos então.'

    def ficha(self):
        # Mostra uma ficha simples para user no inicio
        ficha.abertura()
        nome = ficha.nome()
        sobrenome = ficha.sobrenome()
        nome_completo = nome + ' ' + sobrenome

        # Pergunta se quer ensinar o bot, caso possa
        if self.security[0] == 'livre' or nome_completo == self.security[1] or nome_completo == self.security[2] or nome_completo == self.security[3]:
            printf.print_color('QUER ENSINAR O BOT SEMPRE NA CONVERSA [S/N]: ', 'yellow_end')
            ensinar = input()
            if ensinar[0:1].upper() in self.lista_nao or ensinar[0:2].upper() in self.lista_na:
                ensinar = 'N'
            else:
                ensinar = 'S'
            self.ensinar = ensinar

        ficha.fechamento()

        escolha = random.randint(0, 3)
        self.fala(self.bots_info[escolha])

        if nome_completo in self.conhecidos:
            self.fala('Fico feliz em te ver denovo ' + nome_completo)
        else:
            self.fala('Muito prazer ' + nome_completo)

            self.conhecidos.append(nome_completo)
            memoria_conhecidos = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_conhecidos.json', 'w')
            json.dump(self.conhecidos, memoria_conhecidos)
            memoria_conhecidos.close()

        return nome

    # Função que recebe os inputs do user
    def escuta(self, user_name):
        print()
        printf.print_color(user_name+': ', 'green')
        frase = input()
        print()
        # Caso o input seja vazio e retornado '--vazio--'
        if frase == '' or frase == ' ':
            return "--vazio--"
        return frase

    # Função onde o bot analisa a frase de input e retorna resposta
    def pensa(self, frase_original, user_name):

        frase = tratamento.trata_key(frase_original)
        frase = tratamento.trata_vogal(frase)
        frase = tratamento.trata_consoante(frase)

        self.ultimas_frases[0] = self.ultimas_frases[1]
        self.ultimas_frases[1] = self.ultimas_frases[2]
        self.ultimas_frases[2] = frase

        # Se as ultimas 3 frases forem iguais
        if self.ultimas_frases[2] == self.ultimas_frases[1]:
            if self.ultimas_frases[1] == self.ultimas_frases[0]:
                # Se defini se o bot dira que está repetindo ou puxará outro assunto
                escolha = random.randint(0, 3)
                if escolha == 0:
                    escolha = random.randint(0, 4)
                    frase1 = self.frase_assuntos[escolha]
                    escolha = random.randint(0, 9)
                    frase2 = self.assunto[escolha]

                    return frase1 + ' ' + frase2
                else:
                    escolha = random.randint(0, 4)
                    return self.repeat_resp[escolha]

        # Caso o input seja o vazio
        if frase == '--vazio--':
            # Se defini se o bot dira que está vazio ou puxará outro assunto
            escolha = random.randint(0, 3)
            if escolha == 0:
                escolha = random.randint(0, 4)
                frase1 = self.frase_assuntos[escolha]
                escolha = random.randint(0, 9)
                frase2 = self.assunto[escolha]

                return frase1 + ' ' + frase2
            else:
                escolha = random.randint(0, 4)
                return self.vazio[escolha]

        # Se defini a posição do ultimo caractere e é escolhido um numero de 1 a 3
        ultima = len(frase)-1
        choice = random.randint(1, 3)

        # Se fatia a frase
        inicio_frase4 = frase[0:4].upper()
        inicio_frase5 = frase[0:5].upper()
        inicio_frase6 = frase[0:6].upper()
        inicio_frase7 = frase[0:7].upper()

        # Array de pronomes relativos é definido
        pronome_relativos = ['QUAL', 'QUEM', 'ONDE', 'QUAIS', 'AONDE', 'QUANTO', 'QUANTA', 'QUANTOS', 'QUANTAS']

        # Analisa se a frase foi uma pergunta sem '?', se for, ele é acrescentado
        if frase[ultima] != '?':
            if inicio_frase4 in pronome_relativos or inicio_frase5 in pronome_relativos or inicio_frase6 in pronome_relativos or inicio_frase7 in pronome_relativos:
                printf.print_color(self.name_bot + ': ', 'purple')
                printf.print_color('Isso foi uma pergunta?', 'blue')
                printf.print_color(user_name + ': ', 'green')
                resp_pronome = input().upper()
                if resp_pronome in self.lista_sim:
                    frase = frase + '?'
                    ultima = ultima + 1
                    printf.print_color(self.name_bot + ': ', 'purple')
                    printf.print_color('Então, falando respondendo ela...', 'blue')

        # Um dos arquivos de resposta é escolhido com base na var choice
        if choice == 1:
            if frase[ultima] == '?':
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas1.json', 'r')
            else:
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases1.json', 'r')
        elif choice == 2:
            if frase[ultima] == '?':
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas2.json', 'r')
            else:
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases2.json', 'r')
        else:
            if frase[ultima] == '?':
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_perguntas3.json', 'r')
            else:
                memoria_frases = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_frases3.json', 'r')

        # Frase de resposta é retornada
        frases_resp = json.load(memoria_frases)
        memoria_frases.close()
        if frase in frases_resp:
            return frases_resp[frase]

        # Retorna frase de despedida caso se entenda isso do usuario
        if frase in self.lista_despedida:
            escolha = random.randint(0, 4)
            printf.print_color(self.name_bot + ': ', 'purple')
            printf.print_color(self.despedida[escolha], 'blue')
            return '--despedida--'

        # Caso a primeira letra seja '~' se entra no menu
        if frase[0] == '~':
            frase_return = self.menu(frase, user_name)
            return frase_return

        # Avalia a frase do usuario, se é uma frase de lógica
        try:
            resp = eval(frase)
            if type(resp) == int:
                resp = str(resp)
                escolha = random.randint(0, 3)
                return self.calc[escolha] + ' ' + resp
            elif resp is True:
                escolha = random.randint(0, 3)
                return self.true[escolha]
            elif resp is False:
                escolha = random.randint(0, 3)
                return self.false[escolha]
            else:
                resp = str(resp)
                return resp
        except:
            pass

        #Caso user tenha defino N em ensinar o bot
        if self.ensinar is "N":
            # Abre arquivo txt para escrever oq o bot não soube respoder
            not_know = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_aprendizado/' + self.name_bot_trat + '_not_know.txt', 'a')
            not_know.write(' -> ' + frase_original + '\n')
            not_know.close()

            # Defini se o bot dirá que não entendeu ou se puxará outro assunto
            escolha = random.randint(0, 2)
            if escolha == 0:
                escolha = random.randint(0, 4)
                frase1 = self.frase_assuntos[escolha]
                escolha = random.randint(0, 9)
                frase2 = self.assunto[escolha]

                return frase1 + ' ' + frase2
            else:
                escolha = random.randint(0, 4)
                return self.no_resp[escolha]

        #No ultimo caso, pedi par user ensinar o bot a responder e add no .json caso não N em ensinar
        printf.print_color(self.name_bot + ': ', 'purple')
        printf.print_color('Não entendi oque voce disse', 'blue')
        while True:
            printf.print_color(self.name_bot + ': ', 'purple')
            printf.print_color('Quer me ensinar a responder isso?', 'blue_end')
            s_or_n = input('[S/N]')
            if s_or_n[0].upper() in self.lista_nao or s_or_n[0:1].upper() in self.lista_nao or s_or_n[0:2].upper() in self.lista_nao:
                s_or_n = 'N'
            elif s_or_n[0].upper() in self.lista_sim or s_or_n[0:1].upper() in self.lista_sim or s_or_n[0:2].upper() in self.lista_sim:
                s_or_n = 'S'
            else:
                escolha = random.randint(0, 4)
                printf.print_color(self.no_resp[escolha], 'blue')
                s_or_n = 'N'
            if s_or_n is 'N':
                # Abre arquivo txt para escrever oq o bot não soube respoder
                not_know = open('bots_files/' + self.name_bot_trat + '/' + self.name_bot_trat + '_frases_prontas/' + self.name_bot_trat + '_not_know.txt', 'a')
                not_know.write(' -> ' + frase_original + '\n')
                not_know.close()
                break
            if s_or_n is 'S':
                self.learn(frase)
                return 'Hmmm, vamos continuar então'
            return 'Tente outra coisa então.'

    # Função onde o bot fala com o user
    def fala(self, frase):
        printf.print_color(self.name_bot+': ', 'purple')
        time.sleep(0.4)
        printf.print_color(frase, 'blue')
