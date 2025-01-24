# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# CARDÁPIO
ingrediente1 = "queijo"
ingrediente2 = "frango"
ingrediente3 = "frango com queijo"
ingrediente4 = "pizza"
ingrediente5 = "carne"

# Lista do que vai no pastel
pastel = []

# Organização
print(f"\n{cor_ciano}======== Bem-vindo a Pastelaria Nunes ========\n")
print(f"======== Aqui está nosso cardápio: \n")

print(f"== Escolha quantos ingredientes preferir ==\n")
print(f"1- Queijo")
print(f"2- Frango")
print(f"3- Frango com Queijo")
print(f"4- Pizza")
print(f"5- Carne{reset_cor}")

while True:
    escolha = input(f"\n{cor_verde}Digite de 1 a 5 para escolha, ou digite 'sair' quando terminar de escolher: {reset_cor}").lower()
    
    if escolha == "sair" :
        print(f"{cor_vermelho}\n ===== Você terminou de escolher ! =====\n{reset_cor}")
        break
        
    elif escolha == "1":
        if ingrediente1 not in pastel: # Se não estiver, adiciono
            print(f"{cor_ciano}\n===== Sabor adicionado, mais algum? =====\n{reset_cor}")
            pastel.append(ingrediente1)
        else:
            print(f"{cor_vermelho}\nEsse sabor você já escolheu, escolha outro !\n{reset_cor}")
            
    elif escolha == "2":
        if ingrediente2 not in pastel: # Se não estiver, adiciono
            print(f"{cor_ciano}\n===== Sabor adicionado, mais algum? =====\n{reset_cor}")
            pastel.append(ingrediente2)
        else:
            print(f"{cor_vermelho}\nEsse sabor você já escolheu, escolha outro !\n{reset_cor}")
            
    elif escolha == "3":
        if ingrediente3 not in pastel: # Se não estiver, adiciono
            print(f"{cor_ciano}\n===== Sabor adicionado, mais algum? =====\n{reset_cor}")
            pastel.append(ingrediente3)
        else:
            print(f"{cor_vermelho}\nEsse sabor você já escolheu, escolha outro !\n{reset_cor}")
            
    elif escolha == "4":
        if ingrediente4 not in pastel: # Se não estiver, adiciono
            print(f"{cor_ciano}\n===== Sabor adicionado, mais algum? =====\n{reset_cor}")
            pastel.append(ingrediente4)
        else:
            print(f"{cor_vermelho}\nEsse sabor você já escolheu, escolha outro !\n{reset_cor}")
            
    elif escolha == "5":
        if ingrediente5 not in pastel: # Se não estiver, adiciono
            print(f"{cor_ciano}\n===== Sabor adicionado, mais algum? =====\n{reset_cor}")
            pastel.append(ingrediente5)
        else:
            print(f"{cor_vermelho}\nEsse sabor você já escolheu, escolha outro !\n{reset_cor}")
            
    else:
        print(f"{cor_vermelho}\n===== Você está fazendo algo errado, tente de novo =====\n{reset_cor}")

# Organização
print(f"{cor_ciano}======== Esses são os ingredientes que vão no seu pastel: \n{reset_cor}")
for ingrediente in pastel:
    print(f"- {ingrediente}")

print(f"{cor_ciano}\n ======== Obrigado por escolher a Pastelaria Nunes <3 ========{reset_cor}")