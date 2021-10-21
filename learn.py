import printf


def get_resp(n):
    print('>> ', end="")
    printf.print_color('REPOSTA '+n+': ', 'yellow_end')
    resp = input().capitalize()
    return resp