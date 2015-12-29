from reader import Reader
from card import IllegalTarget

class Player(object):
    # Base
    name = None
    coins = 0

    # AI
    influence = None
    known_cards = None

    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.reader = Reader()
        self.active_cards = []

    def __str__(self):
        return '{}'.format(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __len__(self):
        return len(self.active_cards)

    def output(self):
        return '{} ({} coins):\n\t{}\t\n'.format(self.name, self.coins, self.active_cards)

    def initialize_cards(self, card_1, card_2):
        self.active_cards = [card_1, card_2]

    def set_cards(self, cards):
        self.active_cards.extend(cards)

    def pop_cards(self):
        temp = self.active_cards
        self.active_cards = []
        return temp

    def has(self, card):
        return card in self.active_cards

    def mutate_coins(self, diff):
        self.coins += diff

    def has_influence(self):
        return True if self.active_cards else False

    def _sacrifice(self, card):
        if not self.has(card):
            raise IllegalTarget('Try again, I do not think you have the {}'.format(card))
        else:
            print '{} has just flipped the {}'.format(self.name, card)
            self.active_cards.remove(card)

    # ----------------------
    # Get Actions
    # ----------------------
    def couped(self):
        pass

    def assassinated(self):
        pass

    def stolen(self):
        pass

    def validate(self, action, target_player):
        pass

    # ----------------------
    # Get Actions
    # ----------------------
    def get_move(self):
        return self.reader.get(self, 'move')

    def sacrifice(self):
        while True:
            try:
                card = self.reader.get(self, 'sacrifice')[0]
                self._sacrifice(card)
                return card
            except IllegalTarget as e:
                print e

    def get_exchange_selection(self, available_options):
        return self.reader.get(self, 'exchange', available_options)

    def get_bullshit(self):
        print 'Getting BS'
        bs = self.reader.get(self, 'bs')[0]
        print 'BS: {}'.format(bs)
        return bs == 'yes'

    def get_block(self):
        block = self.reader.get(self, 'block')[0]
        print 'Block: {}'.format(block)
        return block == 'yes'
