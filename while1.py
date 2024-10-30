maior_num = -999999999

num = int(input("Digite um número ou -1 para sair: "))

while num != -1:
    if num > maior_num:
        maior_num = num
    num = int(input("Digite um número ou -1 para sair: "))

print("O maior número digitado foi", maior_num)