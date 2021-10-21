def print_color(frase, color):
    if color == 'purple':
        print('\033[0;35m' + str(frase) + '\033[m', end='')
    elif color == 'blue':
        print('\033[0;34m' + str(frase) + '\033[m')
    elif color == 'blue_end':
        print('\033[0;34m' + str(frase) + '\033[m', end='')
    elif color == 'green':
        print('\033[0;32m' + str(frase) + '\033[m', end='')
    elif color == 'red':
        print('\033[0;31m' + str(frase) + '\033[m')
    elif color == 'yellow_end':
        print('\033[0;33m' + str(frase) + '\033[m', end='')
    elif color == 'yellow':
        print('\033[0;33m' + str(frase) + '\033[m')
    else:
        print(str(frase))
