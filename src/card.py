from random import shuffle

def create(type):
    pass

class Card(object):
    def __init__(self):
        self.type = None
        self.revealed = False
        self.ACTIONS = None
        self.BLOCKS = None

    def reveal(self):
        self.revealed = True

    def get_type(self):
        return self.type

    def __eq__(self, other):
        return self.type == other.type

    def __ne__(self, other):
        return self.type != other.type

    def __str__(self):
        return str(self.type)

    @staticmethod
    def build_card(type):
        if type == 'contessa':
            return Contessa()
        if type == 'duke':
            return Duke()
        if type == 'assassin':
            return Assassin()
        if type == 'ambassador':
            return Ambassador()
        if type == 'captain':
            return Captain()
        return None

    @staticmethod
    def actions_for_influences():
        pass

    @staticmethod
    def blocks_for_influences():
        pass

class Contessa(Card):
    def __init__(self, type='contessa'):
        self.type = type
        self.ACTIONS = []
        self.BLOCKS = ['assassinate']

class Assassin(Card):
    def __init__(self, type='assassin'):
        self.type = type
        self.ACTIONS = ['assassinate']
        self.BLOCKS = []

    @staticmethod
    def assassinate(active_player, target_player):
        if active_player.coins >= 3 and target_player.has_influence():
            active_player.mutate_coins(-3)
            target_player.sacrifice()
        else:
            raise IllegalAction('Three coins and valid target are necessary for an assassination')


class Duke(Card):
    def __init__(self, type='duke'):
        self.type = type
        self.ACTIONS = ['tax']
        self.BLOCKS = ['foreign_aid']

    @staticmethod
    def tax(active_player):
        active_player.mutate_coins(3)

class Captain(Card):
    def __init__(self, type='captain'):
        self.type = type
        self.ACTIONS = ['steal']
        self.BLOCKS = ['steal']

    @staticmethod
    def steal(active_player, player_target):
        if player_target.coins >= 2:
            player_target.mutate_coins(-2)
            active_player.mutate_coins(2)
        else:
            available_coins = player_target.coins
            player_target.mutate_coins(-available_coins)
            active_player.mutate_coins(available_coins)

class Ambassador(Card):
    def __init__(self, type='ambassador'):
        self.type = type
        self.ACTIONS = ['exchange']
        self.BLOCKS = ['steal']

    @staticmethod
    def exchange(active_player, deck):
        # Get the player her/his choices
        available_options = active_player.pop_cards()
        available_options.append(deck.pop())
        available_options.append(deck.pop())

        # Have the player get cards
        while True:
            try:
                selection = active_player.get_exchange_selection(available_options)
                for card in selection:
                    available_options.remove(card)
                remaining = available_options
                print selection
                print remaining
                if len(remaining) > 2:
                    raise IllegalAction("Not a valid choice, try again")

                deck.extend(remaining)

                # Give the man/woman his/her cards
                active_player.set_cards(selection)

                print active_player.output()

                # Put the cards back
                shuffle(deck)
                return
            except IllegalAction as e:
                print e


class IllegalAction(Exception):
    pass


class IllegalTarget(Exception):
    pass
