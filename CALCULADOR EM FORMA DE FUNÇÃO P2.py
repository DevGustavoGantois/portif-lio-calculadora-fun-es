def exponenciacao():
    x = float(input('Primeiro número:'))
    y = float(input('Segundo número:'))
    return "Exponenciação = ", x**y
def divisao():
    x = float(input('Primeiro número:'))
    y = int(input('Segundo número:'))
    return "Divisão = ", x / y
def multiplicacao():
    x = float(input('Primeiro número:'))
    y = float(input('Segundo número:'))
    return "Multiplicação = ", x*y
def subtracao():
    x = float(input('Primeiro número:'))
    y = float(input('Segundo número:'))
    return "Subtração =  ", x - y
def soma():
    x = float(input('Primeiro número:'))
    y = float(input('Segundo número:'))
    return "Soma = ", x + y
opcao = 1

print(' ==============> CALCULADORA DIGITAL <===========================')

while True:
    print('\t 1 - Soma')
    print('\t 2 - Subtração')
    print('\t 3 - Multiplicação')
    print('\t 4 - Divisão')

    opcao = int(input('Quais das opções você deseja escolher:'))

    if opcao == 5:
        print(exponenciacao())
    elif opcao == 4:
        print(divisao())
    elif opcao == 3:
        print(multiplicacao())
    elif opcao == 2:
        print(subtracao())
    elif opcao == 1:
        print(soma())
    elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('O PROGRAMA FOI ENCERRADO.')
        print(' >>>>>> VOLTE SEMPRE <<<<<<<')
        break