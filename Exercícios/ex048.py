soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont += 1
        soma += num
print('A soma de todos os {} valores resultou em {}'.format(cont, soma))
