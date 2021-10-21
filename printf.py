def print_color(frase, color):
    if color == 'purple':
        print('\033[0;35m' + frase + '\033[m', end='')
    elif color == 'blue':
        print('\033[0;34m' + frase + '\033[m')
    elif color == 'blue_end':
        print('\033[0;34m' + frase + '\033[m', end='')
    elif color == 'green':
        print('\033[0;32m' + frase + '\033[m', end='')
    elif color == 'red':
        print('\033[0;31m' + frase + '\033[m')
    elif color == 'yellow_end':
        print('\033[0;33m' + frase + '\033[m', end='')
    elif color == 'yellow':
        print('\033[0;33m' + frase + '\033[m')
    else:
        print(frase)
