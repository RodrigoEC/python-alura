import random

dict_niveis = {
    'facil': 10,
    'medio': 5,
    'dificil': 3
}

def adivinhacao():

    print("++++++++++++++++++++++++++++++++++++++++")
    print("+++ Bem vindo ao jogo de adivinhação +++")
    print("++++++++++++++++++++++++++++++++++++++++")
    print()


    nivel = input('Defina o nível (facil, medio ou dificil): ')
    n_chances = dict_niveis[nivel]

    n_secreto = random.randint(1, 101)

    saida = f'Acabaram as tentativas! O número secreto era >> {n_secreto} <<.'
    for rodada in range(1, n_chances + 1):
        print(f'rodada {rodada} de {n_chances}')
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print('Meu amor...eu disse entre 1 e 100, perdesse essa rodada!')
            continue

        if chute == n_secreto:
            saida = f'Você acertou e ainda sobraram {n_chances - rodada} tentativas! O número secreto era >> {n_secreto} <<'
            break

        elif chute < n_secreto:
            print('O número secreto é >> maior << do que o seu chute!')
        else:
            print('O número secreto é >> menor << do que o seu chute!')

    return saida

if __name__ == '__main__':
    print(adivinhacao())