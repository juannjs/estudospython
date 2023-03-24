# Função para adição
def adc(x, y):
    return x + y

# Função para subtração
def sub(x, y):
    return x - y

# Função para multiplicação
def multi(x, y):
    return x * y

# Função para divisão
def div(x, y):
    return x / y

print("Bem-vindo à minha calculadora!")

# Loop
while True:
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Selecione a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    resp = input("Digite sua escolha (1/2/3/4): ")

    # Realizar operação de acordo com a escolha do usuário
    if resp == '1':
        print(num1, "+", num2, "=", adc(num1, num2))

    elif resp == '2':
        print(num1, "-", num2, "=", sub(num1, num2))

    elif resp == '3':
        print(num1, "*", num2, "=", multi(num1, num2))

    elif resp == '4':
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            print(num1, "/", num2, "=", div(num1, num2))
    
    else:
        print("Opção inválida! Tente novamente.")
