import random

print ("========== Luta Mewtwo ==========") # Organização

# Lista pokémons
print ("\n===== Pokémon =====")
print ("1- Charizard")
print ("2- Lapras")
print ("3- Dragonite")
print ("4- Raichu")
print ("5- Alakazam")
print ("6- Rayquaza")

# Pokémons
pokemon =  input ("Escolha um pokémon de 1 a 6: ")
mewtwo = "mewtwo"

# Vidas
vida_pokemon = 500
vida_mewtwo = 1000

rodada = 1

while vida_pokemon > 0 and vida_mewtwo > 0 :
    # danos
    dano_pokemon = random.randint(250, 500)
    dano_mewtwo = random.randint(50,250)

    print (f"\nRodada {rodada}\n") # Organização

    # Charizard
    if pokemon== "1" : 
        vida_mewtwo -= dano_pokemon
        print (f"Charizard causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1 
        if rodada > 2 :
            vida_pokemon -= dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Charizard, resta {vida_pokemon} de vida")

    # Lapras
    elif pokemon == "2" : 
        vida_mewtwo -= dano_pokemon
        print (f"Lapras causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1
        if rodada > 2 :
            vida_pokemon -=dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Lapras, resta {vida_pokemon} de vida")

    # Dragonite
    elif pokemon == "3" : 
        vida_mewtwo -= dano_pokemon
        print (f"Dragonite causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1
        if rodada > 2 :
            vida_pokemon -= dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Dragonite, resta {vida_pokemon} de vida")

    # Raichu
    elif pokemon == "4" : 
        vida_mewtwo -= dano_pokemon
        print (f"Raichu causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1
        if rodada > 2 :
            vida_pokemon -= dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Raichu, resta {vida_pokemon}")

    # Alakazam
    elif pokemon == "5" : 
        vida_mewtwo -= dano_pokemon
        print (f"Alakazam causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1
        if rodada > 2 :
            vida_pokemon -= dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Alakazam, resta {vida_pokemon} de vida")

    # Rayquaza
    elif pokemon == "6" :
        vida_mewtwo -= dano_pokemon
        print (f"Rayquaza causou {dano_pokemon} dano em Mewtwo, resta {vida_mewtwo} de vida")
        rodada +=1
        if rodada > 2 :
            vida_pokemon -= dano_mewtwo
            print (f"Mewtwo causou {dano_mewtwo} dano em Rayquaza, resta {vida_pokemon} de vida")

    # Usuario não seguiu instruções
    else:
        print ("Número invalido !")
        break


if pokemon == "1" and vida_pokemon > 0: #Charizard
    print (f"\n====== Charizard Venceu ======")
elif pokemon == "2" and vida_pokemon > 0: #Lapras
    print ("\n====== Lapras Venceu ======")
elif pokemon == "3" and vida_pokemon > 0: #dragonite
    print (f"\n====== Dragonite Venceu ======")
elif pokemon == "4" and vida_pokemon > 0: #Raichu
    print (f"\n====== Raichu Venceu ======")
elif pokemon == "5" and vida_pokemon > 0: #Alakazam
    print (f"\n====== Alakazam Venceu ======")
elif pokemon == "6" and vida_pokemon > 0: #rayquaza
    print (f"\n====== Rayquaza Venceu ======")
else:
    print ("\nMewtwo venceu !")
