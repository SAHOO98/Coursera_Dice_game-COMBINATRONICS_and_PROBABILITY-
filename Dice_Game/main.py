from dice import Dice


class Oracle:
    def __init__(self, dices):
        assert type(dices) == list and all(len(dice) == 6 for dice in dices)
        self._dices = [Dice(dice) for dice in dices]

    def __len__(self):
        return len(self._dices)

    def __getitem__(self, index):
        assert type(index) == int and index >= 0
        return self._dices[index]

    def find_the_best_dice(self):
        n = len(self)
        flag = -2
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if self[i] > self[j]:
                    flag = i
                else:
                    flag = -1
                    break
            if flag != -1:
                break
        return flag

    def win_me_a_fortune(self):
        strategy = dict()
        index = self.find_the_best_dice()
        if index != -1:
            strategy["choose_first"] = True
            strategy["first_dice"] = index
        else:
            strategy["choose_first"] = False
            for i in range(len(self)):
                for j in range(len(self)):
                    if i == j: continue
                    if self[i] > self[j]:
                        strategy[i] = j
                        break
        return strategy


if __name__ == '__main__':
    test = [[1, 2, 3, 4, 5, 6], [1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7]]
    test1 = [[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
    test2 = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
    test3 = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]  # 1
    test4 = [[1, 4, 5, 6, 9, 10], [2, 2, 3, 7, 11, 11], [3, 4, 4, 5, 6, 12]]
    o = Oracle(test4)
    i = o.find_the_best_dice()
    if i >= 0:
        print('Best dice is: ', o[i])
    else:
        print('No best Dice.')

    print(o.win_me_a_fortune())
