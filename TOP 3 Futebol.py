#código criado com ajuda de IA
# Escolha um jogador de futebol do top 3

Jogadores = {
    "Cristiano Ronaldo" and "CR7": "siiiiiiiiir",
    "MESSI" and "anao": "ET",
    "Neymar" and "NEY": "O pai tá ON"
}

# Solicite um Jogador do Top 3

escolha= input("Escolha um jogador do Top 3:").upper()

# Verificar Jogador

if escolha.upper() in Jogadores:
    print(Jogadores[escolha.upper()])
else :
    print ("jogador não encontrado")