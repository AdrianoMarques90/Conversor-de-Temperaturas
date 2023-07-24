while True:
    'Desenvolva um algoritmo que permita ao usuário converter uma temperatura para três diferentes unidades: Celsius (°C), Fahrenheit (°F) e Kelvin (K). O programa deve exibir um menu de opções e solicitar ao usuário que escolha a unidade de temperatura de entrada e a unidade de temperatura de saída. Em seguida, deve solicitar o valor da temperatura a ser convertida e exibir o resultado da conversão.'
    print("Escolha uma temperatura em Graus Celsius, Fahrenheit ou Kelvin para converter! ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    temperatura_conv = int(input(" 1-Celsius para Fahrenheit | 2-Celsius para Kelvin | 3-Fahrenheit para Celsius | 4-Fahrenheit para Kelvin | 5-Kelvin para Celsius | 6-Kelvin para Fahrenheit | 7-SAIR: "))
    if temperatura_conv ==7:
        break
    elif temperatura_conv ==1:
        graus_para_conv = float(input("Digite a temperatura em Celsius para ser convertida em Fahrenheit: "))
        valor_convertido = graus_para_conv*(9/5)+32
        print(f" A temperatura de {graus_para_conv} graus Celsius em Fahrenheit é: {valor_convertido}")
    elif temperatura_conv ==2:
        graus_para_conv = float(input("Digite a temperatura em Celsius para ser convertida em Kelvin: "))
        valor_convertido = graus_para_conv+ 273.15
        print(f" A temperatura de {graus_para_conv} graus Celsius em Kelvin é: {valor_convertido}")
    elif temperatura_conv ==3:
        graus_para_conv = float(input("Digite a temperatura em fahrenheit para ser convertida em Celsius: "))
        valor_convertido = (graus_para_conv - 32)* 5/9
        print(f" A temperatura de {graus_para_conv} graus Fahrenheit em Celsius é: {valor_convertido}")
    elif temperatura_conv == 4:
        graus_para_conv = float(input("Digite a temperatura em Fahrenheit para ser convertida em Kelvin: "))
        valor_convertido =  (graus_para_conv+ 459.67) * 5/9
        print(f" A temperatura de {graus_para_conv} graus Fahrenheit em Kelvin é: {valor_convertido}")
    elif temperatura_conv == 5:
        graus_para_conv = float(input("Digite a temperatura em Kelvin para ser convertida em Celsius: "))
        valor_convertido = graus_para_conv - 273.15
        print(f" A temperatura de {graus_para_conv} graus Kelvin em Celsius é: {valor_convertido}")
    elif temperatura_conv ==6:
        graus_para_conv = float(input("Digite a temperatura em Kelvin para ser convertida em Fahrenheit: "))
        valor_convertido = (graus_para_conv* 9/5) - 459.67
        print(f" A temperatura de {graus_para_conv} graus Kelvin em Fahrenheit é: {valor_convertido}")
    else: 
        print("Digite uma opção válida !")