#!/usr/bin/env python

from __future__ import print_function, unicode_literals, division
from random import random
from utils import nl


class Tree(object):
    height = 0

    def __repr__(self):
        return "<%s tree, %.1f ft>" % (self.name, self.height)

    def grow(self):
        self.height += self.growth_rate + self.growth_rate * random() / 3

class Bamboo(Tree):
    growth_rate = 10
    name        = "Bamboo"

class Birch(Tree):
    growth_rate = 1.2
    name        = "Birch"


def main():
    trees = Bamboo(), Bamboo(), Birch(), Birch()
    print(trees, nl)

    for tree in trees: tree.grow()
    print(trees, nl)

    for _ in range(5):
        for tree in trees: tree.grow()
    print(trees, nl)

main()
