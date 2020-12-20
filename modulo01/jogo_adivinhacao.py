print("++++++++++++++++++++++++++++++++")
print("Bem vindo ao jogo de adivinhação")
print("++++++++++++++++++++++++++++++++")

n_secreto = 42
chute = int(input("Digite o seu número: "))

saida = f"Você errou! o número secreto era {n_secreto}"
if n_secreto == chute:
    saida = f"Você acertou!"

print(saida)