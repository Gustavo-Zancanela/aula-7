impar = 0
par = 0

num = int(input("Digite um número ou 0 para sair: "))

while num != 0:
    if num % 2 == 1:
        impar += 1
    else:
        par += 1 
    num = int(input("Digite um número ou 0 para sair: "))

print("Quantidade de números pares digitados:", par)
print("Quantidade de números ímpares digitados:", impar)
