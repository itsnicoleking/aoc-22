file = open("./inputs/day2_input.txt", "r")
lineList = [line.rstrip('\n') for line in file]
file.close

rockScore = 1
paperScore = 2
scissorsScore = 3
loseScore = 0
drawScore = 3
winScore = 6

# Part 1
ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

losingPlays = ['A Z', 'B X', 'C Y']
drawingPlays = ['A X', 'B Y', 'C Z']
winningPlays = ['A Y', 'B Z', 'C X']

def getTotalScore1():
  totalScore = 0

  for line in lineList:
    # Find win/lose/draw score
    if line in losingPlays:
      totalScore += loseScore
    elif line in drawingPlays:
      totalScore += drawScore
    elif line in winningPlays:
      totalScore += winScore
    # Find play score
    play = line.split()[1]
    if play == ROCK:
      totalScore += rockScore
    elif play == PAPER:
      totalScore += paperScore
    elif play == SCISSORS:
      totalScore += scissorsScore

  return totalScore

print ('Part 1:', getTotalScore1())

# Part 2
ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def getRoundScore(opponentPlay, outcome):
  roundScore = 0

# gross
  if outcome == LOSE:
    roundScore += loseScore
    if opponentPlay == ROCK:
      roundScore += scissorsScore
    elif opponentPlay == PAPER:
      roundScore += rockScore
    elif opponentPlay == SCISSORS:
      roundScore += paperScore
  
  elif outcome == DRAW:
    roundScore += drawScore
    if opponentPlay == ROCK:
      roundScore += rockScore
    elif opponentPlay == PAPER:
      roundScore += paperScore
    elif opponentPlay == SCISSORS:
      roundScore += scissorsScore

  elif outcome == WIN:
    roundScore += winScore
    if opponentPlay == ROCK:
      roundScore += paperScore
    elif opponentPlay == PAPER:
      roundScore += scissorsScore
    elif opponentPlay == SCISSORS:
      roundScore += rockScore

  return roundScore

def getTotalScore2():
  totalScore = 0

  for line in lineList:
    splittered = line.split()
    totalScore += getRoundScore(splittered[0], splittered[1])
  
  return totalScore

print ('Part 2:', getTotalScore2())
