def cadpes(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{nome},{idade}\n')
        except:
            print('Houve um ERRO no resgistro dos dados')
        else:
            print(f'Novo registro {nome} adicionado')
            a.close()


def cadpod(arq, nome='desconhecido', preço=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{nome},{preço}\n')
        except:
            print('Houve um ERRO no resgistro dos dados')
        else:
            print(f'Novo registro {nome} adicionado')
            a.close()