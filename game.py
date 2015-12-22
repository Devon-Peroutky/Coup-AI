from card import Captain, Contessa, Assassin, Ambassador, Duke
from itertools import cycle
from random import shuffle
from copy import deepcopy

class Game(object):
    # Declarations
    players = {}
    card_population = [Assassin() for _ in xrange(3)] + \
                      [Ambassador() for _ in xrange(3)] + \
                      [Captain() for _ in xrange(3)] + \
                      [Contessa() for _ in xrange(3)] + \
                      [Duke() for _ in xrange(3)]

    # Card-types
    CONTESSA = 'contessa'
    DUKE = 'duke'
    CAPTAIN = 'captain'
    AMBASSADOR = 'ambassador'
    ASSASSIN = 'assassin'

    # Actions
    INCOME = 'income'
    FOREIGN_AID = 'foreign_aid'
    STEAL = 'steal'
    TAX = 'tax'
    ASSASSINATE = 'assassinate'
    EXCHANGE = 'exchange'
    COUP = 'coup'
    ACTIONS = {
        'all': set(['income', 'foreign_aid', 'coup', 'steal', 'tax', 'assassinate', 'exchange']),
        'free': set(['income', 'foreign_aid', 'coup']),
        'blockable': set(['assassinate', 'steal', 'foreign_aid']),
        'targets_influence': set(['coup', 'assassinate']),
        'targets_player': set(['steal']),
        'bluffable': set(['steal', 'tax', 'assassinate', 'exchange']),
    }

    def __init__(self, players):
        self.players = players
        self.deck = deepcopy(self.card_population)

    def __len__(self):
        return sum([1 for player in self.players.values() if player.influence_remaining()])

    def play(self):
        for acting_player in cycle(self.players):
            if not acting_player.influence_remaining:
                continue
            acting_player.perform

    def deal_cards(self):
        shuffle(self.deck)

        for player in self.players:
            player.card_1 = self.deck.pop()
            player.card_2 = self.deck.pop()


    def make_turn(self):
        pass

