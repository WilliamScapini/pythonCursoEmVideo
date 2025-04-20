def player(jog = "<desconhecido>",gols = 0):
    if not gols.isnumeric():
        gols = 0
    if not jog.isalpha():
        jog = "<desconhecido>"
    print(f"o jogador {jog} fez {gols} no campeonato")

jogador = input("Nome do Jogador: ")
gols = input("Gols do Jogador: ")
player(jogador,gols)