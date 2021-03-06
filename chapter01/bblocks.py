#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from random import choice as rndchoice
from itertools import cycle

from utils import Loop, TextInput, range1, first, nl
from board import Board, BaseTile

size        = 5
pause_time  = 0.2
players     = {1: "➀➁➂➃", 2: "➊➋➌➍"}
ai_players  = [1, ]
check_moves = 15
padding     = 2, 1


class Tile(BaseTile):
    num = maxnum = player = None

    def __repr__(self):
        if self.player : return players[self.player][self.num-1]
        else           : return str(self.num)

    def increment(self, player):
        """ Increment tile number; if number wraps, increment neighbour tiles.
            `bblocks.counter` is used to avoid infinite recursion loops.
        """
        if not bblocks.counter.next(): bblocks.check_end(player)

        if self._increment(player):
            for tile in board.cross_neighbours(self):
                tile.increment(player)
            board.draw()

    def _increment(self, player):
        self.player = player
        self.num.next()
        return bool(self.num == 1)


class BlocksBoard(Board):
    def __init__(self, *args, **kwargs):
        super(BlocksBoard, self).__init__(*args, **kwargs)
        neighbours = self.neighbour_cross_locs

        for tile in self:
            tile.maxnum = len( [self.valid(nbloc) for nbloc in neighbours(tile)] )
            tile.num    = Loop(range1(tile.maxnum))

    def ai_move(self, player):
        """Randomly choose between returning the move closest to completing a tile or a random move."""
        tiles = [t for t in self if self.valid_move(player, t)]

        def to_max(t): return t.maxnum - t.num
        tiles.sort(key=to_max)
        return rndchoice( [first(tiles), rndchoice(tiles)] )

    def valid_move(self, player, tile):
        return bool(tile.player==player or not tile.player)


class BlockyBlocks(object):
    winmsg  = "player %s wins!"
    counter = Loop(range(check_moves))

    def check_end(self, player):
        """Check if game is finished."""
        if all(tile.player==player for tile in board):
            board.draw()
            print(nl, self.winmsg % player)
            sys.exit()


class Test(object):
    def run(self):
        self.textinput = TextInput(board=board)

        for p in cycle(players.keys()):
            board.draw()
            tile = board.ai_move(p) if p in ai_players else self.get_move(p)
            tile.increment(p)
            bblocks.check_end(p)

    def get_move(self, player):
        while True:
            loc = self.textinput.getloc()
            if board.valid_move(player, board[loc]) : return board[loc]
            else                                    : print(self.textinput.invalid_move)


if __name__ == "__main__":
    board   = BlocksBoard(size, Tile, num_grid=True, padding=padding, pause_time=pause_time)
    bblocks = BlockyBlocks()

    try: Test().run()
    except KeyboardInterrupt: sys.exit()
