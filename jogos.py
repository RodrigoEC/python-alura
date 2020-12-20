from modulo01.jogo_adivinhacao import adivinhacao

jogos = {
    '2': adivinhacao
}

print("++++++++++++++++++++++++++++++++++++++++")
print("+++ Bem-vinde ao menu dos jogos!!!!! +++")
print("++++++++++++++++++++++++++++++++++++++++")
print()

print('''
1 - Forca
2 - Adivinhacao
''')

jogo = input('digite o numero do jogo que você quer jogar: ')
try:
    print(jogos[jogo]())
except:
    print("Você selecionou uma opcoção invalida!")