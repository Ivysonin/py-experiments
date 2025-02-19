# Funções para executar

def tabuada() :
    try:
        numero = int(input ("Escolha o número para ver sua tabuada: "))
        contador = 1
        resultado = numero * contador
        for i in range(10) :
            print (f"{numero} x {contador} = {resultado}")
            contador += 1
            resultado = numero * contador
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError:
        print ("\n===== ERRO: Você não escolheu um número =====")

def somando () :
    try:
        print ("=== Escolha dois números para fazer sua soma:\n")
        num1 = int(input ("Digite um número: "))
        num2 = int(input ("Digite outro número: "))
        resultado = num1 + num2
        print (f"{num1} + {num2} = {resultado}")
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError:
        print ("\n===== ERRO: Você não escolheu um número =====")

def subtrair() :
    try:
        print ("=== Escolha dois números para subtrair:\n")
        num1 = int(input ("Digite um número: "))
        num2 = int(input ("Digite outro número: "))
        resultado = num1 - num2
        print (f"{num1} - {num2} = {resultado}")
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

def divisao() :
    try:
        print ("=== Escolha dois números para dividir, lembre que não podemos dividir nada por 0 !\n")
        num1 = int(input ("Dividendo: "))
        num2 = int(input ("Divisor: ")) 
        resultado = num1 / num2
        print (f"{num1} ÷ {num2} = {resultado}")
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")
    except ZeroDivisionError:
        print ("\n===== Erro: Número não divide por 0 =====")

def multiplicar() :
    try: 
        print ("=== Escolha dois números para multiplicar:\n")
        num1 = int(input ("Digite um número: "))
        num2 = int(input ("Digite outro número: "))
        resultado = num1 * num2
        print (f"{num1} x {num2} = {resultado}")
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

def potencia() :
    try :
        print ("=== Escolha dois números, Um para Você expontenciar e outro para saber se é quadrada,cubica, etcs:\n")
        num1 = int(input ("Digite o que você deseja expontenciar: "))
        num2 = int(input ("Digite quanto vai ser essa expontenciação (2para quadrada, 3 para cubica...): "))
        resultado = num1**num2
        print (f"\n{num1}^{num2} = {resultado}")
        print ("================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

def imc() :
    try :
        print ("=== Digite seu peso e a altura para saber a Índice de Massa Corporal (IMC):\n")
        peso = float(input ("Digite seu peso: "))
        altura = float(input ("Digite sua altura: "))
        resultado = peso / (altura**2)
        print (f"\nAltura {altura}, peso {peso}, IMC {resultado:.2f}")
        print ("=====================================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

def C_para_F() :
    try :
        print ("=== Transformando °C em °F:\n")
        graus_celsius = float(input ("Informe a temperatura °C: "))
        f = (graus_celsius * 9/5) + 32
        print (f"{graus_celsius}°C convertido para Fahrenheit, {f}°F")
        print ("==========================================")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

def porcentagem() :
    try :
        escolha = int(input("Digite '1' para acréscimo ou '2' para desconto: "))
        if escolha == 1 : # Acréscimo
            valor = float(input ("Digite o valor: "))
            porcentagem = float(input ("Digite a porcentagem: "))
            resultado = valor + (valor * porcentagem/100)
            print (f"Atribuindo {porcentagem}% a {valor} = {round(resultado, 2)}")
            print ("==================================")
        elif escolha == 2 : # Desconto
            valor = float(input ("Digite o valor: "))
            porcentagem = float(input ("Digite a porcentagem: "))
            resultado = valor - (valor * porcentagem/100)
            print (f"Diminuindo {porcentagem}% a {valor} = {round(resultado, 2)}")
            print ("================================")  
        else:
            print ("\n===== Siga as instruções =====")
    # Exibindo conforme o usuario não seguir regras(da exeções)
    except KeyboardInterrupt :
        print ("\n===== ERRO: Não digite espaços =====")
    except ValueError :
        print ("\n===== ERRO: Você não escolheu um número =====")

# Organização
print ("========== Bem-vindo ao Caderno Matemático Nunes ==========")
print ("===== Esse caderno foi pensado para você fazer suas atividades de casa(Tarefas da escola) =====\n") 

print ("=== Lista do que temos:\n") 

# Organização para escolhas
print ("1. Tabuada")
print ("2. Somar")
print ("3. Subtrair")
print ("4. Dividir")
print ("5. Multiplicar")
print ("6. Pontenciação")
print ("7. IMC")
print ("8. Transformar °C em °F")
print ("9. Porcentagem")

while True:
    # CONFORME A ESCOLHA DO USUARIO, EXECUTE
    escolhendo_o_que_fazer = input ("\n=== Digite um número 1 a 9 conforme o que você precisa (0 para sair): ").lower()

    # Encerrando o programa
    if escolhendo_o_que_fazer == "0" :
        print ("\n===== Programa encerrado, Te espero no próximo exercício =====\n")
        break
    # Tabuada
    elif escolhendo_o_que_fazer == "1" :
        tabuada()
    # Somando
    elif escolhendo_o_que_fazer == "2" : 
        somando()
    # Subtrair
    elif escolhendo_o_que_fazer == "3" :
        subtrair()
    # Divisão
    elif escolhendo_o_que_fazer == "4" : 
        divisao()
    # Multiplicação
    elif escolhendo_o_que_fazer == "5" :
        multiplicar()
    # Potenciação
    elif escolhendo_o_que_fazer == "6" :
        potencia()
    # IMC
    elif escolhendo_o_que_fazer == "7" :
        imc()
    # Transformas °C em °F
    elif escolhendo_o_que_fazer == "8" :
        C_para_F()
    # Porcentagem
    elif escolhendo_o_que_fazer == "9" :
        porcentagem()
    # Erro do Usuario
    else:
        print ("\n===== Você não está seguindo instruções, tente de novo ! =====")