from apilib import *

while True:
    op = menu('Pesquisar por filmes relacionados ao digitado com menos informacoes',
              'Pesquisar por um filme em específico com mais informacoes', tamanho=76)
    if op == 1:
        filmes = requisitarfilmes()
        printinfosfilmes(filmes)
    if op == 2:
        filme = requisitarfilme()
        printinfosfilme(filme)
    while True:
        a = str(input('\033[31m[ o ] Deseja continuar? [Sim ou Não] -> \033[m')).upper().strip()[0]
        if a in 'SN':
            break
    if a == 'N':
        print('\033[31m=' * 76)
        print('ADEUS!'.center(76))
        print('\033[31m=' * 76)
        break
    print('')
