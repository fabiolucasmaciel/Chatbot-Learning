#arquivo para tratar strings mais rapidamente

def trata_key(frase):
    frase = frase.replace(' ', '')
    frase = frase.replace('[', '')
    frase = frase.replace(']', '')
    frase = frase.replace('{', '')
    frase = frase.replace('}', '')
    frase = frase.replace('(', '')
    frase = frase.replace(')', '')
    frase = frase.replace(';', '')
    frase = frase.replace('|', '')
    frase = frase.replace('@', '')
    frase = frase.replace(',', '')
    frase = frase.replace('.', '')
    frase = frase.replace('!', '')
    frase = frase.replace('"', '')
    frase = frase.replace("'", "")
    frase = frase.upper()

    return frase


def trata_vogal(frase):
    if 'AA' in frase or 'AAA' in frase or 'AAAA' in frase or 'AAAAA' in frase or 'AAAAAA' in frase or 'AAAAAAA' in frase or 'AAAAAAAA' in frase or 'AAAAAAAAA'in frase or 'AAAAAAAAAA' in frase or 'AAAAAAAAAAA' in frase:
        frase = frase.replace('AAAAAAAAAAA', 'A')
        frase = frase.replace('AAAAAAAAAA', 'A')
        frase = frase.replace('AAAAAAAAA', 'A')
        frase = frase.replace('AAAAAAAA', 'A')
        frase = frase.replace('AAAAAAA', 'A')
        frase = frase.replace('AAAAAA', 'A')
        frase = frase.replace('AAAAA', 'A')
        frase = frase.replace('AAAA', 'A')
        frase = frase.replace('AAA', 'A')
        frase = frase.replace('AA', 'A')

    if 'EE' in frase or 'EEE' in frase or 'EEEE' in frase or 'EEEEE' in frase or 'EEEEEE' in frase or 'EEEEEEE' in frase or 'EEEEEEEE' in frase or 'EEEEEEEEE' in frase or 'EEEEEEEEEE' in frase or 'EEEEEEEEEEE' in frase:
        frase = frase.replace('EEEEEEEEEEE', 'E')
        frase = frase.replace('EEEEEEEEEE', 'E')
        frase = frase.replace('EEEEEEEEE', 'E')
        frase = frase.replace('EEEEEEEE', 'E')
        frase = frase.replace('EEEEEEE', 'E')
        frase = frase.replace('EEEEEE', 'E')
        frase = frase.replace('EEEEE', 'E')
        frase = frase.replace('EEEE', 'E')
        frase = frase.replace('EEE', 'E')
        frase = frase.replace('EE', 'E')

    if 'II' in frase or 'III' in frase or 'IIII' in frase or 'IIIII' in frase or 'IIIIII' in frase or 'IIIIIII' in frase or 'IIIIIIII' in frase or 'IIIIIIIII' in frase or 'IIIIIIIIII' in frase or 'IIIIIIIIIII' in frase:
        frase = frase.replace('IIIIIIIIIII', 'I')
        frase = frase.replace('IIIIIIIIII', 'I')
        frase = frase.replace('IIIIIIIII', 'I')
        frase = frase.replace('IIIIIIII', 'I')
        frase = frase.replace('IIIIIII', 'I')
        frase = frase.replace('IIIIII', 'I')
        frase = frase.replace('IIIII', 'I')
        frase = frase.replace('IIII', 'I')
        frase = frase.replace('III', 'I')
        frase = frase.replace('II', 'I')

    if 'OO' in frase or 'OOO' in frase or 'OOOO' in frase or 'OOOOO' in frase or 'OOOOOO' in frase or 'OOOOOOO' in frase or 'OOOOOOOO' in frase or 'OOOOOOOOO' in frase or 'OOOOOOOOOO' in frase or 'OOOOOOOOOOO' in frase:
        frase = frase.replace('OOOOOOOOOOO', 'O')
        frase = frase.replace('OOOOOOOOOO', 'O')
        frase = frase.replace('OOOOOOOOO', 'O')
        frase = frase.replace('OOOOOOOO', 'O')
        frase = frase.replace('OOOOOOO', 'O')
        frase = frase.replace('OOOOOO', 'O')
        frase = frase.replace('OOOOO', 'O')
        frase = frase.replace('OOOO', 'O')
        frase = frase.replace('OOO', 'O')
        frase = frase.replace('OO', 'O')

    if 'UU' in frase or  'UUU' in frase or 'UUUU' in frase or 'UUUUU' in frase or 'UUUUUU' in frase or 'UUUUUUU' in frase or 'UUUUUUUU' in frase or 'UUUUUUUUU' in frase or 'UUUUUUUUUU' in frase or 'UUUUUUUUUUU' in frase:
        frase = frase.replace('UUUUUUUUUUU', 'U')
        frase = frase.replace('UUUUUUUUUU', 'U')
        frase = frase.replace('UUUUUUUUU', 'U')
        frase = frase.replace('UUUUUUUU', 'U')
        frase = frase.replace('UUUUUUU', 'U')
        frase = frase.replace('UUUUUU', 'U')
        frase = frase.replace('UUUUU', 'U')
        frase = frase.replace('UUUU', 'U')
        frase = frase.replace('UUU', 'U')
        frase = frase.replace('UU', 'U')

    return frase

