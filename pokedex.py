# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# Função para adicionar os pokémons
def pokemons() -> dict:
    nome = input ("Digite o nome do pokémon: ")
    tipo = input ("Digite o tipo do pokémon: ")
    fraqueza = input ("Digite a fraqueza do pokémon: ")
    print() # Pular linha
    pokedex.update({nome : {"Tipo" : tipo , "Fraqueza" : fraqueza}})
    return pokedex

# Dicionario vazio
pokedex = {}

print(f"{cor_ciano}====== POKÉDEX ======\n{reset_cor}") # Organização

while True:
    try:
        qnt_pokemons = int(input(f"{cor_verde}=== Digite a quantidade de pokémons: {reset_cor}"))
    
        # Adicionando os pokémons
        for i in range(qnt_pokemons):
            pokemons()

        # Organização
        print(f"\n{cor_ciano}===== Pokémons Registrado na Pokédex =====\n{reset_cor}") # Organização

        for chave,valor in pokedex.items():
            print(f"Nome: {chave}")
            # Exibindo o 'valor' com as chaves ['Tipo'] and ['Fraqueza']
            print(f"    Tipo: {valor['Tipo']}")
            print(f"    Fraqueza: {valor['Fraqueza']}\n")
        break
    
    except ValueError: # Se for digitado algo que não seja número ele gera esse erro
        print(f"\n{cor_vermelho}===== ERRO: digite números =====\n{reset_cor}")