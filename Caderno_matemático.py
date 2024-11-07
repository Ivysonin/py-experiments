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

escolhendo_o_que_fazer = input ("\n=== Digite um número (1 a 9) conforme o que você precisa: ").lower()

# CONFORME A ESCOLHA DO USUARIO, EXECUTE

# Tabuada
if escolhendo_o_que_fazer == "1" :
    numero = int(input ("Escolha o número para ver sua tabuada: "))
    contador = 1
    resultado = numero * contador
    while contador <= 10:
        print (f"{numero} x {contador} = {resultado}")
        contador += 1
        resultado = numero * contador
    print ("================")

# Somando
elif escolhendo_o_que_fazer == "2" : 
    print ("=== Escolha dois números para fazer sua soma:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 + num2
    print (f"{num1} + {num2} = {resultado}")
    print ("================")

# Subtrair
elif escolhendo_o_que_fazer == "3" :
    print ("=== Escolha dois números para subtrair:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 - num2
    print (f"{num1} - {num2} = {resultado}")
    print ("================")

# Divisão
elif escolhendo_o_que_fazer == "4" : 
    print ("=== Escolha dois números para dividir, lembre que não podemos dividir nada por 0 !\n")
    num1 = int(input ("Dividendo: "))
    num2 = int(input ("Divisor: ")) 
    resultado = num1 / num2
    print (f"{num1} ÷ {num2} = {resultado}")
    print ("================")

# Multiplicação
elif escolhendo_o_que_fazer == "5" :
    print ("=== Escolha dois números para multiplicar:\n")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    resultado = num1 * num2
    print (f"{num1} x {num2} = {resultado}")
    print ("================")

# Potenciação
elif escolhendo_o_que_fazer == "6" :
    print ("=== Escolha dois números, Um para Você expontenciar e outro para saber se é quadrada,cubica, etcs:\n")
    num1 = int(input ("Digite o que você deseja expontenciar: "))
    num2 = int(input ("Digite quanto vai ser essa expontenciação (2para quadrada, 3 para cubica...): "))
    resultado = num1**num2
    print (f"\n{num1}^{num2} = {resultado}")
    print ("================")

# IMC
elif escolhendo_o_que_fazer == "7" :
    print ("=== Digite seu peso e a altura para saber a Índice de Massa Corporal (IMC):\n")
    peso = float(input ("Digite seu peso: "))
    altura = float(input ("Digite sua altura: "))
    resultado = peso / (altura**2)
    print (f"\nAltura {altura}, peso {peso}, IMC {resultado:.2f}")
    print ("=====================================")

# Transformas °C em °F
elif escolhendo_o_que_fazer == "8" :
    print ("=== Transformando °C em °F:\n")
    graus_celsius = int(input ("Informe a temperatura °C: "))
    f = (graus_celsius * 9/5) + 32
    print (f"{graus_celsius}°C convertido para Fahrenheit, {f}°F")
    print ("==========================================")

# Porcentagem
elif escolhendo_o_que_fazer == "9" :
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
        
# Erro do Usuario
else:
    print ("\n===== Você não está seguindo instruções, Reinie ! =====")
