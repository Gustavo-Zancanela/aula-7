print("+" + 16 * "-" + "+")
print(("|" + "  " + "Bem vindo!!!" + "  " + "|\n"), end="")
print(("|" + "Adivinhe a senha" + "|\n"), end="")
print("+" + 16 * "-" + "+")
print()
print()

senha = 777
tentativa = int(input("Digite a senha correta: "))

while senha != tentativa:
    print("hahaha! você está preso em um loop!")
    tentativa = int(input("Digite a senha correta: "))
print("Muito bem! Está livre do loop")
