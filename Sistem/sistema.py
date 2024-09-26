from Sistem.biblioteca.arquivo import *
from Sistem.biblioteca.interface import *
from Sistem.biblioteca.moedas import *
from time import sleep
from Sistem.biblioteca.cores import *
from tabulate import tabulate

arqpes = 'clientes.txt'
arqpre = 'preco.txt'

if not arqExiste(arqpes):
    criarArq(arqpes)
if not arqExiste(arqpre):
    criarArq(arqpre)
while True:
    resp = menu(['Produtos', 'Clientes', 'Cadastrar Produtos', 'Cadastrar Cliente', 'Novo Orçamento', 'Sair do Programa'])
    sleep(1.5)
    if resp == 1:
        cabeçalho('Opção 1')
        lerArqpre(arqpre)
    elif resp == 2:
        cabeçalho('Clientes Cadastrados')
        lerArq(arqpes)
    elif resp == 3:
        cabeçalho('Novo cadastro de Produto')
        cognome = str(input('Nome do Produto: '))
        preco = leiaval('Digite o valor do produto: R$')
        codpro = int(input('Digite o código: '))
        cadpro(arqpre, codpro, cognome, preco)
    elif resp == 4:
        cabeçalho('Novo cadastro de Cliente')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        codpes = int(input('Código: '))
        cadpes(arqpes, codpes, nome, idade)
    elif resp == 6:
        cabeçalho('Sair do Sistema... Até logo')
        break
    elif resp == 5:
        cabeçalho('Novo Orçamento')
        print(c["padrão"])
        valor = 0
        while True:
            try:
                pes = lerCli('Insira o código do cliente: ')
            except (ValueError, TypeError):
                print(f'{c["erro"]}ERRO! Digite um valor válido!{c["padrão"]}')
            except:
                print(f'{c["erro"]}Ocorreu um erro! Tente novamente...{c["padrão"]}')
            else:
                cabeçalho(f'Cliente: {pes}')
                break
        while True:
            pro = lerCód('Insira o código do produto: ')
            #print(type(pro))
            #pro = leiaval(pro)
            valor += pro
            cont = str(input('Quer adicionar mais? [S/N] ')).upper()
            if cont == 'N':
                print('Ok, sem mais produtos')
                print(f'O valor total ficou {reais(valor)}')
                break
        tabfp = [
            ["Forma de Pagamento", "Código"],
            ["Pix", "1"],
            ["Dinheiro", "2"],
            ["Débito", "3"],
            ["Crédito", "4"]
        ]

        tabelafp = tabulate(tabfp, headers="firstrow", tablefmt="grid")
        print(tabelafp)
        while True:
            try:
                fp = int(input('Qual vai ser a forma de pagamento? '))
            except (ValueError, TypeError):
                print(f'{c["erro"]}ERRO! Digite uma forma de pagamento válida!{c["padrão"]}')
            else:
                sleep(1.5)
                if fp == 1:
                    print(
                        f'{c["pix"]}O valor no pix pode ter desconto de até 15% e fica {desc(valor, 15, True)}{c["padrão"]}'
                        )
                    while True:
                        sleep(1.5)
                        while True:
                            tipdesc = str(input('Vai dar o desconto por porcetagem ou reais? [RS/%] ')).upper()
                            if tipdesc == '%':
                                vd = leiadesc('Digite o desconto que será dado: ')
                                print('Processando!')
                                sleep(1.5)
                                if 0 <= vd <= 15:
                                    print(f'O valor total com o desconto de {vd}% será de {desc(valor, vd, True)}')
                                    break
                                else:
                                    print(f'{c["erro"]}ERRO! Desconto inválido{c["padrão"]}')
                            elif tipdesc == 'RS':
                                vd = leiadesc('Digite o desconto que será dado: ')
                                sleep(0.5)
                                print('Processando...')
                                sleep(0.5)
                                maxdesc = des(valor, 15)
                                if vd > maxdesc:
                                    sleep(0.5)
                                    print(f'{c["erro"]}DESCONTO SUPERIOR AO PERMITIDO! Tente novamente...{c["padrão"]}')
                                elif vd < maxdesc:
                                    sleep(0.5)
                                    print(f'O valor total com desconto de {reais(vd)} será de {descrs(valor, vd, True)}')
                                    break
                        break
                elif fp == 3:
                    print(f'Você escolheu a opção {c["deb"]}DÉBITO!{c["padrão"]}')
                    print(
                        f'Para a função {c["deb"]}DÉBITO{c["padrão"]} é permitido 8% de desconto de ficar em '
                        f'um total de {desc(valor, 8, True)}')
                    while True:
                        vd = leiadesc('Digite o desconto que será dado: ')
                        sleep(1.5)
                        if 0 <= vd <= 8:
                            print(f'O valor total com desconto de {vd}% será de {desc(valor, vd, True)}')
                            break
                        else:
                            print(f'{c["erro"]}ERRO! Desconto inválido!{c["padrão"]}')
                elif fp == 4:
                    if valor < 50:
                        print(f'{c["erro"]}Valor insuficiente! Valor mínimo de parcela R$50,00{c["padrão"]}')
                    else:
                        print(f'Você escolheu a função {c["cre"]}CRÉDITO{c["padrão"]}')
                        sleep(1.5)
                        print(
                            f'Pode ser feito em até {c["cre"]}24{c["padrão"]} parcelas, cada parcela com valor '
                            f'mínimo de {c["cre"]}R$50,00{c["padrão"]}')
                        sleep(1.5)
                        tabeljuros = [
                            ["Quantidade de parcelas", "Juros"],
                            ["1 - 5", "3%"],
                            ["6 - 9", "4%"],
                            ["10 - 13", "5,5%"],
                            ["14 - 18", "6,5"],
                            ["19 - 24", "8%"]
                        ]

                        tabeljuros = tabulate(tabeljuros, headers="firstrow", tablefmt="grid", stralign="center")
                        print(f'{c["cre"]}{tabeljuros}')
                        print(c["padrão"])
                        sleep(1.5)
                        qp = int(input('Quantidade de parcelas: '))
                        vcp = valor / qp
                        sleep(1.5)
                        print('Processando...')
                        sleep(1.5)
                        if vcp < 50:
                            print('Valor por parcela insuficiente! Escolha menos parcelas!')
                        else:
                            if 1 <= qp <= 5:
                                print(
                                    f'O valor final será de {qp} parcelas com valor de {c["cre"]}{formasdepagamento.jur3(valor, qp, 3)}{c["padrão"]} cada')
                                break
                            elif 6 <= qp <= 9:
                                print(
                                    f'O valor final será de {qp} parcelas com valor de {c["cre"]}{formasdepagamento.jur4(valor, qp, 4)}{c["padrão"]} cada')
                                break
                            elif 10 <= qp <= 13:
                                print(
                                    f'O valor final será de {qp} parcelas com valor de {c["cre"]}{formasdepagamento.jur55(valor, qp, 5.5)}{c["padrão"]} cada')
                                break
                            elif 14 <= qp <= 18:
                                print(
                                    f'O valor final será de {qp} parcelas com valor de {c["cre"]}{formasdepagamento.jur65(valor, qp, 6.5)}{c["padrão"]} cada')
                                break
                            elif 19 <= qp <= 24:
                                print(
                                    f'O valor final será de {qp} parcelas com valor de {c["cre"]}{formasdepagamento.jur8(valor, qp, 8)}{c["padrão"]} cada')
                                break
            break
        print(f'{c["cre"]}Orçamento Finalizado! Volte Sempre{c["padrão"]}')

    else:
        print('\033[31mERRO! Insira uma opção válida!\033[m')
