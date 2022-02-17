import json
from time import sleep
import requests as re


def printinfosfilme(dicionario):
    d = dicionario
    data = f"{d['Released'][0:2]}/{d['Released'][3:6]}/{d['Released'][7:]}"
    print('=' * 76)
    print(f"\033[33mTítulo:\033[m {d['Title']}.\n"
          f"\033[33mData de lançamento:\033[m {data}.\n"
          f"\033[33mGênero:\033[m {d['Genre']}.\n"
          f"\033[33mDiretor:\033[m {d['Director']}.\n"
          f"\033[33mAlguns atores:\033[m {d['Actors']}.\n"
          f"\033[33mPaís:\033[m {d['Country']}.\n"
          f"\033[33mPrêmios:\033[m {d['Awards']}.\n"
          f"\033[33mimdbRating:\033[m {d['imdbRating']}\n"
          f"\033[33mTipo:\033[m {d['Type']}.\n"
          f"\033[33mPoster:\033[m {d['Poster']}.")
    print('=' * 76)


def printinfosfilmes(dicionario):
    d = dicionario["Search"]
    print('=' * 76)
    for filme in d:
        print('')
        print(f"\033[33mTítulo:\033[m {filme['Title']}.\n"
              f"\033[33mAno de lançamento:\033[m {filme['Year']}.\n"
              f"\033[33mTipo:\033[m {filme['Type']}.\n"
              f"\033[33mPoster:\033[m {filme['Poster']}.")
        print('')
    print('=' * 76)


def requisitarfilmes():
    while True:
        nome = str(input('Insira o nome do filme ou série -> ')).strip().replace(' ', '+')
        try:
            link = re.get(f'http://www.omdbapi.com/?apikey=4bac1aa8&s={nome}')
        except Exception as erro:
            print('Foi encontrado um erro na sua requisição. Verifique sua conexão e tente novamente.\n'
                  f'Código de erro: {erro}.')
        else:
            d = json.loads(link.text)
            if d['Response'] == 'False':
                print('\033[31m-\033[m' * 50)
                print('\033[31m Nenhum filme encontrado, digite novamente.\033[m')
                print('\033[31m-\033[m' * 50)
                sleep(1)
            else:
                return d


def requisitarfilme():
    while True:
        nome = str(input('Insira o nome do filme ou série -> ')).strip().replace(' ', '+')
        try:
            link = re.get(f'http://www.omdbapi.com/?apikey=4bac1aa8&t={nome}')
        except Exception as erro:
            print('Foi encontrado um erro na sua requisição. Verifique sua conexão e tente novamente.\n'
                  f'Código de erro: {erro}.')
        else:
            d = json.loads(link.text)
            if d['Response'] == 'False':
                print('\033[31m-\033[m' * 50)
                print('\033[31mFilme não encontrado, digite novamente.\033[m')
                print('\033[31m-\033[m' * 50)
                sleep(1)
            else:
                return d


def menu(*opcoes, tamanho=50):
    print(f"{' MENU '}".center(tamanho, '='))
    for x, op in enumerate(opcoes):
        print(f'[ {x+1} ] -> {op}.')
    print('=' * tamanho)
    while True:
        try:
            escolha = int(input('Insira a sua opção -> '))
        except Exception:
            print('Insira somente números.')
        else:
            if not 1 <= escolha <= len(opcoes):
                print('Insira somente um número do menu de opções.')
            else:
                return escolha
