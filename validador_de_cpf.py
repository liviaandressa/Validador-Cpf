
cpf = input('digite um CPF: ')
novo_cpf = cpf[:-2]

reverso = 10
total = 0

for indice in range(19):
    if indice > 8:
        indice -=9

    total += int (novo_cpf[indice]) * reverso

    reverso -= 1
    if reverso <2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)
        
if cpf == novo_cpf:
    print('CPF válido')
else:
    print('CPF inválido')