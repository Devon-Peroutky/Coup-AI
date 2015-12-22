from random import shuffle

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
        return str(self.__class__.__name__)

    @staticmethod
    def income():
        pass

    @staticmethod
    def foreign_aid():
        pass

    @staticmethod
    def coup():
        pass

    @staticmethod
    def actions_for_influences():
        pass

    @staticmethod
    def blocks_for_influences():
        pass

class Contessa(Card):
    def __init__(self, type='queen'):
        self.type = type
        self.ACTIONS = []
        self.BLOCKS = ['assassinate']

class Assassin(Card):
    def __init__(self, type='assassin'):
        self.type = type
        self.ACTIONS = ['assassinate']
        self.BLOCKS = []

    def assassinate(self, active_player, target_player):
        if active_player.coins >= 3 and target_player.is_active():
            active_player.coins -= 3
            '''
            ASSASSINATION
            '''
        else:
            raise IllegalAction('Three coins and valid target are necessary for an assassination')


class Duke(Card):
    def __init__(self, type='duke'):
        self.type = type
        self.ACTIONS = ['tax']
        self.BLOCKS = ['foreign_aid']

    @staticmethod
    def tax(active_player):
        active_player.coins += 3

class Captain(Card):
    def __init__(self, type='captain'):
        self.type = type
        self.ACTIONS = ['steal']
        self.BLOCKS = ['steal']

    @staticmethod
    def steal(active_player, player_target):
        if player_target.coins >= 2:
            player_target.coins -= 2
            active_player.coins += 2
        else:
            available_coins = player_target.coins
            player_target.coins -= available_coins
            active_player.coins += available_coins

class Ambassador(Card):
    def __init__(self, type='ambassador'):
        self.type = type
        self.ACTIONS = ['exchange']
        self.BLOCKS = ['steal']

    @staticmethod
    def exchange(active_player, deck):
        # Get the player her/his choices
        available_options = active_player.get_cards()
        available_options.append(deck.pop())
        available_options.append(deck.pop())

        # Have the player get cards
        remaining = active_player.get_exchange_selection(available_options)

        # Put the cards back
        shuffle(deck.extend(remaining))

class IllegalAction(Exception):
    pass


class IllegalTarget(Exception):
    pass