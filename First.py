
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for x in dice1:
      for y in dice2:
        if x>y:
          dice1_wins+=1
        elif y>x:
          dice2_wins+=1
    return (dice1_wins, dice2_wins)

def d1_ge_d2(d1, d2):
  temp = count_wins(d1, d2)
  return temp[0]>temp[1]

def find_the_best_dice(dices):
  n = len(dices)
  flag = -2
  MAX = dices[0]
  for i in range(n):
    for j in range(n):
      if i==j: continue
      if d1_ge_d2(dices[i], dices[j]):
        flag = i
      else:
        flag=-1
        break
    if flag!=-1:
      break

  return flag

def compute_strategy(dices):
  strategy = dict()
  index = find_the_best_dice(dices)
  if index!=-1:
    strategy["choose_first"] = True
    strategy["first_dice"] = index
  else:
    strategy["choose_first"] = False
    for i in range(len(dices)):
      for j in range(len(dices)):
        if i==j: continue
        if d1_ge_d2(dices[j], dices[i]):
          strategy[i] = j
          break
  
  return strategy


i = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
j = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
k = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]] #2
b = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]] #1
h = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
test = [[1, 2, 3, 4, 5, 6],[1, 1, 2, 4, 5, 7],[1, 2, 2, 3, 4, 7]]
test1 = [[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
print(find_the_best_dice(test))
print(d1_ge_d2(test1[2], test1[3]))
print(count_wins(test1[2], test1[3]))

# for x in combinations(test1, 2):
#   print(count_wins(x[0], x[1]))
print(compute_strategy(test1))
