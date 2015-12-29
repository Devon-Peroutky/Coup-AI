from card import Captain, Contessa, Assassin, Ambassador, Duke
from itertools import cycle
from random import shuffle
from copy import deepcopy
import sys
from card import IllegalTarget, IllegalAction
from player import Player
from actions import is_blockable, is_bsable, is_targeted, ACTION_MAP

# Declarations
card_population = [Assassin() for _ in xrange(3)] + \
                  [Ambassador() for _ in xrange(3)] + \
                  [Captain() for _ in xrange(3)] + \
                  [Contessa() for _ in xrange(3)] + \
                  [Duke() for _ in xrange(3)]

revealed_cards = []


class Game(object):

    def __init__(self, names):
        self.current_move = None
        self.players = {name.lower(): Player(name) for name in names}
        self.finishers = {}
        self.deck = deepcopy(card_population)

    def __len__(self):
        return sum([1 for player in self.players.values() if player.has_influence()])

    def nactive_players(self):
        return self.players.values()

    def get_player(self, name):
        return self.players.get(name)

    def _play(self):
        for acting_player in cycle(self.players.values()):
            self.check_for_winner()

            if not acting_player.has_influence():
                continue
            self.perform_move(acting_player)

    def play_coup(self):
        print 'Dealing Cards...'
        self.deal_cards()

        print "Let's play"
        self._play()

    def check_for_winner(self):
        # Only 1 player left, we have a winner
        if len(self) == 1:
            self.place(self.players[0])
            '''
            Update Finish Table
            '''
            sys.exit(0)

    def place(self, player):
        position = len(self)
        print '{} has finished in position: {}'.format(player, position)

        self.finishers[position] = player
        self.players.pop(player)

    def deal_cards(self):
        shuffle(self.deck)

        for player in self.players.values():
            player.initialize_cards(self.deck.pop(), self.deck.pop())

    def _execute_bullshit(self, defendant, accuser, card_in_question):
        flipped_card = defendant.sacrifice()
        print 'Is {} a {}?'.format(flipped_card, card_in_question)

        # Defendant was telling the truth
        if flipped_card == card_in_question:
            print '{} was telling the truth.'.format(defendant)
            print accuser.sacrifice()
            self.deck.append(flipped_card)
            shuffle(self.deck)
            defendant.set_cards([self.deck.pop()])
            return True

        # Defendant was bluffing
        else:
            print '{} was lieing.'.format(defendant)
            revealed_cards.append(flipped_card)
            return False

    def offer_block(self, acting_player, block_action, target_player):
        if target_player.get_block():
            print 'WE GOT A BLOCK'
            return self.offer_bullshit(target_player, block_action, accusers=[acting_player])
        return True

    def offer_bullshit(self, the_player, action, accusers=None):
        accusers = accusers or self.players.values()
        for player in accusers:
            if player is the_player:
                continue
            if player.get_bullshit():
                print 'WE GOT A BULLSHIT'
                return self._execute_bullshit(the_player, player, ACTION_MAP.get(action))
        return True

    def _perform(self, acting_player, action, target_player=None):
        # Special case for exchanging
        if action is Ambassador.exchange:
            return action(acting_player, self.deck)
        # Evey other action
        else:
            return action(acting_player, target_player) if target_player else action(acting_player)

    def _validate_move(self, target_player):
        if is_targeted(self.current_move.__name__) and not target_player:
            raise IllegalTarget("That player was not able to be found. Try again")

    def announce_action(self, acting_player, target_player=None):
        output = '{} is using {}'.format(str(acting_player), self.current_move.__name__)
        if target_player:
            output += ' on {}\n'.format(target_player)
        print output

    def perform_move(self, acting_player):
        successful_through_block, successful_through_bs = True, True

        while True:
            try:
                self.current_move, target_player = acting_player.get_move()
                target_player = self.players.get(target_player)
                self.announce_action(acting_player, target_player)
                self._validate_move(target_player)

                if is_bsable(self.current_move):
                    print 'Getting Bullshits'
                    successful_through_bs = self.offer_bullshit(acting_player, self.current_move.__name__)
                if is_blockable(self.current_move):
                    print 'Getting Blocks'
                    successful_through_block = self.offer_block(acting_player, is_blockable(self.current_move), target_player)

                if successful_through_block and successful_through_bs:
                    self._perform(acting_player, self.current_move, target_player)
                if self.current_move is Assassin.assassinate:
                    acting_player.mutate_coins(-3)
                return
            except (IllegalTarget, IllegalAction) as e:
                print e
