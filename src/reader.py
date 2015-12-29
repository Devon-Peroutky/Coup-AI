from collections import namedtuple
from actions import INCOME, FOREIGN_AID, COUP, ASSASSINATE, STEAL, EXCHANGE, TAX, ACTION_HANDLERS
from actions import is_targeted
from card import Card
from move import Move

Input = namedtuple('Input', 'prompt validation_function')


class Reader(object):
    MOVE = '{}What would you like to do? ' \
       '\n\t- {}' \
       '\n\t- {}' \
       '\n\t- {} [target_player]' \
       '\n\t- {} [target_player]' \
       '\n\t- {} [target_player]' \
       '\n\t- {}' \
       '\n\t- {}\n'.format('{}', INCOME, FOREIGN_AID, COUP, ASSASSINATE, STEAL, EXCHANGE, TAX)
    BS = '{}: would you like to BS (Yes or No)?'
    BLOCK = '\t{}: would you like to block (Yes or No)?'
    EXCHANGE = '\t{}: which card(s) would like? \t{}'
    SACRIFICE = '\t{}: which of your cards would you like to sacrifice?'

    def __init__(self):
        self._load_input_map()

    def _load_input_map(self):
        self.input_map = {
            'move': Input(self.MOVE, self.validate_move),
            'bs': Input(self.BS, self.validate_bs),
            'block': Input(self.BLOCK, self.validate_bs),
            'exchange': Input(self.EXCHANGE, self.validate_exchange),
            'sacrifice': Input(self.SACRIFICE, self.validate_sacrifice)
        }

    def validate_exchange(self, player_input):
        print 'Validating exchange'
        input_1, input_2 = player_input.strip().split(' ')
        card_1 = Card.build_card(input_1.lower())
        card_2 = Card.build_card(input_2.lower())

        if card_1 is None or card_2 is None:
            raise UnparsableAction('Could not parse the card type(s) from input: {}'.format(player_input))
        else:
            print 'Selecting {}, {}'.format(card_1, card_2)
            return card_1, card_2

    def validate_sacrifice(self, player_input):
        card = Card.build_card(player_input.strip())

        if card is None:
            raise UnparsableAction('Could not parse the card type from input: {}'.format(player_input))
        else:
            return card, None

    @staticmethod
    def validate_move(player_input):
        move = player_input.strip().split(' ')
        if len(move) == 2:
            action, target_player = move
        else:
            action = move[0]
            target_player = None
        print 'Validating move: {}  {}'.format(action, target_player)
        if action not in ACTION_HANDLERS:
            raise UnparsableAction('Cannot identify the inputted move: {}'.format(action))

        if not is_targeted(action):
            return ACTION_HANDLERS.get(action), None

        if is_targeted(action) and not target_player:
            raise UnparsableAction('Inputted move: {} requires a target player'.format(action))
        return ACTION_HANDLERS.get(action), target_player

    def validate_bs(self, player_input):
        bs = player_input.strip()
        print bs
        if bs == 'yes' or bs == 'no':
            return bs, None
        else:
            raise UnparsableAction('Select either Yes or No')

    def _parse_action(self, action, target_player=None):
        pass

    def get(self, player, input_type, *args):
        action, target_player = None, None
        prompt, validation_func = self.input_map.get(input_type)

        while True:
            try:
                player_input = raw_input(prompt.format(player.output(), *args)).lower()
                action, target_player = validation_func(player_input)
                print 'Returning {} {}'.format(action, target_player)
                return action, target_player
            except (TypeError, UnparsableAction, ValueError) as e:
                print 'Error parsing move -> {}'.format(e)



class UnparsableAction(Exception):
    pass