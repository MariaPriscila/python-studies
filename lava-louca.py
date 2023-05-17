F = int(input()) # Lê o número de casos de teste
for _ in range(F):
    mesa_deck = list(map(int, input().split()))
    players_decks = []
    while True:
        player_deck = list(map(int, input().split()))
        if player_deck[0] == -1:
            break
        players_decks.append(player_deck)
    
    # inicializar variáveis
    num_players = len(players_decks)
    player_idx = 0
    mesa_idx = 0
    mesa_card = mesa_deck[mesa_idx]
    round_count = 0

    while round_count < 1000:
        round_count += 1

        # obtém a carta do jogador atual
        player_card = players_decks[player_idx][0]

        # verifica se o jogador tem uma carta igual a carta mesa
        if player_card == mesa_card:
            players_decks[player_idx].pop(0)
            mesa_deck.pop(mesa_idx)
            mesa_idx = 0
            mesa_card = mesa_deck[mesa_idx] if len(mesa_deck) > 0 else None
        else:
            players_decks[player_idx].append(players_decks[player_idx].pop(0))
            mesa_deck.append(mesa_card)
            mesa_idx += 1
            if mesa_idx >= len(mesa_deck):
                mesa_idx = 0
            mesa_card = mesa_deck[mesa_idx]

        # verifica se o jogador atual não tem mais cartas
        if len(players_decks[player_idx]) == 0:
            print(player_idx + 1)
            break

        # ir para o próximo jogador
        player_idx += 1
        if player_idx >= num_players:
            player_idx = 0

    # se nenhum jogador ganhou, Juvenal vence
    if round_count == 1000:
        print(0)

