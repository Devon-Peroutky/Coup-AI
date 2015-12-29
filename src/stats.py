possible_pairs = [
    'Ambassador Contessa',
    'Captain Duke',
    'Contessa Duke',
    'Ambassador Assassin',
    'Ambassador Captain',
    'Assassin Contessa',
    'Assassin Captain',
    'Assassin Duke',
    'Ambassador Duke',
    'Captain Contessa',
    'Duke Duke',
    'Ambassador Ambassador',
    'Contessa Contessa',
    'Captain Captain',
    'Assassin Assassin'
]

def base_probability():
    return 2/15

def known_probability(this_player, game, other_player):
    potential_cards = [card for card in game.card_population if card not in this_player.known_cards]
    return len(other_player)/len(potential_cards)


