def calculadora():
    operacao = input("Digite a operação a ser realizada (exemplo: +, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
        print("Resultado da soma é:", resultado)
    elif operacao == '-':
        resultado = num1 - num2
        print("Resultado da subtração é:", resultado)
    elif operacao == '*':
        resultado = num1 * num2
        print("Resultado da multiplicação é:", resultado)
    elif operacao == '/':
        resultado = num1 / num2
        print("Resultado da divisão é:", resultado)
    else:
        print("Operação inválida.")

calculadora()