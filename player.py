
class Player(object):
    # Base
    name = None
    card_1 = None
    card_2 = None
    coins = 0

    # AI
    influence = None
    known_cards = None

    def __init__(self, name):
        active_cards = []

    def __str__(self):
        return '{}:\n\t{}\n\t{}'.format(self.name, self.card_1, self.card_2)

    def __len__(self):
        num = 0
        if self.card_1:
            num += 1
        if self.card_2:
            num += 1
        return num

    def initialize_cards(self, card_1, card_2):
        self.card_1 = card_1
        self.card_2 = card_2
        self.active_cards.append(card_1)
        self.active_cards.append(card_2)


    def get_cards(self):
        return self.active_cards

    def has(self, card):
        return card in self.active_cards

    def influence_remaining(self):
        return self.active_cards

    def perform(self, action, target_player=None):
        pass

    # ----------------------
    # Get Actions
    # ----------------------
    def get_move(self):
        pass

    def get_card_selection(self):
        pass

    def get_exchange_selection(self):
        pass

    def get_bullshit(self):
        pass

    def get_block(self):
        pass