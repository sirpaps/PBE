#!/usr/bin/env python

# Imports {{{
import sys
from random import randint
from copy import deepcopy

from shared import *

dimensions = 8, 8
empty = ' '
# }}}



class Loc(object):
    def __init__(self, x, y=None):
        x, y = unwrap(x, y)
        self.loc = x, y
        self.x, self.y = x, y

    def __str__(self):
        return str(self.loc)

    def __iter__(self):
        return iter(self.loc)
