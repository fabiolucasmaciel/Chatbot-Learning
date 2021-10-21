import printf
import time


def abertura():
    print()
    printf.print_color('-' * 22, 'yellow_end')
    printf.print_color(' FICHA ', 'yellow_end')
    printf.print_color('-' * 22, 'yellow')


def nome():
    nome = ''
    while nome == '':
        printf.print_color('PRIMEIRO NOME: ', 'yellow_end')
        nome = input().capitalize().strip()
    return nome


def sobrenome():
    sobrenome = ''
    while sobrenome == '':
        printf.print_color('SOBRENOME: ', 'yellow_end')
        sobrenome = input().capitalize().strip()
    return sobrenome

def fechamento():
    printf.print_color('[Digite "~help" para ver comandos do bot] ', 'yellow')
    printf.print_color('-' * 50, 'yellow')
    printf.print_color('\n[STARTING CHAT]\n', 'green')
    print()
    time.sleep(1.5)
    print('\n' * 50)

