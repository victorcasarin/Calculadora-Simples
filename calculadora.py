# Função para somar
def soma(a, b):
    return a + b


# Função para subtrair
def subtracao(a, b):
    return a - b


# Função para multiplicar
def multiplicacao(a, b):
    return a * b


# Função para dividir
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não permitida."


# Função principal para escolher a operação
def calculadora():

    while True:
        print("CALCULADORA SIMPLES")
        print("Escolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")

        operacao = input("Digite o número da operação desejada (1/2/3/4): ")

        if operacao in '1234':
            break
        else:
            print('OPÇÃO INVÁLIDA. Tente novamente.')


    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == '2':
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == '3':
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == '4':
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida.")


# Chama a função principal
calculadora()
