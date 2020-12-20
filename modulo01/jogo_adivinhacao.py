import random

print("++++++++++++++++++++++++++++++++")
print("Bem vindo ao jogo de adivinhação")
print("++++++++++++++++++++++++++++++++")
print()


n_secreto = random.randint(1, 101)
n_chances = 10

saida = 'Acabaram as tentativas! O número secreto era >> 42 <<.'

for rodada in range(1, n_chances + 1):
    print(f'rodada {rodada} de {n_chances}')
    chute = int(input("Digite o seu número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("Meu amor...eu disse entre 1 e 100, perdesse essa rodada!")
        continue

    if chute == n_secreto:
        saida = f'Você acertou e ainda sobraram {n_chances - rodada} tentativas! O número secreto era >> {n_secreto} <<'
        break

    elif chute < n_secreto:
        print('O número secreto é >> maior << do que o seu chute!')
    else:
        print('O número secreto é >> menor << do que o seu chute!')


print(saida)