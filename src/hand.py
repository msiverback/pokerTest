from cgitb import handler
from .card import Card, Rank

class Hand:

    def __init__(self):
        self.hand = []
        self.__isTwo = False
        self.__isThree = False
        self.__isStraight = False
        self.__is_same = False

    def add(self, card : Card):
        for h in self.hand:
            if card.rank == h.rank:
                self.__isTwo = True
        self.hand.append(card)
        ranks = {i.name: 0 for i in Rank}
        for h in self.hand:
            ranks[h.rank.name] += 1
        maxIndex = max(ranks, key=ranks.get)
        if ranks[maxIndex] == 3:
            self.__isThree = True
        sortedHand = sorted(self.hand, key=lambda v: v.rank.value)
        diff = 0
        self.__isStraight = True
        for i in range(1,len(sortedHand)):
            diff = sortedHand[i].rank.value - sortedHand[i-1].rank.value
            if diff != 1:
                self.__isStraight = False
        suite = self.hand[0].suite
        for i in range(1, len(sortedHand)):
            if suite == sortedHand[i].suite:
                self.__is_same = True
            else:
                self.__is_same = False

    def two(self) -> bool:
        return self.__isTwo

    def three(self) -> bool:
        return self.__isThree

    def straight(self) -> bool:
        return self.__isStraight

    def same_suite(self):
        return self.__is_same

    def better(self, other) -> bool:
        if (not self.__isTwo and not self.straight() and not self.same_suite()):
            if (not other.__isTwo and not other.straight() and not other.same_suite()):
                #Highest cards wins
                self.hand.sort(key=lambda v: v.rank.value, reverse=True)
                other.hand.sort(key=lambda v: v.rank.value, reverse=True)
                for i in range(0,len(self.hand)-1):
                    if (self.hand[i].rank.value > other.hand[i].rank.value):
                        return True
                    elif (self.hand[i].rank.value < other.hand[i].rank.value):
                        return False
            return False
        elif(self.__isTwo and not self.straight() and not self.same_suite()):
            if (not other.__isTwo and not other.straight() and not other.same_suite()):
                return True