def trata_consoante(frase):
    if 'KKK' in frase or 'KKKK' in frase or 'KKKKK' in frase or 'KKKKKK' in frase or 'KKKKKKK' in frase or 'KKKKKKKK' in frase or 'KKKKKKKKK'in frase or 'KKKKKKKKKK' in frase or 'KKKKKKKKKKK' in frase:
        frase = frase.replace('KKKKKKKKKKK', 'K')
        frase = frase.replace('KKKKKKKKKK', 'K')
        frase = frase.replace('KKKKKKKKK', 'K')
        frase = frase.replace('KKKKKKKK', 'K')
        frase = frase.replace('KKKKKKK', 'K')
        frase = frase.replace('KKKKKK', 'K')
        frase = frase.replace('KKKKK', 'K')
        frase = frase.replace('KKKK', 'K')
        frase = frase.replace('KKK', 'K')

    if 'MM' in frase or 'MMM' in frase or 'MMMM' in frase or 'MMMMM' in frase or 'MMMMMM' in frase or 'MMMMMMM' in frase or 'MMMMMMMM' in frase or 'MMMMMMMMM'in frase or 'MMMMMMMMMM' in frase or 'MMMMMMMMMMM' in frase:
        frase = frase.replace('MMMMMMMMMMM', 'M')
        frase = frase.replace('MMMMMMMMMM', 'M')
        frase = frase.replace('MMMMMMMMM', 'M')
        frase = frase.replace('MMMMMMMM', 'M')
        frase = frase.replace('MMMMMMM', 'M')
        frase = frase.replace('MMMMMM', 'M')
        frase = frase.replace('MMMMM', 'M')
        frase = frase.replace('MMMM', 'M')
        frase = frase.replace('MMM', 'M')
        frase = frase.replace('MM', 'M')

    if 'NN' in frase or 'NNN' in frase or 'NNNN' in frase or 'NNNNN' in frase or 'NNNNNN' in frase or 'NNNNNNN' in frase or 'NNNNNNNN' in frase or 'NNNNNNNNN' in frase or 'NNNNNNNNNN' in frase or 'NNNNNNNNNNN' in frase:
        frase = frase.replace('NNNNNNNNNNN', 'N')
        frase = frase.replace('NNNNNNNNNN', 'N')
        frase = frase.replace('NNNNNNNNN', 'N')
        frase = frase.replace('NNNNNNNN', 'N')
        frase = frase.replace('NNNNNNN', 'N')
        frase = frase.replace('NNNNNN', 'N')
        frase = frase.replace('NNNNN', 'N')
        frase = frase.replace('NNNN', 'N')
        frase = frase.replace('NNN', 'N')
        frase = frase.replace('NN', 'N')

    if 'SS' in frase or 'SSS' in frase or 'SSSS' in frase or 'SSSSS' in frase or 'SSSSSS' in frase or 'SSSSSSS' in frase or 'SSSSSSSS' in frase or 'SSSSSSSSS' in frase or 'SSSSSSSSSS' in frase or 'SSSSSSSSSSS' in frase:
        frase = frase.replace('SSSSSSSSSSS', 'S')
        frase = frase.replace('SSSSSSSSSS', 'S')
        frase = frase.replace('SSSSSSSSS', 'S')
        frase = frase.replace('SSSSSSSS', 'S')
        frase = frase.replace('SSSSSSS', 'S')
        frase = frase.replace('SSSSSS', 'S')
        frase = frase.replace('SSSSS', 'S')
        frase = frase.replace('SSSS', 'S')
        frase = frase.replace('SSS', 'S')
        frase = frase.replace('SS', 'S')

    if 'ZZ' in frase or 'ZZZ' in frase or 'ZZZZ' in frase or 'ZZZZZ' in frase or 'ZZZZZZ' in frase or 'ZZZZZZZ' in frase or 'ZZZZZZZZ' in frase or 'ZZZZZZZZZ' in frase or 'ZZZZZZZZZZ' in frase or 'ZZZZZZZZZZZ' in frase:
        frase = frase.replace('ZZZZZZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZZ', 'Z')
        frase = frase.replace('ZZZZZ', 'Z')
        frase = frase.replace('ZZZZ', 'Z')
        frase = frase.replace('ZZZ', 'Z')
        frase = frase.replace('ZZ', 'Z')

    if 'HAH' in frase or 'HAHA' in frase or 'HAHAH' in frase or 'HAHAHA' in frase or 'HAHAHAH' in frase or 'HAHAHAHA' in frase or 'HAHAHAHAH' in frase or 'HAHAHAHAHA' in frase or 'HAHAHAHAHAH' in frase:
        frase = frase.replace('HAHAHAHAHAH', 'HA')
        frase = frase.replace('HAHAHAHAHA', 'HA')
        frase = frase.replace('HAHAHAHAH', 'HA')
        frase = frase.replace('HAHAHAHA', 'HA')
        frase = frase.replace('HAHAHAH', 'HA')
        frase = frase.replace('HAHAHA', 'HA')
        frase = frase.replace('HAHAH', 'HA')
        frase = frase.replace('HAHA', 'HA')
        frase = frase.replace('HAH', 'HA')

    if 'RSR' in frase or 'RSRS' in frase or 'RSRSR' in frase or 'RSRSRS' in frase or 'RSRSRSR' in frase or 'RSRSRSRS' in frase or 'RSRSRSRSR' in frase or 'RSRSRSRSRS' in frase or 'RSRSRSRSRSR' in frase:
        frase = frase.replace('RSRSRSRSRSR', 'RS')
        frase = frase.replace('RSRSRSRSRS', 'RS')
        frase = frase.replace('RSRSRSRSR', 'RS')
        frase = frase.replace('RSRSRSRS', 'RS')
        frase = frase.replace('RSRSRSR', 'RS')
        frase = frase.replace('RSRSRS', 'RS')
        frase = frase.replace('RSRSR', 'RS')
        frase = frase.replace('RSRS', 'RS')
        frase = frase.replace('RSR', 'RS')

    return frase
