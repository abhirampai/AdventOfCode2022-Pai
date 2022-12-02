my_moves = {"X": 1, "Y": 2, "Z": 3}
strategy = {"X": "B", "Y": "C", "Z": "A"}

score_after_each_round = []

for rounds in input.split("\n"):
  opponent, me = rounds.split(" ")
  if (strategy[me] == opponent):
    score_after_each_round.append(my_moves[me])
  elif (opponent_moves[opponent] == my_moves[me]):
    score_after_each_round.append(my_moves[me] + 3)
  else:
    score_after_each_round.append(my_moves[me] + 6)

print(sum(score_after_each_round))
