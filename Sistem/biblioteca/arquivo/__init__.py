from Sistem.biblioteca.interface import *
from Sistem.biblioteca.moedas import *
from Sistem.biblioteca.cores import *
import re


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def cadpes(arq, cad, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{cad},{nome},{idade}\n')
        except:
            print('Houve um ERRO no resgistro dos dados')
        else:
            print(f'Novo registro {nome} adicionado')
            a.close()


def cadpro(arq, cod, nome='não atribuído', preço=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{cod},{nome},{reais(preço)}\n')
        except:
            print('Houve um ERRO no resgistro dos dados')
        else:
            print(f'Registro de {nome} adicionado')
            a.close()


def lerArqpre(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PRODUTOS CADASTRADOS')
        for linha in arq:
            dado = linha.split(',')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<4} - {dado[1]:<23} - {dado[2]:>}')
    finally:
        arq.close()


def lerArq(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(',')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<4} - {dado[1]:<25} - {dado[2]:>2} anos')

    finally:
        arq.close()


def lerCód(cad):
    while True:
        try:
            entrada = int(input(cad))
            arq = open('preco.txt', 'rt')
        except (ValueError, TypeError):
            print(f'{c["erro"]}ERRO! Digite um valor correto. Tente novamente...{c["padrão"]}')
        except:
            print(f'{c["erro"]}ERRO! Tente novamente...')
        else:
            for linha in arq:
                dado = linha.split(',')
                cód = int(dado[0])
                if entrada == cód:
                    val = dado[2]
                    val = re.sub('[R$]', '', val)
                    val = leiapre(val)
                    return val


def lerCli(pes):
    entrada = int(input(pes))
    arq = open('clientes.txt', 'rt')
    for linha in arq:
        dado = linha.split(',')
        cód = int(dado[0])
        if entrada == cód:
            val = dado[1]
            return val


'''def lerCód(cad, nome):
    arq = open(nome, 'rt')
    for linha in arq:
        dado = linha.split(',')
        cód = int(dado[0])
        if cad == cód:
            val = dado[2]
            print(f'{dado[1]} - {val}')'''
