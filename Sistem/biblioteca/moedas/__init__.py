from Sistem.biblioteca.cores import *


def reais(n):
    r = f'R${n:>.2f}'.replace('.', ',')
    return r


def desc(p, t, form=False):
    r = p - (p*t/100)
    return r if form is False else reais(r)


def des(p, t):
    r = p*t/100
    return r


def descrs(p, d, form=False):
    r = p - d
    return r if form is False else reais(r)


def leiaval(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! \"{entrada}\" é um preço inválido')
        else:
            valido == True
            return float(entrada)


def leiapre(msg):
    valido = False
    while not valido:
        entrada = str(msg)
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! \"{entrada}\" é um preço inválido')
        else:
            valido == True
            return float(entrada)


def leiadesc(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! \"{entrada}\" é um desconto inválido')
        else:
            valido == True
            return float(entrada)


def leiadescrs(msg):
    valido = False
    while not valido:
        entrada = float(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'{c["erro"]}ERRO! \"{entrada}\" é um desconto inválido')
        else:
            valido == True
            return float(entrada)