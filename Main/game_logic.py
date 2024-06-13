from deck_class import Deck
from player_class import Player

def play_war():
    # Create deck and shuffle
    deck = Deck()
    deck.shuffle()

    # Split deck between two players
    player_one = Player("One")
    player_two = Player("Two")

    for _ in range(26):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    # Game logic here
    game_on = True
    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round {round_num}")

        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Player Two wins!")
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Player One wins!")
            game_on = False
            break

        # Start a new round
        player_one_cards = [player_one.remove_one()]
        player_two_cards = [player_two.remove_one()]

        # War logic here (simplified example)
        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print("War!")
                if len(player_one.all_cards) < 5:
                    print("Player One unable to declare war")
                    print("Player Two wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to declare war")
                    print("Player One wins!")
                    game_on = False
                    break
                else:
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
