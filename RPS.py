# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random 

steps = {}

def player(prev_play, opponent_history=[]):
  if prev_play != "":
    opponent_history.append(prev_play)
  choice = ['R', 'P', 'S']
  guess = random.choice(choice)

  n = 4 
  hist = opponent_history
  if len(hist) > n:
    pattern = join(hist[-n:])

    if join(hist[-(n + 1):]) in steps.keys():
      steps[join(hist[-(n + 1):])] += 1
    else:
      steps[join(hist[-(n + 1):])] = 1

    possible = [pattern + "R", pattern + "S", pattern + "P"]

    for i in possible:
      if not i in steps.keys():
        steps[i] = 0
  
    predict = max(possible, key = lambda key:steps[key])
  
    if predict[-1] == "R":
      guess = "P"
    elif predict[-1] == "P":
      guess = "S"
    elif predict[-1] == "S":
      guess = "R"  
  return guess

def join(moves):
  return "".join(moves)