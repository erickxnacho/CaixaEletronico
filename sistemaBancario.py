#Desafio
#criar sistema bancario com tres operaçoes: deposito, saque e ver extrato.

#Todos os depositos devem ser armazenados em uma variavel e exibidos na operação extrato
#O sistema deve permitir realizar 3 saquesss diarios com limite maximo de 500 reais por saque
#Caso o usuario não tenha o saldo em conta os sistema deve informar ao usuario que não é possivel fazer o saque por falta de saldo
#Todos os saque devem ser armazenados na operação extrato
#A operação extrato deve exibir todos os depositos e saque realizados assim como o saldo total da conta

menu ='''

[d]Depoistar
[s]Sacar
[e]Extrato
[q]Sair

=> '''


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3
sacado = depositado = 0
while True:

    opcao = input(menu)

    if opcao == 'd':
        print('deposito')
        deposito = float(input('Valor do deposito: R$'))
        saldo = saldo + deposito
        print(saldo)
        depositado = depositado + deposito

    elif opcao == 's':
        if numero_saques == limite_saques:
            print('Não é possivel realizar a operação, Limite diario de saques já realizados')
        else:
            print('Sacar')
            saque = float(input('Digite o valor do saque: R$'))
            if saque > 500:
                print('Não foi possivel realizar esssa operação, Valor maximo de R$500,00 por saque!')
                
            elif saque > saldo:
                print(f'Não foi possivel realizar esssa operação, Saldo insuficiente! seu saldo total é de {(saldo)}')

            
            else:
                saldo = saldo - saque
                print(f'saque de R${saque} realizado, seu saldo agora é de {saldo}')
                numero_saques = numero_saques + 1
                print(f'saque realizado: {numero_saques}')
                sacado = sacado + saque


            
    elif opcao == 'e':
        print('Extrato')
        print(f'Seu saldo atual é de R${saldo}, foram depositados R${depositado} e sacados R${sacado}')
    elif opcao == 'q':
        break
    else:
        print('Digite uma opcao valida')
    