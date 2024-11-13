# Funções para executar

def tabuada() :
    numero = int(input ("Escolha o número para ver sua tabuada: "))
    contador = 1
    resultado = numero * contador
    for i in range(10) :
        print (f"{numero} x {contador} = {resultado}")
        contador += 1
        resultado = numero * contador
    print ("================")

def somando () :
    print ("=== Escolha dois números para fazer sua soma:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 + num2
    print (f"{num1} + {num2} = {resultado}")
    print ("================")

def subtrair() :
    print ("=== Escolha dois números para subtrair:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 - num2
    print (f"{num1} - {num2} = {resultado}")
    print ("================")

def divisao() :
    try:
        print ("=== Escolha dois números para dividir, lembre que não podemos dividir nada por 0 !\n")
        num1 = int(input ("Dividendo: "))
        num2 = int(input ("Divisor: ")) 
        resultado = num1 / num2
        print (f"{num1} ÷ {num2} = {resultado}")
        print ("================")
    except ZeroDivisionError:
        print ("\n===== Erro: Número não divide por 0 =====")

def multiplicar() :
    print ("=== Escolha dois números para multiplicar:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 * num2
    print (f"{num1} x {num2} = {resultado}")
    print ("================")

def potencia() :
    print ("=== Escolha dois números, Um para Você expontenciar e outro para saber se é quadrada,cubica, etcs:\n")
    num1 = int(input ("Digite o que você deseja expontenciar: "))
    num2 = int(input ("Digite quanto vai ser essa expontenciação (2para quadrada, 3 para cubica...): "))
    resultado = num1**num2
    print (f"\n{num1}^{num2} = {resultado}")
    print ("================")    

def imc() :
    print ("=== Digite seu peso e a altura para saber a Índice de Massa Corporal (IMC):\n")
    peso = float(input ("Digite seu peso: "))
    altura = float(input ("Digite sua altura: "))
    resultado = peso / (altura**2)
    print (f"\nAltura {altura}, peso {peso}, IMC {resultado:.2f}")
    print ("=====================================")

def C_para_F() :
    print ("=== Transformando °C em °F:\n")
    graus_celsius = int(input ("Informe a temperatura °C: "))
    f = (graus_celsius * 9/5) + 32
    print (f"{graus_celsius}°C convertido para Fahrenheit, {f}°F")
    print ("==========================================")

def porcentagem() :
    escolha = input("Primeiro escolha se é um acréscimo(1) ou desconto(2): ")
    if escolha == "1" : # Acréscimo
        valor = int(input ("Digite o valor: "))
        porcentagem = int(input ("Digite a porcentagem: "))
        resultado = valor + (valor * porcentagem/100)
        print (f"Atribuindo {porcentagem}% a {valor} = {resultado}")
        print ("==================================")
    else: # Desconto
        valor = int(input ("Digite o valor: "))
        porcentagem = int(input ("Digite a porcentagem: "))
        resultado = valor - (valor * porcentagem/100)
        print (f"Diminuindo {porcentagem}% a {valor} = {resultado}")
        print ("================================")

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
        print ("\n===== Programa encerrado =====\n")
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