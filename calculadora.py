# Calculadora em Python

nome = input("Qual seu nome?")
print("Podemos começar!")
print("Irei lhe pedir alguns números e mostrar as operações aritméticas.")

while True:  # Este vai ser o loop
    # Pedido de números
    Numero1 = int(input("Digite seu primeiro numero: "))
    Numero2 = int(input("Digite seu segundo numero: "))

    # Essas são nossas operações
    soma = Numero1 + Numero2
    subtracao = Numero1 - Numero2
    multiplicacao = Numero1 * Numero2
    if Numero2 != 0:
        divisao = Numero1 / Numero2
    else:
        divisao = "indefinida"

    # Solicitar a operação
    operacao = input("Qual operação deseja fazer? soma, subtração, multiplicação, divisao: ").lower()

    # Execução de operação
    if operacao == "soma":
        print(f"O Resultado da soma é {soma}")
    elif operacao == "subtracao":
        print(f"O Resultado da subtração é {subtracao}")
    elif operacao == "multiplicacao":
        print(f"O resultado da multiplicação é {multiplicacao}")
    elif operacao == "divisao":
        if Numero2 != 0:
            print(f"O Resultado da divisão é {divisao}")
        else:
            print("Erro: Não é possível dividir por zero.")
    else:
        print("Operação inválida")

    # O usuário deseja continuar?
    continuar = input("Deseja continuar? (sim/não): ").lower()
    if continuar != "sim":
        print("Obrigado por usar a calculadora. Até a próxima!")
        break
