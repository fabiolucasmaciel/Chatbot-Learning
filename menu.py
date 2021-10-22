import printf


def command_learn():
    print('>> ', end='')
    printf.print_color('CHAVE: ', 'yellow_end')
    key = input().upper().strip()
    return key


def command_help():
    printf.print_color('-' * 25, 'yellow_end')
    printf.print_color(' HELP ', 'yellow_end')
    printf.print_color('-' * 25, 'yellow')

    printf.print_color(' ~learn : Usado para ensinar o bot a responder coisa. ', 'yellow')
    printf.print_color(' ~help : Usado para ver os comandos disponiveis. ', 'yellow')

    printf.print_color('-' * 56, 'yellow')


def command_erro():
    printf.print_color('\n[COMANDO NAO ENTENDIDO]', 'red')
    printf.print_color('\n[ESCREVA ~help PARA AJUDA]\n', 'red')