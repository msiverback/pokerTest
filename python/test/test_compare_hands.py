from ..src.card import Card
from ..src.card import Suite
from ..src.card import Rank
from ..src.hand import Hand

def test_compare_hands():
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.three),
             Card(Suite.diamonds, Rank.five),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.nine)]
    hand1 = Hand()
    for c in cards:
        hand1.add(c)   
    assert hand1.two() == False
    assert hand1.straight() == False
    assert hand1.same_suite() == False
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.three),
             Card(Suite.diamonds, Rank.five),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.king)]
    hand2 = Hand()
    for c in cards:
        hand2.add(c)
    assert hand2.two() == False
    assert hand2.straight() == False
    assert hand2.same_suite() == False
    assert hand1.better(hand2) == False
    assert hand2.better(hand1) == True
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.three),
             Card(Suite.diamonds, Rank.eight),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.nine)]
    hand1 = Hand()
    for c in cards:
        hand1.add(c)   
    assert hand1.two() == True
    assert hand1.straight() == False
    assert hand1.same_suite() == False
    cards = [Card(Suite.hearts, Rank.eight), 
             Card(Suite.spades, Rank.three),
             Card(Suite.diamonds, Rank.five),
             Card(Suite.clubs, Rank.ace),
             Card(Suite.hearts, Rank.king)]
    hand2 = Hand()
    for c in cards:
        hand2.add(c)
    assert hand2.two() == False
    assert hand2.straight() == False
    assert hand2.same_suite() == False
    assert hand1.better(hand2) == True
    assert hand2.better(hand1) == False
    

