from card import IllegalAction, Duke, Captain, Assassin, Ambassador, Contessa


class Action(object):

    @staticmethod
    def income(active_player):
        active_player.mutate_coins(1)

    @staticmethod
    def foreign_aid(active_player):
        active_player.mutate_coins(2)

    @staticmethod
    def coup(active_player, target_player):
        if active_player.coins >= 7:
            active_player.coins -= 7
            target_player.sacrifice()
        else:
            raise IllegalAction("insufficient currency to coup")

    @staticmethod
    def sacrifice_card(active_player):
        active_player.sacrifice()

    @classmethod
    def actions_for_influences(cls, influences):
        actions = []
        for inf in cls.__subclasses__():
            if inf.__name__ in influences:
                actions.extend(inf.ACTIONS)
        return sorted(actions)

    @classmethod
    def blocks_for_influences(cls, influences):
        blocks = []
        for inf in cls.__subclasses__():
            if inf.__name__ in influences:
                blocks.extend(inf.BLOCKS)
        return sorted(blocks)


# Actions
INCOME = 'income'
FOREIGN_AID = 'foreign_aid'
STEAL = 'steal'
TAX = 'tax'
ASSASSINATE = 'assassinate'
EXCHANGE = 'exchange'
COUP = 'coup'
SACRIFICE = 'sacrifice'
BLOCK_STEAL = 'block_steal'
BLOCK_ASSASSINATION = 'block_assassination'
BLOCK_FOREIGN_AID = 'block_foreign_aid'

ACTION_MAP = {
    TAX: Duke(),
    STEAL: Captain(),
    ASSASSINATE: Assassin(),
    EXCHANGE: Ambassador(),
    BLOCK_STEAL: Captain(), # MAKE THIS HANDLE AMBASSADOR
    BLOCK_ASSASSINATION: Contessa(),
    BLOCK_FOREIGN_AID: Duke()
}

ACTION_HANDLERS = {
    INCOME: Action.income,
    FOREIGN_AID: Action.foreign_aid,
    COUP: Action.coup,
    STEAL: Captain.steal,
    TAX: Duke.tax,
    ASSASSINATE: Assassin.assassinate,
    EXCHANGE: Ambassador.exchange,
    SACRIFICE: Action.sacrifice_card
}


def is_targeted(move):
    if move in ['steal', 'assassinate', 'coup']:
        return True
    else:
        return False


def is_blockable(action):
    move = action.__name__
    print 'MOVE: {}'.format(move)
    if move is 'foreign_aid':
        return BLOCK_FOREIGN_AID
    elif move is 'assassination':
        return BLOCK_ASSASSINATION
    elif move is 'steal':
        return BLOCK_STEAL
    else:
        return None


def is_bsable(action):
    move = action.__name__
    if move in ['steal', 'tax', 'assassinate', 'exchange', 'block_steal', 'block_assassinate']:
        return True
    else:
        return False
