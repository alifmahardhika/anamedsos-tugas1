a = "Goal! Manchester United 1, Burnley 1. James Tarkowski (Burnley) header from very close range to the top right corner. Assisted by Ashley Westwood with a cross following a corner."
a = a.split(".")
goal_scorer = a[1].split(" (")[0][1:]
# goal_scorer = goal_scorer[0]
assist = a[2].split(" ")[3]
print(goal_scorer)
print(assist)