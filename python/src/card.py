from enum import Enum

class Suite(Enum):
    hearts=1
    spades=2
    diamonds=3
    clubs=4

class Rank(Enum):
    two=2
    three=3
    four=4
    five=5
    six=6
    seven=7
    eight=8
    nine=9
    ten=10
    jack=11
    queen=12
    king=13
    ace=14


class Card:
    
    def __init__(self, suite : Suite, rank : Rank):
        self.rank = rank
        self.suite = suite