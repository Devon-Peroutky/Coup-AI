class MoveBulder(object):
    def __init__(self):
        self.action = None
        self.acting_player = None
        self.targeted_player = None
        self.handler = None
        self.coin_requirements = None

    def add_action(self, action):
        self.action = action

    def add_acting_player(self, acting_player):
        self.acting_player = acting_player

    def add_targeted_player(self, targeted_player):
        self.targeted_player = targeted_player

    def add_handler(self, handler):
        self.handler = handler

    def add_coin_requirements(self, coins):
        self.coin_requirements = coins

    def build_move(self):
        return Move(self.acting_player, self.action, self.handler, self.targeted_player, self.coin_requirements)


class Move(object):
    def __init__(self, acting_player, action, handler=None, targeted_player=None, coin_requirements=None):
        self.acting_player = acting_player
        self.action = action
        self.handler = handler
        self.targeted_player = targeted_player
        self.coin_requirements = coin_requirements

    def add_action(self, action):
        self.action = action

    def add_acting_player(self, acting_player):
        self.acting_player = acting_player

    def add_targeted_player(self, targeted_player):
        self.targeted_player = targeted_player

    def add_handler(self, handler):
        self.handler = handler

    def add_coin_requirements(self, coins):
        self.coin_requirements = coins
