# Adicionar os pokémons
# Tipo do pokémon
# Fraqueza do pokémon
# Exibir uma lista

pokedex = {}

print ("====== POKÉDEX ======\n") # Organização

qnt_pokemons = int(input ("=== Digite a quantidade de pokémons: "))

for i in range(qnt_pokemons) :
    nome = input ("Digite o nome do pokémon: ")
    tipo = input ("Digite o tipo do pokémon: ")
    fraqueza = input ("Digite a fraqueza do pokémon: ")
    pokedex.update({nome : {"Tipo" : tipo , "Fraqueza" : fraqueza}})

print ("\n===== Pokémons Registrado na Pokédex =====\n") # Organização

for chave,valor in pokedex.items() :
    print(f"{chave} - {valor}")
