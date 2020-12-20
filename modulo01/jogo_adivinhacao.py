print("++++++++++++++++++++++++++++++++")
print("Bem vindo ao jogo de adivinhação")
print("++++++++++++++++++++++++++++++++")
print()


n_secreto = 42
n_chances = 10

saida = 'Acabaram as tentativas! O número secreto era >> 42 <<.'

for rodada in range(1, n_chances + 1):
    print(f'rodada {rodada} de {n_chances}')
    chute = int(input("Digite o seu número: "))

    if chute == n_secreto:
        saida = f'Você acertou e ainda sobraram {n_chances} tentativas! O número secreto era >> 42 <<'
        break

    elif chute < n_secreto:
        print('O número secreto é >> maior << do que o seu chute!')
    else:
        print('O número secreto é >> menor << do que o seu chute!')


print(saida)