opponent_moves = {"A": 1, "B": 2, "C": 3}
my_moves = {"X": 1, "Y": 2, "Z": 3}
winning_strategy = {"A": "Y", "B": "Z", "C": "X"}
losing_strategy = {"A": "Z", "B": "X", "C": "Y"}

score_after_each_round = []

for rounds in input.split("\n"):
  opponent, me = rounds.split(" ")
  if (me == "Z"):
    score_after_each_round.append(my_moves[winning_strategy[opponent]] + 6)
  elif (me == "Y"):
    score_after_each_round.append(opponent_moves[opponent] + 3)
  else:
    score_after_each_round.append(my_moves[losing_strategy[opponent]])

print(sum(score_after_each_round))
