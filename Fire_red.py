import random

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

print (f"{cor_ciano}========== Luta Mewtwo =========={reset_cor}") # Organização

# Lista pokémons
print (f"{cor_ciano}\n===== Pokémon ====={reset_cor}")
print ("1- Charizard")
print ("2- Lapras")
print ("3- Dragonite")
print ("4- Raichu")
print ("5- Alakazam")
print ("6- Rayquaza")

# Pokémons
pokemon =  input (f"{cor_ciano}Escolha um pokémon de 1 a 6: {reset_cor}")
mewtwo = "mewtwo"

# Vidas
vida_pokemon = 500
vida_mewtwo = 1000

rodada = 1

while vida_pokemon > 0 and vida_mewtwo > 0 :
    # danos
    dano_pokemon = random.randint(250, 500)
    dano_mewtwo = random.randint(50,250)

    print (f"{cor_ciano}\nRodada {rodada}\n{reset_cor}") # Organização

    match pokemon:
        case '1': # Charizard
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Charizard causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1 
            if rodada > 2 :
                vida_pokemon -= dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Charizard, resta {vida_pokemon} de vida{reset_cor}")

        case '2': # Lapras
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Lapras causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1
            if rodada > 2 :
                vida_pokemon -=dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Lapras, resta {vida_pokemon} de vida{reset_cor}")

        case '3': # Dragonite
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Dragonite causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1
            if rodada > 2 :
                vida_pokemon -= dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Dragonite, resta {vida_pokemon} de vida{reset_cor}")

        case '4': # Raichu
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Raichu causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1
            if rodada > 2 :
                vida_pokemon -= dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Raichu, resta {vida_pokemon}{reset_cor}")

        case '5': # Alakazam
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Alakazam causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1
            if rodada > 2 :
                vida_pokemon -= dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Alakazam, resta {vida_pokemon} de vida{reset_cor}")

        case '6': # Rayquaza
            vida_mewtwo -= dano_pokemon
            print (f"{cor_verde}Rayquaza causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida{reset_cor}")
            rodada +=1
            if rodada > 2 :
                vida_pokemon -= dano_mewtwo
                print (f"{cor_vermelho}Mewtwo causou {dano_mewtwo} dano em Rayquaza, resta {vida_pokemon} de vida{reset_cor}")

        # Usuario não seguiu instruções
        case _ :
            print (f"{cor_vermelho}========== Número invalido =========={reset_cor}")
            break


if pokemon == "1" and vida_pokemon > 0: #Charizard
    print (f"{cor_verde}\n====== Charizard Venceu ======{reset_cor}")
elif pokemon == "2" and vida_pokemon > 0: #Lapras
    print (f"{cor_verde}\n====== Lapras Venceu ======{reset_cor}")
elif pokemon == "3" and vida_pokemon > 0: #dragonite
    print (f"{cor_verde}\n====== Dragonite Venceu ======{reset_cor}")
elif pokemon == "4" and vida_pokemon > 0: #Raichu
    print (f"{cor_verde}\n====== Raichu Venceu ======{reset_cor}")
elif pokemon == "5" and vida_pokemon > 0: #Alakazam
    print (f"{cor_verde}\n====== Alakazam Venceu ======{reset_cor}")
elif pokemon == "6" and vida_pokemon > 0: #rayquaza
    print (f"{cor_verde}\n====== Rayquaza Venceu ======{reset_cor}")
else:
    print (f"{cor_vermelho}\n====== Mewtwo venceu ======\n{reset_cor}")