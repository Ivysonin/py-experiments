# Função para adicionar os pokémons
def pokemons() :
    nome = input ("Digite o nome do pokémon: ")
    tipo = input ("Digite o tipo do pokémon: ")
    fraqueza = input ("Digite a fraqueza do pokémon: ")
    pokedex.update({nome : {"Tipo" : tipo , "Fraqueza" : fraqueza}})
    return pokedex

# Dicionario vazio
pokedex = {}

print ("====== POKÉDEX ======\n") # Organização

while True :
    try :
        qnt_pokemons = int(input ("=== Digite a quantidade de pokémons: "))
    
        # Adicionando os pokémons
        for i in range(qnt_pokemons) :
            pokemons()

# Organização
        print ("\n===== Pokémons Registrado na Pokédex =====\n") # Organização

        for chave,valor in pokedex.items() :
            print(f"{chave} - {valor}")
        break
    
    except ValueError :
        print ("\n===== ERRO: digite números =====\n")