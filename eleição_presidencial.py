# Em uma eleição presidencial, existem 5 candidatos. Os votos serão registrados da seguinte forma:
# 1, 2, 3, 4, 5 - Voto para os respectivos candidatos 
# 6 - Voto nulo
# 7 - Voto em branco

# Construa um algoritmo que: 
# • Leias o voto de cada pessoa; 
# • Calcule o total de votos de cada candidato;
# • Calcule o total de votos nulos; 
# • Calcule o total de votos em branco; 
# • Determine o candidato vencedor;
# • mostre os valores dos itens anteriores.

# OBS: Quando for digitado ZERO que indica o fim do processamento e que não deve ser considerado.
#################################################################################################################

# Retorna a quantidade de vezes que o candidado foi votado
def contando_votos_candidatos(n) :
    return len(n)

# Candidatos
candidato_1 = "Neymar"
candidato_2 = "Messi"
candidato_3 = "CR7"
candidato_4 = "Haaland"
candidato_5 = "Mbappé"

# Listas dos candidatos
lista_candidato_1 = []
lista_candidato_2 = []
lista_candidato_3 = []
lista_candidato_4 = []
lista_candidato_5 = []
lista_voto_nulo_6 = []
lista_voto_branco_7 = []


# Organização
print ("\n===== Eleição Presidencial =====\n")
print ("=== Números dos Canditados ===\n")
# Organização
print (f"1. {candidato_1}")
print (f"2. {candidato_2}")
print (f"3. {candidato_3}")
print (f"4. {candidato_4}")
print (f"5. {candidato_5}")
print (f"6. Voto nulo")
print (f"7. Voto em branco")
print ("0. para encerrar votos\n")

while True :
    vote = input ("=== Escolha o Candidato e digite seu número (0 para sair): ")

    if vote == "0" :
        print ("\n===== VOTAÇÕES ENCERRADAS =====\n")
        break
    elif vote == "1" :
        lista_candidato_1.append(1)
    elif vote == "2" :
        lista_candidato_2.append(1)
    elif vote == "3" :
        lista_candidato_3.append(1)
    elif vote == "4" :
        lista_candidato_4.append(1)
    elif vote == "5" :
        lista_candidato_5.append(1)
    elif vote == "6" :
        lista_voto_nulo_6.append(1)
    elif vote == "7" :
        lista_voto_branco_7.append(1)
    else:
        print ("\n===== ERRO, tente novmente =====\n")

# Votos
votos_candidatos = {
    candidato_1 : contando_votos_candidatos(lista_candidato_1) ,
    candidato_2 : contando_votos_candidatos(lista_candidato_2) ,
    candidato_3 : contando_votos_candidatos(lista_candidato_3) ,
    candidato_4 : contando_votos_candidatos(lista_candidato_4) ,
    candidato_5 : contando_votos_candidatos(lista_candidato_5) ,
    }

# Exibindo a lista de votos para o usuario
for chave,valor in votos_candidatos.items() :
    print (f"=== O candidato ( {chave} ) obteve: {valor} Votos")
print (f"=== O Voto nulo obeteve: {contando_votos_candidatos(lista_voto_nulo_6)} Votos")
print (f"=== Votos em branco obeteve: {contando_votos_candidatos(lista_voto_branco_7)} Votos")

# Verifica todos os valores. O maior valor é pegado e adicionado junto com a sua chave para a variavel 'vencedor'
vencedor = max(votos_candidatos, key = votos_candidatos.get)

# vencedor = max(votos_candidatos, key=votos_candidatos.get)
print (f"\n===== O vencedor é: {vencedor} com {votos_candidatos[vencedor]} votos! =====")