import pytest
from ..src.card import Card
from ..src.card import Suite
from ..src.card import Rank
from ..src.hand import Hand


def test_high_card():
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.three),
             Card(Suite.diamonds, Rank.five),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.nine)]
    hand = Hand()
    for c in cards:
        hand.add(c)
    assert hand.two() == False

    
def test_pair_input():
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.eight),
             Card(Suite.diamonds, Rank.five),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.nine)]
    hand = Hand()
    for c in cards:
        hand.add(c)
    assert hand.two() == True

def test_three_of_a_kind_input():
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.eight),
             Card(Suite.diamonds, Rank.eight),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.nine)]
    hand = Hand()
    for c in cards:
        hand.add(c)
    assert hand.three() == True

def test_straight():
    cards = [Card(Suite.hearts, Rank.queen), 
             Card(Suite.spades, Rank.ten),
             Card(Suite.diamonds, Rank.nine),
             Card(Suite.clubs, Rank.jack),
             Card(Suite.hearts, Rank.eight)]
    hand = Hand()
    for c in cards:
        hand.add(c)
    assert hand.straight() == True

def test_flush():
    cards = [Card(Suite.hearts, Rank.queen), 
             Card(Suite.hearts, Rank.ten),
             Card(Suite.hearts, Rank.nine),
             Card(Suite.hearts, Rank.jack),
             Card(Suite.hearts, Rank.eight)]
    hand = Hand()
    for c in cards:
        hand.add(c)
    assert hand.same_suite() == True
    