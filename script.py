from src.game import Game
from src.player import Player

def main():
    the_players = ['Kevin', 'Ryan', 'Devon', 'Matt']
    the_game = Game(the_players)
    the_game.play_coup()

if __name__ == '__main__':
    main()