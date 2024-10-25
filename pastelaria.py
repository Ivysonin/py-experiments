# CARDÁPIO
ingrediente1 = "queijo"
ingrediente2 = "frango"
ingrediente3 = "frango com queijo"
ingrediente4 = "pizza"
ingrediente5 = "carne"

# Lista do que vai no pastel
pastel = []

print ("======== Bem-vindo a Pastelaria Nunes ========")
print ("======== Aqui está nosso cardápio: \n")

print ("== Escolha quantos ingredientes preferir ==\n")
print ("1- Queijo")
print ("2- Frango")
print ("3- Frango com Queijo")
print ("4- Pizza")
print ("5- Carne")

while True:
    escolha = input ("Digite de 1 a 5 para escolha, ou digite 'sair' quando terminar de escolher: ".lower())
    if escolha == "sair" :
        print ("Você terminou de escolher !\n")
        break
    elif escolha == "1" :
        if ingrediente1 not in pastel:
            print ("Sabor adicionado, mais algum?\n")
            pastel.append(ingrediente1)
        else:
            print ("Esse sabor você já escolheu, escolha outro !\n")
    elif escolha == "2" :
        if ingrediente2 not in pastel:
            print ("Sabor adicionado, mais algum?\n")
            pastel.append(ingrediente2)
        else:
            print ("Esse sabor você já escolheu, escolha outro !\n")
    elif escolha == "3" :
        if ingrediente3 not in pastel:
            print ("Sabor adicionado, mais algum?\n")
            pastel.append(ingrediente3)
        else:
            print ("Esse sabor você já escolheu, escolha outro !\n")
    elif escolha == "4" :
        if ingrediente4 not in pastel:
            print ("Sabor adicionado, mais algum?\n")
            pastel.append(ingrediente4)
        else:
            print ("Esse sabor você já escolheu, escolha outro !\n")
    elif escolha == "5" :
        if ingrediente5 not in pastel:
            print ("Sabor adicionado, mais algum?\n")
            pastel.append(ingrediente5)
        else:
            print ("Esse sabor você já escolheu, escolha outro !\n")
    else:
        print ("\nVocê está fazendo algo errado, tente de novo\n")

print ("======== Esses são os ingredientes que vão no seu pastel: \n")
for ingrediente in pastel:
    print (f"- {ingrediente}")

print ("\n ======== Obrigado por escolher a Pastelaria Nunes <3 ========")