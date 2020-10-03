class Dice:
    def __init__(self, list_of_faces, ):
        assert type(list_of_faces) == list and len(list_of_faces) == 6
        self._faces = list_of_faces

    def getFaces(self):
        return self._faces

    def compareTO(self, dice):
        assert type(dice) == Dice
        dice1_wins, dice2_wins = 0, 0
        for x in self._faces:
            for y in dice.getFaces():
                if x > y:
                    dice1_wins += 1
                elif y > x:
                    dice2_wins += 1
        return dice1_wins, dice2_wins

    def __ge__(self, dice):
        assert type(dice) == Dice
        temp = self.compareTO(dice)
        return temp[0] >= temp[1]

    def __gt__(self, dice):
        assert type(dice) == Dice
        temp = self.compareTO(dice)
        return temp[0] > temp[1]

    def __le__(self, dice):
        assert type(dice) == Dice
        temp = self.compareTO(dice)
        return temp[0] <= temp[1]

    def __lt__(self, dice):
        assert type(dice) == Dice
        temp = self.compareTO(dice)
        return temp[0] < temp[1]

    def __eq__(self, dice):
        return self._faces == dice.getFaces()

    def __ne__(self, dice):
        return self._faces != dice.getFaces()

    def __str__(self):
        return  "Faces: "+ str(self._faces)


if __name__ == '__main__':
    test = [[1, 2, 3, 4, 5, 6],[1, 1, 2, 4, 5, 7],[1, 2, 2, 3, 4, 7]]
    test1 = [[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
    test2 = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
    test3 = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]] #1
    d1 = Dice(test[0])
    d2 = Dice(test[1])
    print(d1.compareTO(d2))

    print(d1>=d2)
    print(d1>d2)
    print(d1<d2)
    print(d1<=d2)
    print(d1==d2)
    print(d1!=d2)
    print(d1)
    print(d2)
